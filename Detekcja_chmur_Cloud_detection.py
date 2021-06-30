!pip install shapely
!pip install lightgbm
!pip install s2cloudless

from s2cloudless import S2PixelCloudDetector
import numpy as np
import rasterio
from rasterio.warp import reproject, Resampling
from osgeo import gdal

#Band 1
with rasterio.open("C:\\Users\\eliza\\Desktop\\Sentinel_2\\S2A_OPER_MSI_L1C_TL_EPA__20160815T031336_A000462_T34UEV_B01.jp2") as scl:
    B01=scl.read()
    tmparr = np.empty_like(B01)
    aff = scl.transform
    print(B01.shape)


referenceFile = "C:\\Users\\eliza\\Desktop\\Cloud Detection\\Cloud files\\S2A_OPER_MSI_L1C_TL_SGS__20160825T132122_A006139_T34UEV_B01.jp2"
reference = gdal.Open(referenceFile, 0)
referenceTrans = reference.GetGeoTransform()
x_res = referenceTrans[1]
y_res = -referenceTrans[5]

#Specify input and output filenames
inputFile_2 = "C:\\Users\\eliza\\Desktop\\Cloud Detection\\Cloud files\\S2A_OPER_MSI_L1C_TL_SGS__20160825T132122_A006139_T34UEV_B02.jp2"
outputFile_2 = "C:\\Users\\eliza\\Desktop\\Cloud Detection\\Reproject files\\S2A_OPER_MSI_L1C_TL_SGS__20160825T132122_A006139_T34UEV_B02.tif"

inputFile_4 = "C:\\Users\\eliza\\Desktop\\Cloud Detection\\Cloud files\\S2A_OPER_MSI_L1C_TL_SGS__20160825T132122_A006139_T34UEV_B04.jp2"
outputFile_4 = "C:\\Users\\eliza\\Desktop\\Cloud Detection\\Reproject files\\S2A_OPER_MSI_L1C_TL_SGS__20160825T132122_A006139_T34UEV_B04.tif"

inputFile_5 = "C:\\Users\\eliza\\Desktop\\Cloud Detection\\Cloud files\\S2A_OPER_MSI_L1C_TL_SGS__20160825T132122_A006139_T34UEV_B05.jp2"
outputFile_5 = "C:\\Users\\eliza\\Desktop\\Cloud Detection\\Reproject files\\S2A_OPER_MSI_L1C_TL_SGS__20160825T132122_A006139_T34UEV_B05.tif"

inputFile_8 = "C:\\Users\\eliza\\Desktop\\Cloud Detection\\Cloud files\\S2A_OPER_MSI_L1C_TL_SGS__20160825T132122_A006139_T34UEV_B08.jp2"
outputFile_8 = "C:\\Users\\eliza\\Desktop\\Cloud Detection\\Reproject files\\S2A_OPER_MSI_L1C_TL_SGS__20160825T132122_A006139_T34UEV_B08.tif"

inputFile_8A = "C:\\Users\\eliza\\Desktop\\Cloud Detection\\Cloud files\\S2A_OPER_MSI_L1C_TL_SGS__20160825T132122_A006139_T34UEV_B8A.jp2"
outputFile_8A = "C:\\Users\\eliza\\Desktop\\Cloud Detection\\Reproject files\\S2A_OPER_MSI_L1C_TL_SGS__20160825T132122_A006139_T34UEV_B8A.tif"

inputFile_11 = "C:\\Users\\eliza\\Desktop\\Cloud Detection\\Cloud files\\S2A_OPER_MSI_L1C_TL_SGS__20160825T132122_A006139_T34UEV_B11.jp2"
outputFile_11 = "C:\\Users\\eliza\\Desktop\\Cloud Detection\\Reproject files\\S2A_OPER_MSI_L1C_TL_SGS__20160825T132122_A006139_T34UEV_B11.tif"

inputFile_12 = "C:\\Users\\eliza\\Desktop\\Cloud Detection\\Cloud files\\S2A_OPER_MSI_L1C_TL_SGS__20160825T132122_A006139_T34UEV_B12.jp2"
outputFile_12 = "C:\\Users\\eliza\\Desktop\\Cloud Detection\\Reproject files\\S2A_OPER_MSI_L1C_TL_SGS__20160825T132122_A006139_T34UEV_B12.tif"

