============
PloneBooking
============

See CHANGES.txt as well for complete change log overview for all versions.

ChangeLog version 3.1.1
=======================
Added most functions and corrections of atreal such as interval and permissions translation uid_catalog and cleanup (thanks tiazma!)

Unfortenately there is a small difference between Plone 4 and 5 in the execution of the TAL define statement in file booking_peridodicity_form starting at line 85.
Therefore a very small change "_0" was required in file plonebooking.js from line 19 onwards in function showPeriodicityResult. This file is located here: 
/your_path_to_Plone_eggsProducts.PloneBooking-3.1.1-py2.7.egg/Products/PloneBooking/skins/plonebooking_javascripts/plonebooking.js
The following test solves the issue for Plone 4.3 and Plone 5
    if (form['periodicity_form_periodicity_end_date'] === undefined) {
        periodicity_end_date = form['periodicity_form_periodicity_end_date_0'].value; // Plone 4 works only with  "_0" in fieldname!. It should then be form['periodicity_form_periodicity_end_date_0'].value;
    } else {
        periodicity_end_date = form['periodicity_form_periodicity_end_date'].value; // Plone 5 works only with no "_0" in fieldname!. It should then be form['periodicity_form_periodicity_end_date'].value;
    }

ChangeLog version 3.1
=====================
* Compatible with Plone 4 and Plone 5 (requires switch-off of new CSRF feature!)
* Adapted README.txt
* Extra Installation Guidelines and TroubleShouting hints in Readme_Products.PloneBooking.txt
* Various corrections (NO Anonymous Booking is possible) 
* Now better error handling and more important a really working PloneBooking.js script. Tested in Chrome, Firefox and IExlorer
* Correction in macro plonebooking_macros.pt ``comma`` declaration in tal attribute worked in Plone 4, not in Plone 5
* New fields on BookingForm: Phone Number and Comments
* Extra Periodicty option: Every day same time to the Periodicity end date 
* Changed Layout & Colors in pop-ups, Wider Popup to accommodate 0-24 hrs timerange
* Missing Icons Added


Required Products
=================

* Plone 4.x or Plone 5
Note that new data elements on the Bookingform has been added compared with previous versions 3.0 and lower

Installing & troubleshooting PloneBooking
=========================================
See Readme_Products.PloneBooking.txt


Overview
========

PloneBooking proposes several content types for Plone: a booking center that
contains bookable objects and bookings.  You can do some configuration in your
booking center like choosing the default view or determining types and
categories for bookable objects.

How to book objects ?
You must login to do bookings (requires Authenticated user), 
Viewing bookings is possible as Anonymous user.

1. Add a booking on a bookable object.

   * There are two methods :

     - Browse the calendar and click on the '+' in one of the cells.

     - Click "add booking" on a bookable object.

   * Then :

     - fill out the form:  your number, phone number and email, booking title, comment (not necessary).

     - Choose an time slot (interval) for your booking.

     - You might want to add a comment.

     - Validate. Perhaps there is an other booking for the same object at the
       same time. If so change your request.

2. Adding periodicity settings to your booking (Wich will regularly duplicate
   your booking).

   - Select your booking in your calendar or in the listing view.

   - Click on the periodicity tab.

   - There are 4 kinds of periodicity (one new type is added in this version).
      - Same day and hour every week 
      - Same day and hour every x weeks
      - Same day and hour every month (e.g. every 2nd monday of the month) 
      - Every day same time to the Periodicity end date 

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
version 3.1 extended,corrected and ported to Plone 4.3 and 5 by PetSta

Translations
------------

Dutch by Sander van Geloven <sander@atopia.nl>

Italian by Vincenzo Barone <vincenzo.barone@abstract.it>
