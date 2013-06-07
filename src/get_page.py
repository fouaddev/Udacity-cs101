
def get_page(url):
	try:
		import urllib
		import urllib2
		return urlib.urlopen(url).read()
	except Exception, e:
		print "ERROR: %s" % e
		return ""