import _snaide

#***********************************************************************************************************************

graph_db = _snaide._init("http://localhost:7474/db/data/")

#***********************************************************************************************************************

def get_all_users():
	global graph_db
	return _snaide._get_all_users(graph_db)

#***********************************************************************************************************************

def get_one_user(user_name, user_guid):
	global graph_db
	return _snaide._get_one_user(graph_db, user_name, user_guid)

#***********************************************************************************************************************

def get_all_events():
	global graph_db
	return _snaide._get_all_events(graph_db)

#***********************************************************************************************************************

def get_events_owned_by(user_name, user_guid):
	global graph_db
	return _snaide._get_events_owned_by(graph_db,user_name, user_guid)

#***********************************************************************************************************************

def get_one_event (event_name, event_guid):
	global graph_db
	return _snaide._get_one_event (graph_db, event_name, event_guid)
	
#***********************************************************************************************************************

def get_statuses_by(user_name, user_guid):
	global graph_db
	return _snaide._get_statuses_by(graph_db, user_name, user_guid)

#***********************************************************************************************************************

def get_comments_by(user_name, user_guid):
	global graph_db
	return _snaide._get_comments_by(graph_db, user_name, user_guid)

#***********************************************************************************************************************

def get_group_members(group_name, group_guid):
 	global graph_db
 	return _snaide._get_group_members(graph_db, group_name, group_guid)

#***********************************************************************************************************************

def get_groups_owned_by (user_name, user_guid):
	global graph_db
	return _snaide._get_groups_owned_by (graph_db, user_name, user_guid)

#***********************************************************************************************************************

def get_all_pages():
	global graph_db
	return _snaide._get_all_pages(graph_db)

#***********************************************************************************************************************

def get_all_events():
	global graph_db
	return _snaide._get_all_events(graph_db)

#***********************************************************************************************************************
def get_events_created_by(user_name, user_guid):
	global graph_db
	return _snaide._get_events_created_by(graph_db, user_name, user_guid)

#***********************************************************************************************************************

def get_event_attendees (event_name, event_guid):
	global graph_db
	return _snaide._get_event_attendees(graph_db, event_name, event_guid)

#***********************************************************************************************************************

def get_event_info (event_name, event_guid):
	global graph_db
	return _snaide._get_event_info(graph_db, event_name, event_guid)
	

#***********************************************************************************************************************

def get_event_organizer (event_name, event_guid):
	global graph_db
	return _snaide._get_event_organizer(graph_db, event_name, event_guid)
	

#***********************************************************************************************************************

def get_event_date (event_name, event_guid):
	global graph_db
	return _snaide._get_event_date(graph_db, event_name, event_guid)
	
#***********************************************************************************************************************

def get_event_start_time (event_name, event_guid):
	global graph_db
	return _snaide._get_event_start_time(graph_db, event_name, event_guid)
	

#***********************************************************************************************************************

def get_event_title (event_guid):
	global graph_db
	return _snaide._get_event_title(graph_db, event_guid)

#***********************************************************************************************************************

def get_event_attendees_count(event_name, event_guid):
	global graph_db
	return _snaide._get_event_attendees_count(graph_db, event_name, event_guid)
	
#***********************************************************************************************************************

def get_event_short_description(event_name, event_guid):
	global graph_db
	return _snaide._get_event_short_description(graph_db, event_name, event_guid)

#***********************************************************************************************************************

def get_event_description(event_name, event_guid):
	global graph_db
	return _snaide._get_event_description(graph_db, event_name, event_guid)


#***********************************************************************************************************************

def get_event_max_attendees(event_name, event_guid):
	global graph_db
	return _snaide._get_event_max_attendees(graph_db, event_name, event_guid)	

#***********************************************************************************************************************

def get_event_end_registration_day(event_name, event_guid):
	global graph_db
	return _snaide._get_event_end_registration_day(graph_db, event_name, event_guid)
	
#***********************************************************************************************************************

def get_event_fee(event_name, event_guid):
	global graph_db
	return _snaide._get_event_fee(graph_db, event_name, event_guid)

#***********************************************************************************************************************

def get_event_contact_details(event_name, event_guid):
	global graph_db
	return _snaide._get_event_contact_details(graph_db, event_name, event_guid)
	
#***********************************************************************************************************************

def get_event_venue(event_name, event_guid):
	global graph_db
	return _snaide._get_event_venue(graph_db, event_name, event_guid)

#***********************************************************************************************************************

def get_event_location(event_name, event_guid):
	global graph_db
	return _snaide._get_event_location(graph_db, event_name, event_guid)

#***********************************************************************************************************************

def get_event_website(event_name, event_guid):
	global graph_db
	return _snaide._get_event_website(graph_db, event_name, event_guid)

#***********************************************************************************************************************

def get_event_twitter_hash(event_name, event_guid):
	global graph_db
	return _snaide._get_event_twitter_hash(graph_db, event_name, event_guid)

#***********************************************************************************************************************

def get_event_location(event_name, event_guid):
	global graph_db
	return _snaide._get_event_location(graph_db, event_name, event_guid)

#***********************************************************************************************************************