# Call gdal Warp
kwargs = {"format": "GTiff", "xRes": x_res, "yRes": y_res}
ds_2 = gdal.Warp(outputFile_2, inputFile_2, **kwargs)
ds_4 = gdal.Warp(outputFile_4, inputFile_4, **kwargs)
ds_5 = gdal.Warp(outputFile_5, inputFile_5, **kwargs)
ds_8 = gdal.Warp(outputFile_8, inputFile_8, **kwargs)
ds_8A = gdal.Warp(outputFile_8A, inputFile_8A, **kwargs)
ds_11 = gdal.Warp(outputFile_11, inputFile_11, **kwargs)
ds_12 = gdal.Warp(outputFile_12, inputFile_12, **kwargs)


with rasterio.open("C:\\Users\\eliza\\Desktop\\Cloud Detection\\Cloud files\\S2A_OPER_MSI_L1C_TL_SGS__20160825T132122_A006139_T34UEV_B09.jp2") as scl_9:
    B09=scl_9.read()

with rasterio.open("C:\\Users\\eliza\\Desktop\\Cloud Detection\\Cloud files\\S2A_OPER_MSI_L1C_TL_SGS__20160825T132122_A006139_T34UEV_B10.jp2") as scl_10:
    B10=scl_10.read()
    
with rasterio.open("C:\\Users\\eliza\\Desktop\\Cloud Detection\\Reproject files\\S2A_OPER_MSI_L1C_TL_SGS__20160825T132122_A006139_T34UEV_B02.tif") as scl_2:
    B02=scl_2.read()
    
with rasterio.open("C:\\Users\\eliza\\Desktop\\Cloud Detection\\Reproject files\\S2A_OPER_MSI_L1C_TL_SGS__20160825T132122_A006139_T34UEV_B04.tif") as scl_4:
    B04=scl_4.read()
    
with rasterio.open("C:\\Users\\eliza\\Desktop\\Cloud Detection\\Reproject files\\S2A_OPER_MSI_L1C_TL_SGS__20160825T132122_A006139_T34UEV_B05.tif") as scl_5:
    B05=scl_5.read()
    
with rasterio.open("C:\\Users\\eliza\\Desktop\\Cloud Detection\\Reproject files\\S2A_OPER_MSI_L1C_TL_SGS__20160825T132122_A006139_T34UEV_B08.tif") as scl_8:
    B08=scl_8.read()
    
with rasterio.open("C:\\Users\\eliza\\Desktop\\Cloud Detection\\Reproject files\\S2A_OPER_MSI_L1C_TL_SGS__20160825T132122_A006139_T34UEV_B8A.tif") as scl_8A:
    B8A=scl_8A.read()
    
with rasterio.open("C:\\Users\\eliza\\Desktop\\Cloud Detection\\Reproject files\\S2A_OPER_MSI_L1C_TL_SGS__20160825T132122_A006139_T34UEV_B11.tif") as scl_11:
    B11=scl_11.read()
    
with rasterio.open("C:\\Users\\eliza\\Desktop\\Cloud Detection\\Reproject files\\S2A_OPER_MSI_L1C_TL_SGS__20160825T132122_A006139_T34UEV_B12.tif") as scl_12:
    B12=scl_12.read()


bands = np.array([np.dstack((B01[0]/10000.0,B02[0]/10000.0,B04[0]/10000.0,B05[0]/10000.0,B08[0]/10000.0,B8A[0]/10000.0,B09[0]/10000.0,B10[0]/10000.0,B11[0]/10000.0,B12[0]/10000.0))])
print(bands.shape)
cloud_detector = S2PixelCloudDetector(threshold=0.4, average_over=4, dilation_size=2)
cloud_probs = cloud_detector.get_cloud_probability_maps(bands)
mask = cloud_detector.get_cloud_masks(bands).astype(rasterio.uint8)
with rasterio.open("C:\\Users\\eliza\\Desktop\\Cloud Detection\\Cloudless files\\clouds.tif", "w",  driver='GTiff',compress="lzw",height=mask.shape[1],width=mask.shape[2],count=1,dtype=rasterio.uint8) as dest:
    dest.write(mask)
with rasterio.open("C:\\Users\\eliza\\Desktop\\Cloud Detection\\Cloudless files\\clouds_prob.tif", "w",  driver='GTiff',compress="lzw",height=cloud_probs.shape[1],width=cloud_probs.shape[2],count=1,dtype=cloud_probs.dtype) as dest:
    dest.write(cloud_probs)













