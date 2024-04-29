import glob
import os
from osgeo import ogr
import pandas as pd

gpkg_path = r'C:\Users\Admin\PycharmProjects\csv-to-geopackage\empty_geopackage.gpkg'
path = r'C:\Users\Admin\PycharmProjects\csv-to-geopackage\data\data_csv'
# Create a new GeoPackage datasource
driver = ogr.GetDriverByName('GPKG')
datasource = driver.CreateDataSource(gpkg_path)

def split_excel_to_csv(excel_file):
    # Load Excel file
    xls = pd.ExcelFile(excel_file)
    # Create a directory to store CSV files
    output_dir = os.path.splitext(excel_file)[0] + "_csv"
    os.makedirs(output_dir, exist_ok=True)
    
    # Iterate over each sheet and write to CSV
    for sheet_name in xls.sheet_names:
        df = xls.parse(sheet_name)
        csv_file = os.path.join(output_dir, f"{sheet_name}.csv")
        df.to_csv(csv_file, index=False)
        print(f"Sheet '{sheet_name}' saved as '{csv_file}'")

excel_file_path = r"C:\Users\Admin\PycharmProjects\csv-to-geopackage\data\data_3.xlsx"  # Replace with the path to your Excel file
split_excel_to_csv(excel_file_path)

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