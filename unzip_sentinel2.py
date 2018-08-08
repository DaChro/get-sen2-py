# This script unzips the files downloaded by download_sentinel2
# Input parameter is path to the files to unzip
# Files are stored in a subfolder "sentinel2_files"

import zipfile
import os
from sys import argv



def unzip_products(wd):
	# create list of zip files in currentfolder
	zipfiles = [s for s in os.listdir(wd) if ".zip" in s]

	print(str(len(zipfiles))+ ' zipfile(s) found. Unzipping...')

	for file in zipfiles:
		zip_ref = zipfile.ZipFile(os.path.join(wd, file), 'r')
		zip_ref.extractall(os.path.join(wd, 'sentinel2_files'))
		zip_ref.close()

	print('Files unzipped into folder ' + wd + '\sentinel2_files')


if __name__ == "__main__":
	unzip_products(argv[1])
