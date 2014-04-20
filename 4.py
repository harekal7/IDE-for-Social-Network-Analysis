import snaide

friends_count = snaide.get_all_friends_count(None, 48150)

friends = snaide.get_all_friends(None, 48150)

pages_sum = 0
comments_sum = 0
statuses_count = 0
status_likes_count = 0
blogs_count = 0
blog_likes_count = 0
groups_count = 0
groups = set([])

for friend in friends:
	pages_sum = pages_sum + len(snaide.get_pages_liked_by(None, friend))
	comments_sum = comments_sum + len(snaide.get_comments_by(None, friend))
	statuses = snaide.get_statuses_by(None, friend)
	statuses_count = statuses_count + len(statuses)
	for status_id in statuses:
		status_likes_count = status_likes_count + snaide.get_likes_on_single_status(status_id)

	blogs = snaide.get_blogs_by_user(None, friend)
	blogs_count = blogs_count + len(blogs)
	for blog_id in blogs:
		blog_likes_count = blog_likes_count + snaide.get_blog_likers_count(None, blog_id)

	for g in snaide.groups_with_user_as_member(None, friend):
		groups.add ( g )
	
groups_count = groups_count + len(groups)

print "Average Pages Liked by Friends : "+str(pages_sum/friends_count)
print "Average Comments by Friends : "+str(comments_sum/friends_count)
print "Average Statuses posted by Friends : "+str(statuses_count/friends_count)
print "Average Likes on Statuses by Friends : "+str(status_likes_count/friends_count)
print "Average Blogs by Friends : "+str(blogs_count/friends_count)
print "Average Blogs Liked by Friends : "+str(blog_likes_count/friends_count)
print "Total Groups involved by Friends : "+str(groups_count)