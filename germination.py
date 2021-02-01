import pyquery, os, sys, validators, subprocess

def main():
	addtoclient(confirmmagnets(geturl()))

# Gets valid url from user
def geturl():
	url = input("\nCopy and paste a url to scrape magnets from: ").strip()
	while validators.url(url) != True:
		url = input("\nInvalid url. Please enter a valid url i.e. \"https://google.com\": ").strip()
	return url

# Confirms that the provided url contains magnets and appends to confirmed magnet list
def confirmmagnets(url):
	pq = pyquery.PyQuery(url)
	confirmed = list()
	for a in pq.find('a'):
		href = a.get("href")
		if href and (href.startswith("magnet")):
			confirmed.append(href)
	if confirmed == []:
		quit("\nNo magnets found. Exiting...")
	return confirmed

# Adds magnet links to system's default torrent client
def addtoclient(magnets):
	for i in magnets:
		os.system("aria2c --enable-dht=true " + i)

main()
