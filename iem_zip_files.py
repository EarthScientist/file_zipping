import zipfile, os, sys

compression = zipfile.ZIP_DEFLATED

os.chdir("/big_storage/malindgren/AIEM/ZIP")

# here lets create a list of the data we want in each of the zip groups
year_groups = [range(1901,2010)]
variables = ["tas","pr"]
months = ["01","02","03","04","05","06","07","08","09","10","11","12"]
models = ["cru_TS31"]
for model in models:
	print model
	for val in [0]:
		filelist=[]
		for v in variables:
			print 'creating archive'
			zf = zipfile.ZipFile(model+"_"+v+"_"+str(year_groups[val][0])+".zip", mode='w', allowZip64=True)
			for year in year_groups[val]:
				for mon in months:
					if v == "tas":
						# filelist.append(os.path.join("/big_storage/malindgren/AIEM/ALFRESCO_AIEM_CLIP/ALFRESCO_Master_Dataset/ALFRESCO_Model_Input_Datasets/AK_CAN_Inputs/Climate",model,"sresa1b","tas","tas_mean_C_iem_ar4_cccma_cgcm3_1_sresa1b_"+mon+"_"+year+".tif"))
						zf.write(os.path.join("/big_storage/malindgren/AIEM/ALFRESCO_AIEM_CLIP/Climate",model,"historical","tas","tas_mean_C_iem_"+model+"_"+mon+"_"+str(year)+".tif"), arcname="tas_mean_C_iem_"+model+"_"+mon+"_"+str(year)+".tif",compress_type=compression)
					else:
						# filelist.append(os.path.join("/big_storage/malindgren/AIEM/ALFRESCO_AIEM_CLIP/ALFRESCO_Master_Dataset/ALFRESCO_Model_Input_Datasets/AK_CAN_Inputs/Climate",model,"sresa1b","pr","pr_total_mm_iem_ar4_cccma_cgcm3_1_sresa1b_"+mon+"_"+year+".tif"))
						zf.write(os.path.join("/big_storage/malindgren/AIEM/ALFRESCO_AIEM_CLIP/Climate",model,"historical","pr","pr_total_mm_iem_"+model+"_"+mon+"_"+str(year)+".tif"), arcname="pr_total_mm_iem_"+model+"_"+mon+"_"+str(year)+".tif", compress_type=compression)
			print 'closing'
			zf.close()
