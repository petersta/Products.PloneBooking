# -*- coding: utf-8 -*-
## PloneBooking: Online Booking Tool to allow booking on any kind of ressource
## Copyright (C)2005 Ingeniweb

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

"""PloneBooking: Interfaces"""

# $Source: /isp/cvs/repository/zope/products/PloneBooking/interfaces/interfaces.py,v $
# $Id: interfaces.py,v 1.5 2006/04/07 13:49:33 cbosse Exp $
__version__ = "$Revision: 1.5 $"
__author__ = ''
__docformat__ = 'restructuredtext'

from zope.interface import Interface


class IBooking(Interface):
    """This interface proposes methods to access to Booked Objects, and get the
    booking period.
    """

    def getBookedObject(UID):
        """Booked object by IUD
        :param UID: uid of bookable object
        """

    def getBookedObjectRefs():
        """Return all booked objects referenced in Booking.
        """

    def getBookedObjectUIDs():
        """All Booked Objects uids referenced in Booking.
        """

    def isBookingObject(UID):
        """Return true if the booking books the object with the given UID.
        :param UID: uid of bookable object
        """

    def isBookingObjects(uids_list):

        """True if the booking books one of the object (from uid's list).
        :param uids_list: list of uids of bookable objects
        """

    def hasBookedObject(UID, start_date, end_date):
        """True if there are booked object during the given period.
        :param UID: uid of bookable
        :param start_date: start of period as :class:`DateTime.DateTime`
        :param end_date: end of period as :class:`DateTime.DateTime`
        """

    def hasBookedObjects(uids_list, start_date, end_date):
        """
        :param uids_list: list of uids to test
        :param start_date: Date of booking's start
        :param end_date: Date of booking's end
        """


class IBookingCenter(Interface):
    """This interface proposes methods to access contains of a Booking Center.
    """
    def getBookingCenter():
        """Return the Booking center itself
        """

    def getBookings(sort=''):
        """Return all Bookings contained in the BookingCenter.
        """

    def getBookingContainer():
        """Return the booking container.
        """

    def getBookableObjectContainer():
        """Return the bookable object container.
        """

    def getBookedObjects():
        """Return all booked object in container
        """


class IBookableObject(Interface):
    """This interface proposes methods to know if an object is booked.
    """
    def isBooked():
        """True if the object has booking
        """


class IBookingExporter(Interface):
    """Utility methods to format and manipulate exports fields
    """
