import snaide

v1 = snaide.get_all_users_count()
v2 = snaide.get_all_statuses_count()
v3 = snaide.get_all_comments_count()
v4 = snaide.get_all_status_likes_count()
v5 = snaide.get_all_events_count()
v6 = snaide.get_all_pages_count()
v7 = snaide.get_all_blogs_count()
v8 = snaide.get_all_groups_count()


#print "total number of users : "+ str(v1)
print "average no of status per user posted : " + str(float(v2)/v1)
print "average no of comments per each status : " + str(v3/float(v2))
print "average likes for each status : " + str(v4/float(v2)) 
print "total no of events organized : " + str(v5) 
print "total no of blogs created : " + str(v7) 