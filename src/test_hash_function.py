# Lesson 5
def get_page(url):
    try:
        import urllib
        import urllib2
        return urllib.urlopen(url).read()
    except Exception, e:
        print "ERROR: %s" % e
        return ""
def hash_string(keyword,buckets):
    total_ord = 0;
    for c in keyword:
        total_ord = total_ord + ord(c)
    return total_ord % buckets

    
def test_hash_function(func,keys,size):
    results = [0] * size
    keys_used = []
    for w in keys:
        if w not in keys_used:
            hv = func(w,size)
            results[hv] += 1
            keys_used.append(w)
    return results

def hashtable_get_bucket(table, keyword):
    return hash_string
    

words = get_page('http://www.gutenberg.org/cache/epub/1661/pg1661.txt').split()
print "Analyzing buckets, may take a while..."
counts = test_hash_function(hash_string,words,100)
print counts