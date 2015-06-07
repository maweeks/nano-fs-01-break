import os

def rename_files():
	#get file names
	source = "/Users/MattBP/Documents/Nano-FS/lessons/nano-fs-01-lesson/prank/"
	file_list = os.listdir(r"/Users/MattBP/Documents/Nano-FS/lessons/nano-fs-01-lesson/prank/")
	print(file_list)

	#rename files
	for file_name in file_list:
		os.rename((source+file_name), (source+file_name.translate(None, "0123456789")))

rename_files()