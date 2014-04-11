#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Return a ward from input using these resources:
# http://citizenatlas.dc.gov/newwebservices/locationverifier.asmx?op=findLocation
# http://octo.dc.gov/node/718362



def findWard():
	import requests
	url="http://citizenatlas.dc.gov/newwebservices/locationverifier.asmx/findLocation?str="
	addy=raw_input("What is you address?")
	r=requests.get(url+addy)
	ward=r.text.split("<WARD>")[1].split("</WARD>")[0]

	print ward

def main():
	findWard()



if __name__ == '__main__':
	main()
