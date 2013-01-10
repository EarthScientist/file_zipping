from zipfile_infolist import print_info
import zipfile, os, sys

compression = zipfile.ZIP_DEFLATED

os.chdir("/big_storage/malindgren/AIEM/ZIP")

# here lets create a list of the data we want in each of the zip groups
year_groups = [range(2001,2050),range(2050,2101)]
variables = ["rsds"]
months = ["01","02","03","04","05","06","07","08","09","10","11","12"]
models = ["cccma_cgcm3_1","mpi_echam5"]
models2 = ["cccma","echam5"]
scenario = "sresa1b"
metric = "wm-2"
count=0
for model in models:
	print model
	model2 = models2[count]
	count=count+1
	for val in [0,1]:
		filelist=[]
		for v in variables:
			print 'creating archive'
			zf = zipfile.ZipFile(model+"_"+v+"_"+str(year_groups[val][0])+".zip", mode='w', allowZip64=True)
			for year in year_groups[val]:
				for mon in months:
					# filelist.append(os.path.join("/big_storage/malindgren/AIEM/ALFRESCO_AIEM_CLIP/ALFRESCO_Master_Dataset/ALFRESCO_Model_Input_Datasets/AK_CAN_Inputs/Climate",model,"sresa1b","tas","tas_mean_C_iem_ar4_cccma_cgcm3_1_sresa1b_"+mon+"_"+year+".tif"))
					zf.write(os.path.join("/big_storage/malindgren/AIEM/TEM_FINAL_Dec2012/AIEM_MASKED/",v.upper(),model2,model,scenario,v,v+"_mean_"+metric+"_iem_ar4_"+model+"_"+scenario+"_"+mon+"_"+str(year)+".tif"), arcname=v+"_mean_"+metric+"_iem_ar4_"+model+"_"+scenario+"_"+mon+"_"+str(year)+".tif",compress_type=compression)
					
			print 'closing'
			zf.close()
			
