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