This file contains configuration information for Products.PloneBooking 3.1
Version  3.1.1. works on Plone 4.3 and Plone 5, however you need first to prepare some steps.

Add manually following packages in buildout.cfg:
eggs =
    ....
    Products.PloneLanguageTool
    Products.PloneBooking

Disallow the CSRF function in Plone 5 as it will break a proper working Booking system completely.
If you do not want to do that then do not install this product or find time to rewrite it...

[instance]
....
environment-vars =
    PLONE_CSRF_DISABLED true
    
PLONE 4 preparation:
--------------------
Before installing on Plone 4! you need to rename or delete file registry.xml as that only works with Plone 5 resource registry.
The file is located in /your_path_to_Plone_eggs/Products.PloneBooking-3.1-py2.7.egg/Products/PloneBooking/profiles/default/registry.xml     


PLONE 4 and 5 preparation:
--------------------------
Use Add-on in Plone Control Panel or in ZMI the Plone QuickInstaller Tool at /your website/portal_quickinstaller to install the required packages.

Important: 
Products.PloneBooking uses Archetypes which is a subsystem to create content types in Plone 2.x, 3.x and 4.x.
Plone 5 uses Dexterity which is replacing Archetypes and is becoming the default content type. Dexterity is available since from Plone 4+.
Using Products.PloneBooking in Plone 5 requires installation of some extra packages in Plone. 

PLONE 5
The following Plone packages are added via the eggs listed above or are allready included in Plone 5 distribution and MUST be installed as well: 
- Archetypes-tools without content-types 	
- Content-types (plone.app.contenttypes) 
- PloneBooking 
- archetypes.multilingual 	
- plone.app.multilingual

After installation of Products.PloneBooking, verify the existence of property default_charset. 
This property will be created and it must exist. Check and adapt the value when needed.
Go in ZMI to: Plone Property Sheet at  /Plone/portal_properties/site_properties. 
Name: default_charset
Value: utf-8 (string)


DELETE OLD BOOKINGS:
You can clean outdated bookings with dates in provided interval.
        If max_date isn't prodvided, set to 6 month before current date.
        If min_date isn't prodvided, set to 6 month before max_date.
        If max_date and min_date aren't provided, cleaning interval is set as
        follow :
            min_date = (current_date - 12 months)
            max_date = (current_date - 6 months)
        :param min_date: oldest date
        :param max_date: recentest date
        
To run cleanup (delete old bookings) enter as Administrator url: http(s)://your_domain_and_optional_port/your_Plone_site/your_booking_center/janitor/clean_bookings
like this:      
http://localhost:8080/Plone/bookingcenter/janitor/clean_bookings?min_date=2015-01&max_date=2016-06
 

TROUBLESHOOTING:
When property default_charset does not exist an error will occur. It
 is quit difficult to find the root cause if you do not known about this missing property!

In Chrome 50.0.2661.102 and IExplorer 11 this error will be shown: {"error_type": "NotFound"},
while Firefox will show an overlay of the Home page. Using firebug following Javascript Error Message is shown: 

"NetworkError: 404 Not Found - http://localhost:8080/Plone/book-demos/booking_ajax_form?start_ts=1464822000&end_ts=1464823800"


Following error typically occurs when plone.app.multilingual is not installed:
 
   Module OFS.Traversable, line 285, in unrestrictedTraverse
   - __traceback_info__: ([], 'booking.2016-05-23.6283585679')
AttributeError: booking.2016-05-23.6283585679


If your problem is that your cannot list the content in a folder of a bookable object using your_bookable_object_folder_name//folder_contents
then maybe the reason is that you run into an error like this: ValueError: Circular reference detected

I have/had such a situation with bookings that were created for a bookable object using Products.PloneBooking in Plone 5 and not in Plone 4.3.

At the end the problem was caused by the Modification date string in JSON. This formatted date was of type DateTime (uppercase!)
That date looked like this: "ModificationDate": "2016-06-04T16:01:09+02:00"
JSON handler in plone.app.content (3.0.20) could not return a proper ISO format for that type.

I had to change this file: your_path\eggs\plone.app.content-3.0.20-py2.7.egg\plone\app\content\utils.py

It looks now like this and that works fine for me. Maybe you can try that to get a view of the content...

# -*- coding: utf-8 -*-
import Missing
import datetime
import json
from DateTime import DateTime

    def custom_json_handler(obj):
        if obj == Missing.Value:
            return None
        if type(obj) in (datetime.datetime, datetime.date):
            return obj.isoformat()
        if type(obj) in (DateTime, ):
            dt =   DateTime(obj)       
            return dt.ISO()
        return obj


    def json_dumps(data):
        return json.dumps(data, default=custom_json_handler)


# can eventually provide custom handling here if we want
json_loads = json.loads