try:
	import urllib.request
	import ssl
	from bs4 import BeautifulSoup
	import re
	import os
	import time
except ImportError as e:
	print(e)


url = "http://mmmut.ac.in/AllNews.aspx"

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

tags = soup('a')
#print(tags)

# for tag in tags:
# 	print(tag.get('href'), None)


newPdfs = re.findall(r"(\d+notice_\d+\.pdf|\d+news_\d+\.pdf)", str(tags))
# print(*newPdfs, sep="\n")
newPdfs = list(set(newPdfs))


currentDirectory = str(time.strftime("%H-%M-%S%p  %a %d-%b-%Y"))




# print([name for name in os.listdir(".") if os.path.isdir(name)])
latestDir =max([name for name in os.listdir(".") if os.path.isdir(name)])
# print(latestDir)

alreadyExistFiles = [name for name in os.listdir(latestDir)]
print(len(newPdfs), len(alreadyExistFiles))


i=0
for pdf in newPdfs:
	if pdf not in alreadyExistFiles:
		print("\n[*] Downloading: {}".format(pdf))
		newFilePath = ".\\"+currentDirectory+"\\"+pdf
		print(newFilePath)
		f = open(newFilePath, "wb")
		fileUrl = "http://mmmut.ac.in/News_content/"+pdf
		print("fileurl",fileUrl)
		#f.write(pdf.read())
		f.close()
		i += 1
	else:
		print(pdf, " Already downloaded")

# print(newPdfs, len(newPdfs))


print(i, " files downloaded")

# for file in newPdfs:
# 	open("10-44-46AM  Sun 19-May-2019\\"+os.path.basename(file), "wb")