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