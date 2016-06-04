# -*- coding: utf-8 -*-

from Products.Five.browser import BrowserView
from Products.CMFCore.utils import getToolByName
from Products.statusmessages.interfaces import IStatusMessage

import logging
logger = logging.getLogger("Products.PloneBooking")


class Janitor(BrowserView):
    """Provides few browser methods to maintain the booking center
    fully operational.
    """

    def clean_bookings(self):
        """Allow the call of the same BookingCenter method by URL."""
        booking_tool = getToolByName(self.context, 'portal_booking')
        status, msg = booking_tool.clean_bookings(
            self.request.get('min_date', None),
            self.request.get('max_date', None)
        )
        if status:
            logger.info(msg)
            IStatusMessage(self.request).addStatusMessage(msg, 'info')
        else:
            logger.warning(msg)
            IStatusMessage(self.request).addStatusMessage(msg, 'warning')
        return self.request.RESPONSE.redirect(self.context.absolute_url())
