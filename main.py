import glob
import os
path = r'C:\Users\Junaid\PycharmProjects\csv-to-geopackage'
for csv in glob.glob(ruta + '/*.csv'):
    rutacsv = 'file:///' + csv + '?delimiter=,'
    tabla = QgsVectorLayer(rutacsv, os.path.basename(csv), 'delimitedtext')
    opt = QgsVectorFileWriter.SaveVectorOptions()
    opt.EditionCapability = QgsVectorFileWriter.CanAddNewLayer
    opt.layerName = os.path.basename(csv).split('.csv', 1)[0]
    opt.actionOnExistingFile = QgsVectorFileWriter.CreateOrOverwriteLayer
    QgsVectorFileWriter.writeAsVectorFormat(tabla, ruta + '/cdau.gpkg', opt)
    print ('completed')
