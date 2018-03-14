def get_page(url):
	try:
		import urllib
		import urllib2
		return urllib.urlopen(url).read()
	except Exception, e:
		print "ERROR: %s" % e
		return ""
