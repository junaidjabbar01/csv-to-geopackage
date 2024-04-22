import glob
import os
from osgeo import ogr

gpkg_path = r'C:\Users\Admin\PycharmProjects\csv-to-geopackage\empty_geopackage.gpkg'
path = r'C:\Users\Admin\PycharmProjects\csv-to-geopackage'
# Create a new GeoPackage datasource
driver = ogr.GetDriverByName('GPKG')
datasource = driver.CreateDataSource(gpkg_path)

if datasource is None:
    print("Creation of GeoPackage file failed.")
  #  return False


# Create a dummy layer (a point layer with no features)
#layer_name = 'dummy'
#spatial_reference = ogr.osr.SpatialReference()
#spatial_reference.ImportFromEPSG(4326)  # WGS84
#layer = datasource.CreateLayer(layer_name, spatial_reference, ogr.wkbPoint)


for csv in glob.glob(path + '/*.csv'):
    
    csv_file = 'file:///' + csv + '?delimiter=,'
    table = QgsVectorLayer(csv_file, os.path.basename(csv), 'delimitedtext')
    opt = QgsVectorFileWriter.SaveVectorOptions()
    opt.EditionCapability = QgsVectorFileWriter.CanAddNewLayer
    opt.layerName = os.path.basename(csv).split('.csv', 1)[0]
    opt.actionOnExistingFile = QgsVectorFileWriter.CreateOrOverwriteLayer
    QgsVectorFileWriter.writeAsVectorFormat(table, gpkg_path, opt)
    print ('completed')
    
# Close the datasource
datasource = None
print(f"Empty GeoPackage file created at: {gpkg_path}")