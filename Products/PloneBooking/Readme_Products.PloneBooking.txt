This file contains configuration information for Products.PloneBooking 3.1
Version  3.1 works on Plone 4.3 and Plone 5, however you need first to prepare some steps.

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
    
    
Before installing on Plone 5 you need to rename or delete filet registry.xml as that only works with Plone 5 resource registry.
The file is located in /your_path_to_Plone_eggs/Products.PloneBooking-3.1-py2.7.egg/Products/PloneBooking/profiles/default/registry.xml     
    
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


 
TROUBLESHOOTING:
When property default_charset does not exist an error will occur. It
 is quit difficult to find the root cause if you do not known about this missing property!

In Chrome 50.0.2661.102 and IExplorer 11 this error will be shown: {"error_type": "NotFound"}

Firefox shows an overlay of the Home page.
Using firebug following Javascript Error Message is shown: .

"NetworkError: 404 Not Found - http://localhost:8080/Plone/book-demos/booking_ajax_form?start_ts=1464822000&end_ts=1464823800"


Foollowing error typically occurs when plone.app.multilingual is not installed:
 
   Module OFS.Traversable, line 285, in unrestrictedTraverse
   - __traceback_info__: ([], 'booking.2016-05-23.6283585679')
AttributeError: booking.2016-05-23.6283585679