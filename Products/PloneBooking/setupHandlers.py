from Products.CMFCore.utils import getToolByName
import logging


def addCatalogIndexes(context):
    """Setup handler to add indexes to the portal catalog
    """
    # TODO: This should go to the catalog.xml GS profile file
    if context.readDataFile('plonebooking_various.txt') is None:
        return

    portal = context.getSite()
    logger = logging.getLogger("PloneBooking.addCatalogIndexes")

    catalog = getToolByName(portal, 'portal_catalog')
    indexes = catalog.indexes()

    wanted = [
        ('getType', 'FieldIndex', {'indexed_attrs':'getType'}),
        ('getCategory', 'FieldIndex', {'indexed_attrs':'getCategory'}),
        ('getStartDate', 'FieldIndex', {'indexed_attrs':'getStartDate'}),
        ('getEndDate', 'FieldIndex', {'indexed_attrs':'getEndDate'}),
        ('getBookedObjectUID', 'FieldIndex', {'indexed_attrs':'getBookedObjectUID'}),
        ('getPeriodicityUID', 'FieldIndex', {'indexed_attrs':'getPeriodicityUID'})
        ]
    indexables = []
    for idx in wanted:
        if idx[0] in indexes:
            logger.info("Found the '%s' index in the catalog." % idx[0])
        else:
            catalog.addIndex(name=idx[0], type=idx[1], extra=idx[2])
            logger.info("Added '%s' (%s) to the catalog. You should use catalog.xml instead." % (idx[0], idx[1]))
        indexables.append(idx[0])
    if len(indexables) > 0:
        logger.info('Indexing %s.' % ', '.join(indexables))
        catalog.manage_reindexIndex(ids=indexables)
