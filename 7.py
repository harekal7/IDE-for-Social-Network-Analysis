import snaide

blogs = snaide.get_all_blogs()

coverage = 0

for i in blogs:
	tags_count = len(snaide.get_blog_tags(None, i))
	if coverage < tags_count:
		coverage = tags_count
		blog = i
		
print "Blog with highest domain coverage : "+str(snaide.get_blog_name(blog))