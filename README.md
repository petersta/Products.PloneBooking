# Products.PloneBooking
A booking center for Plone


This a a fork which works with Plone 4.3 more precise: Plone 4.3.4.1 (4309). It is in production for more than 1 year.
It works also with Plone 5 (CSRF switched off)

See README.txt and Readme_Products.PloneBooking.txt for detailed information, installation & troubleshooting

When requesting a booking a request form has following fields (one extra):
- Full name of the person booking
- Phone
- Email
- Booking title
- Comment 

The layout and look-and-feel of the popups is somewhat adapted. Better error handling and tested.

You can now book a extra periodicity  type (recurring booking). The following Periodicity types are supported:
- Same day and hour every week
- Same day and hour every weeks
- Same day and hour every month (e.g. every 2nd monday of the month)
- Every day same time to the Periodicity end date   --> New

There is a link on the booking page to http://www.timeanddate.com/worldclock/converter.html
Products.PloenBooking works with your local timezone. For international bookings and 24 hrs around the clock you will
need to book against the time zoen that Plone uses. So you need to convert you own time to the runtime (zone).
On the booking page you will find this message with link: "Check here for the time zone difference to the booking date!"

In order to work properly  a site_property must exist (or manually  created) under portal_properties/site_properties
Name of property is: default_charset
Value of this property is: utf-8  or ISO-8859-15 or your own value.


Hopefully you like this version. It is a much better version. Folllow the installation instructions carefully.
Regards
