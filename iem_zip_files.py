from zipfile_infolist import vapint_info
import zipfile, os, sys

compression = zipfile.ZIP_DEFLATED

os.chdir("/big_storage/malindgren/AIEM/ZIP")

# here lets create a list of the data we want in each of the zip groups
year_groups = [range(1901,2009)]
variables = ["rsds","vap"]
months = ["01","02","03","04","05","06","07","08","09","10","11","12"]
models = ["cru_TS31"]
for model in models:
	print model
	for val in [0,1]:
		filelist=[]
		for v in variables:
			print 'creating archive'
			zf = zipfile.ZipFile(model+"_"+v+"_"+str(year_groups[val][0])+".zip", mode='w', allowZip64=True)
			for year in year_groups[val]:
				for mon in months:
					if v == "rsds":
						# filelist.append(os.path.join("/big_storage/malindgren/AIEM/ALFRESCO_AIEM_CLIP/ALFRESCO_Master_Darsdset/ALFRESCO_Model_Input_Darsdsets/AK_CAN_Inputs/Climate",model,"sresa1b","rsds","rsds_mean_C_iem_ar4_cccma_cgcm3_1_sresa1b_"+mon+"_"+year+".tif"))
						zf.write(os.path.join("/big_storage/malindgren/AIEM/ALFRESCO_AIEM_CLIP/Climate",model,"historical","rsds","rsds_mean_wm-2_iem_"+model+"_"+mon+"_"+str(year)+".tif"), arcname="rsds_mean_wm-2_iem_"+model+"_"+mon+"_"+str(year)+".tif",compress_type=compression)
					else:
						# filelist.append(os.path.join("/big_storage/malindgren/AIEM/ALFRESCO_AIEM_CLIP/ALFRESCO_Master_Darsdset/ALFRESCO_Model_Input_Darsdsets/AK_CAN_Inputs/Climate",model,"sresa1b","vap","vap_total_mm_iem_ar4_cccma_cgcm3_1_sresa1b_"+mon+"_"+year+".tif"))
						zf.write(os.path.join("/big_storage/malindgren/AIEM/ALFRESCO_AIEM_CLIP/Climate",model,"historical","vap","vap_mean_hPa_iem_"+model+"_"+mon+"_"+str(year)+".tif"), arcname="vap_mean_hPa_iem_"+model+"_"+mon+"_"+str(year)+".tif", compress_type=compression)
			print 'closing'
			zf.close()
