def crawl_web_current(graph, seed):
    tocrawl = [seed]
    crawled = []
    while tocrawl:
        page = tocrawl.pop()
        if page not in crawled:
            union(tocrawl, graph.get(page, []))
            crawled.append(page)
    return crawled
 
def crawl_web_bfs(graph, seed):
    tocrawl = [seed]
    crawled = []
    while tocrawl:
        page = tocrawl.pop(0)
        if page not in crawled:
            union(tocrawl, graph.get(page, []))
            crawled.append(page)
    return crawled
 
print crawl_web_current({1: [2, 3], 3: [4]}, 1) #=>[1, 3, 4, 2]
print crawl_web_bfs({1: [2, 3], 3: [4]}, 1) #=>[1, 2, 3, 4]