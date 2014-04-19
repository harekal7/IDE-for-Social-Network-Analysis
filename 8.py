import snaide

pages = snaide.get_all_pages()

coverage = 0

for i in pages:
	tags_count = len(snaide.get_page_tags(None, i["guid"]))
	if coverage < tags_count:
		coverage = tags_count
		page = i["guid"]
		
print "Page with highest domain coverage : "+str(snaide.get_page_title(page))