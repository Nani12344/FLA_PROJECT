# This Python file uses the following encoding: utf-8
import re
import sys

infile = open(sys.argv[1], 'r') #輸入的檔案名
rank = int(sys.argv[2]) #最小的個數
a = 0
allmap ={}

for line in infile: #一行一行讀檔
	url = re.findall('"WARC-Target-URI":+\"([^"]*)\"', line) #抓"WARC-Target-URI"
	str_url = ''.join(url) #把list轉成str
	
	links = re.findall('"Links":+((?=\[)\[[^]]*\]|(?=\{)\{[^\}]*\}|\"[^"]*\")', line) #抓"Links"裡的東西
	str_tmp = ''.join(links) #把list轉成str

	href = re.findall('"href":+\"[^"]*\"', str_tmp) #抓"herf:"後面的東西
	num_href = len(href) #直接算list裡面有幾個東西就可以了

	url = re.findall('"url":+\"[^"]*\"', str_tmp) #抓"url:"後面的東西
	num_url = len(url) #直接算list裡面有幾個東西就可以了

	total = num_href + num_url #總合

		
	allmap[str_url]=total  


count=0 
for key,value in sorted(allmap.iteritems(), key=lambda x:x[1], reverse = True):
	if count < rank:
		print '%s : %d' % (key, allmap[key])
		temp=allmap[key]
		count +=1
	elif count==rank and allmap[key]==temp:
		temp=allmap[key]
		print '%s : %d' % (key,allmap[key])
	else:
		break
	