def get_event_tags(event_name, event_guid):
	global graph_db
	return _snaide._get_event_tags(graph_db, event_name, event_guid)

#***********************************************************************************************************************
def get_all_pages():
	global graph_db
	return _snaide._get_all_pages(graph_db)

#***********************************************************************************************************************
def get_page_likes_count (page_name, page_guid):
	global graph_db
	return _snaide._get_page_likes_count(graph_db, page_name, page_guid)

#***********************************************************************************************************************
def get_pages_created_by (user_name, user_guid):
	global graph_db
	return _snaide._get_pages_created_by(graph_db, user_name, user_guid)
#***********************************************************************************************************************

def get_pages_liked_by (user_name, user_guid):
	global graph_db
	return _snaide._get_pages_liked_by(graph_db, user_name, user_guid)
#***********************************************************************************************************************

def get_page_title (page_guid):
	global graph_db
	return _snaide._get_page_title(graph_db, page_guid)

#***********************************************************************************************************************

def get_page_created_date (page_name, page_guid):
	global graph_db
	return _snaide._get_page_created_date(graph_db, page_name, page_guid)

#***********************************************************************************************************************

def get_page_content(page_name, page_guid):
	global graph_db
	return _snaide._get_page_content(graph_db, page_name, page_guid)

#***********************************************************************************************************************

def get_page_tags(page_name, page_guid):
	global graph_db
	return _snaide._get_page_tags(graph_db, page_name, page_guid)

#***********************************************************************************************************************

def get_page_container_group(page_name, page_guid):
	global graph_db
	return _snaide._get_page_container_group(graph_db, page_name, page_guid)

#***********************************************************************************************************************

def get_group_members(group_name, group_guid):
	global graph_db
	return _snaide._get_group_members(graph_db, group_name, group_guid) 	

#***********************************************************************************************************************
def get_group_members_count(group_name, group_guid):
	global graph_db
	return _snaide._get_group_members_count(graph_db, group_name, group_guid)

#***********************************************************************************************************************

def get_groups_owned_by (user_name, user_guid):
	global graph_db
	return _snaide._get_groups_owned_by(graph_db, user_name, user_guid)

#***********************************************************************************************************************

def get_group_owner (group_name, group_guid):
	global graph_db
	return _snaide._get_group_owner(graph_db, group_name, group_guid)
	
#***********************************************************************************************************************

def get_group_name(group_guid):
	global graph_db
	return _snaide._get_group_name(graph_db, group_guid)

#***********************************************************************************************************************

def get_group_description(group_name, group_guid):
	global graph_db
	return _snaide._get_group_description(graph_db, group_name, group_guid)
	
#***********************************************************************************************************************

def get_group_brief_description(group_name, group_guid):
	global graph_db
	return _snaide._get_group_brief_description(graph_db, group_name, group_guid)

#***********************************************************************************************************************

def is_events_enabled_in_group(group_name, group_guid):
	global graph_db
	return _snaide._is_events_enabled_in_group(graph_db, group_name, group_guid)

#***********************************************************************************************************************

def is_blogs_enabled_in_group(group_name, group_guid):
	global graph_db
	return _snaide._is_blogs_enabled_in_group(graph_db, group_name, group_guid)

#***********************************************************************************************************************

def is_pages_enabled_in_group(group_name, group_guid):
	global graph_db
	return _snaide._is_pages_enabled_in_group(graph_db, group_name, group_guid)

#***********************************************************************************************************************

def get_blog_likers (blog_name, blog_guid):
	global graph_db
	return _snaide._get_blog_likers(graph_db, blog_name, blog_guid)

#***********************************************************************************************************************

def get_blog_commentators (blog_name, blog_guid):
	global graph_db
	return _snaide._get_blog_commentators(graph_db, blog_name, blog_guid)	

#***********************************************************************************************************************

def get_blog_name (blog_guid):
	global graph_db
	return _snaide._get_blog_name(graph_db, blog_guid)		
	

#***********************************************************************************************************************

def get_blog_description(blog_name, blog_guid):
	global graph_db
	return _snaide._get_blog_description(graph_db, blog_name, blog_guid)		
	
#***********************************************************************************************************************

def get_blog_tags(blog_name, blog_guid):
	global graph_db
	return _snaide._get_blog_tags(graph_db, blog_name, blog_guid)		
	

#***********************************************************************************************************************

def get_blog_created_time(blog_name, blog_guid):
	global graph_db
	return _snaide._get_blog_created_time(graph_db, blog_name, blog_guid)		
	
#***********************************************************************************************************************


def get_blogs_by_user (user_name, user_guid):
	global graph_db
	return _snaide._get_blogs_by_user(graph_db, user_name, user_guid)		

#***********************************************************************************************************************

def get_blog_likers_count (blog_name, blog_guid):
	global graph_db
	return _snaide._get_blog_likers_count(graph_db, blog_name, blog_guid)		

#***********************************************************************************************************************

def get_blog_commentator_count (blog_name, blog_guid):
	global graph_db
	return _snaide._get_blog_commentator_count(graph_db, blog_name, blog_guid)		

#***********************************************************************************************************************