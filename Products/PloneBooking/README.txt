============
PloneBooking
============


Required Products
=================

* Plone 3.x or Plone 4.x

Installing PloneBooking
=======================

* with the commands ``easy install Products.PloneBooking``.

* with buildout, just add ``Products.PloneBooking`` in your egg list then run
  ``bin/buildout``.

* Use ``portal_quickinstaller`` to install the PloneBooking in ZMI (or use
  plone_setup in Plone control panels)


Overview
========

PloneBooking proposes several content types for Plone: a booking center that
contains bookable objects and bookings.  You can do some configuration in your
booking center like choosing the default view or determining types and
categories for bookable objects.

How to book objects ?

1. Add a booking on a bookable object.

   * There are two methods :

     - Browse the calendar and click on the '+' in one of the cells.

     - Click "add booking" on a bookable object.

   * Then :

     - fill out the form: title (not necessary), your name and email.

     - Choose an interval for your booking.

     - You might want to add a comment.

     - Validate. Perhaps there is an other booking for the same object at the
       same time. If so change your request.

2. Adding periodicity settings to your booking (Wich will regularly duplicate
   your booking).

   - Select your booking in your calendar or in the listing view.

   - Click on the periodicity tab.

   - There are 3 kinds of periodicity.

   - Set the finishing date of your periodicity.

   - Click "display results". It will show you every booking to create.

   - Click "Create bookings" if you agree with the results.

.. admonition::
   Note

   - The first booking isn't shown as it's your original booking.
   - Some might be already booked. Select an other date or interval by coming
     back on the 'edit' tab.

3. Removing a booking

   - Come back to your booking throught the calendar view or listing view.

   - Click "Retract"

   - That's it, your booking has been removed.

.. admonition::
   Note

   Bookings you've just created can be in a pending state. (depending how your
   booking center has been set up). Just wait for a moderator to validate it.


PloneBooking Content Types
==========================

* ``BookingCenter``: it is the main container. You can create one or more
  BookingCenter on a plone site.

* ``BookableObject``: this is a ressource that users could book (like a room for
  example).

* ``Booking``: you create this kind of objet to book a BookableObject.

Additional tools

* ``BookingTool``

A tool is installed by the installer. It provides mainly some datemanagement
methods.

Credits
=======

Concept, development and tests
------------------------------

The Ingeniweb team http://www.ingeniweb.com

Translations
------------

Dutch by Sander van Geloven <sander@atopia.nl>

Italian by Vincenzo Barone <vincenzo.barone@abstract.it>
