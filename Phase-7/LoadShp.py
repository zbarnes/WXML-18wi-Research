from PyQt4 import QtGui
#update file path for the shapefile in .zip
zip_uri = '/vsizip/U:/GIS DATA/WA Shape/WA Shape.zip'
shp =  QgsVectorLayer(zip_uri, 'WA Shape', 'ogr')
QgsMapLayerRegistry.instance().addMapLayer(shp)