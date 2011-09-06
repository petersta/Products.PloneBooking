# -*- coding: utf-8 -*-
## PloneBooking: Online Booking Tool to allow booking on any kind of ressource
## Copyright (C) 2008 Ingeniweb

## This program is free software; you can redistribute it and/or modify
## it under the terms of the GNU General Public License as published by
## the Free Software Foundation; either version 2 of the License, or
## (at your option) any later version.

## This program is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU General Public License for more details.

## You should have received a copy of the GNU General Public License
## along with this program; see the file COPYING. If not, write to the
## Free Software Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.
"""
"""

import csv
import cStringIO
from zope.component import getUtility
from zope.interface import implements
from DateTime import DateTime
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.CMFCore.utils import getToolByName
from Products.statusmessages.interfaces import IStatusMessage
from Products.PloneBooking.config import EXPORT_MAX_RANGE_DAYS
from Products.PloneBooking.interfaces import IBookingExporter
from Products.PloneBooking import PloneBookingFactory as _


class BookingExporter:
    """
        Basic implementation of a Booking exporter.
        You can orverride this implementation by using some
        ZCML in an overrides.zcml
    """

    implements(IBookingExporter)

    def getFields(self):
        """
            Return the labels of all the fields for this export
        """
        return [
            _("label_booking_title", "Title"),
            _("label_booking_user_full_name", "Full Name"),
            _("label_booking_user_phone", "Phone"),
            _("label_booking_user_email", "Email"),
            _("label_booking_start_date", "Booking start date"),
            _("label_booking_end_date", "Booking end date"),
            _("label_booking_description", "Booking note"),
        ]

    def getValues(self, brains):
        """
            Return a list of values associated with this brain.
        """
        results = []
        for brain in brains:
            ## wake up the object: perhaps there is another way to do that
            ## but I don't think it's very efficient to put all the data
            ## of the booking in the catalog metadata...
            booking = brain.getObject()
            results.append(
                (
                    booking.Title(),
                    booking.getFullName(),
                    booking.getPhone(),
                    booking.getEmail(),
                    booking.getStartDate().strftime("%Y/%m/%d-%H:%M"),
                    booking.getEndDate().strftime("%Y/%m/%d-%H:%M"),
                    booking.Description(),
                )
            )

        return results
    
    def getPortalType(self):
        """
            Return the portal to use for the request
        """
        return "Booking"

    def getEncoding(self):
        """
            Get the encoding that will be used for the CSV export
        """
        return "utf-8"

class Export(BrowserView):
    """
        Export the bookables of a selected ressource (ressource type given
        in the context)
    """

    result_template = ViewPageTemplateFile('export_form.pt')

    def __call__(self):
        # implements(IBookingExporter)
        self.exporter = getUtility(IBookingExporter)
        self.formAction = self.request.form.get("form.action", None) is not None
        self.formResults = None
        if self.formAction and self.checkValues():
            values = self.exporter.getValues(self.getBrains())
            if len(values) == 0:
                self.postMessage(
                        _(u"info_no_results",
                          default = u"There is no booking matching your criteria."
                        ),
                        "info"
                )
                return self.result_template()
            if self.request.form.get("export_type") == "csv":
                return self.exportToCsv(values)
            if self.request.form.get("export_type") == "html":
                self.formResults = values
        return self.result_template()

    def checkValues(self):
        try:
            self.start = DateTime(int(self.request.form.get("ts_start", None)))
            self.end = DateTime(int(self.request.form.get("ts_end", None)))
        except:
            self.postMessage(
                    _(
                      u"error_key_error",
                      default = u"Key error"
                    ),
                    "error"
            )
            return False
        if self.start > self.end:
            self.postMessage(
                    _(u'error_end_before_start',
                      default = u"Start date great than End date."
                    ),
                    "error"
            )
            return False
        if self.start + EXPORT_MAX_RANGE_DAYS < self.end:
            # in this case, the range is too big: we filter to have a range
            # that is less than EXPORT_MAX_RANGE_DAYS value.
            self.postMessage(
                    _(u'error_range_too_large',
                      default = u"Please enter a range that fits into ${number} monthes.",
                      mapping = {u"number": int(EXPORT_MAX_RANGE_DAYS/30)}
                    ),
                    "error"
            )
            return False
        # all tests passed
        return True

    def postMessage(self,msgid,messageType):
        translated = self.context.translate(msgid)
        messages = IStatusMessage(self.request)
        messages.addStatusMessage(translated, type=messageType)

    def getBrains(self):
        """
            Get the brains associated with the export request
        """
        catalog = getToolByName(self.context, "portal_catalog")
        query = {
                # TODO: perhaps replace this criterion with "provided_by"
                # once the interface would appear in the catalog...
                "portal_type": self.exporter.getPortalType(),
                "path": "/".join(self.context.getPhysicalPath()),
                "start": {
                        "query": self.start,
                        "range": "min",
                },
                "end": {
                        "query": self.end,
                        "range": "max",
                },
        }
        brains = catalog(**query)
        return brains

    def getFields(self):
        """
            Return translated fields in a list of unicode
        """
        fields = getUtility(IBookingExporter).getFields()
        return [self.context.translate(field, domain=field.domain) for field in fields]

    def getResults(self):
        return self.formResults

    def getEncoding(self):
        """
            Return the encoding of the CSV file
        """
        return getUtility(IBookingExporter).getEncoding()

    def exportToCsv(self, values):
        """
            Called only when the user select "CSV" export type
        """
        fields = self.getFields()

        stream = cStringIO.StringIO()
        writer = csv.writer(stream)
        encoding = self.getEncoding()

        writer.writerow([field.encode(encoding) for field in fields])
        writer.writerows(values)

        result = stream.getvalue()
        stream.close()
        response = self.request.response
        response.setHeader("Content-Type", "text/csv")
        response.setHeader("Content-Encoding", encoding)
        response.setHeader(
            "Content-Disposition",
            "attachment; filename=booking-%s-%s-%s.csv" % (
                self.context.getId(),
                self.start.strftime("%Y%m%d"),
                self.end.strftime("%Y%m%d"),
            )
        )
        return result
