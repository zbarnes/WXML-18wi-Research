from PyQt4 import QtGui
#File paths must be updated
#Load .shp file from a .zip file 
shp_zip = '/vsizip/C:/Users/zbarnes/Downloads/WA Shape.zip/WA_final.shp'
shp =  QgsVectorLayer(shp_zip, 'WA_final', 'ogr')
QgsMapLayerRegistry.instance().addMapLayer(shp)

#Load csv file
csv_file = "file:///C:/Users/zbarnes/Downloads/TestMap.csv?delimiter=,"
csv = QgsVectorLayer(csv_file, "TestMap", "delimitedtext")
QgsMapLayerRegistry.instance().addMapLayer(csv)

#Join csv file with header WA_GEO_ID and the WA_GEO_ID field in .shp
shpJoinField='WA_GEO_ID'
csvJoinField='WA_GEO_ID'
joinObject = QgsVectorJoinInfo()
joinObject.joinLayerId = csv.id()
joinObject.joinFieldName = csvJoinField
joinObject.targetFieldName = shpJoinField
joinObject.memoryCache = True
shp.addJoin(joinObject)
