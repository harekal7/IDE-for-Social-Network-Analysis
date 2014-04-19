from py2neo import neo4j
from py2neo import cypher 
import time

#***********************************************************************************************************************


'''
Initialises graph db handler
and returns it to the caller
'''

def _init(_url):
	graph_db = neo4j.GraphDatabaseService(_url)
	return graph_db

#***********************************************************************************************************************

'''
fetches all the users of the social network
and returns it in the form of a list of key-value pairs to the caller
'''

def _get_all_users(graph_db):
	query = "MATCH (n:User) RETURN n"
	data, metadata = cypher.execute(graph_db, query)
	ret = []
	for row in data:
		ret.append( {"guid" : row[0]["guid"], 
								 "name" : str(row[0]["name"])} 
							);
	return ret

#***********************************************************************************************************************

def _get_one_user(graph_db, user_name, user_guid):
	if user_name != None and user_guid != None :
		query = "MATCH (n:User) WHERE n.name = "+"'"+str(user_name)+"' and n.guid = "+str(user_guid)+"  RETURN n"
	elif user_name == None:
		query = "MATCH (n:User) WHERE n.guid = "+str(user_guid)+" RETURN n"
	else:
		query = "MATCH (n:User) WHERE n.name = "+"'"+str(user_name)+"'"+" RETURN n"
	data, metadata = cypher.execute(graph_db, query)
	if data:
		for row in data:
			ret = ( {"guid" : row[0]["guid"], "name" : str(row[0]["name"])} );
	else:
		ret = "\n<br \>User not found.<br \>\n"

	return ret

#***********************************************************************************************************************

def _get_all_events(graph_db):
	query = "MATCH (n:Event) RETURN n"
	data, metadata = cypher.execute(graph_db, query)
	ret = []
	for row in data:
		ret.append({"guid" : row[0]["guid"], "name" : str(row[0]["name"])} )

	return ret

#***********************************************************************************************************************
def _get_events_owned_by(graph_db,user_name, user_guid):
	if user_name != None and user_guid != None :
		query = "MATCH (n:Event)-[:Owner_event]-> (m:User) WHERE m.guid = "+str(user_guid)+" and m.name = "+"'"+str(user_name)+"' RETURN n"
	elif user_name == None:
		query = "MATCH (n:Event)-[:Owner_event]-> (m:User) WHERE m.guid = "+str(user_guid)+" RETURN n"
	else:
		query = "MATCH (n:Event)-[:Owner_event]-> (m:User) WHERE m.name = "+"'"+str(user_name)+"'"+" RETURN n"
	data, metadata = cypher.execute(graph_db, query)
	
	if data:
		ret = []
		for row in data:
			ret.append( {"id" : row[0]["guid"], "name" : str(row[0]["name"])} )
	else:
		ret = "No Events"
	return ret

#***********************************************************************************************************************

def _get_one_event (graph_db,event_name, event_guid):
	# get all the users attending the event
	# get the time of event
	if event_name != None and event_guid != None :
		query = "MATCH (m:User)-[:Attends]-> (n:Event) WHERE n.guid = "+str(event_guid)+" and n.name = "+"'"+str(event_name)+"' RETURN m"
	elif event_name == None:
		query = "MATCH (m:User)-[:Attends]-> (n:Event) WHERE n.guid = "+str(event_guid)+"  RETURN m"
	else:
		query = "MATCH (m:User)-[:Attends]-> (n:Event) WHERE n.name = "+"'"+str(event_name)+"'"+" RETURN m"
	data, metadata = cypher.execute(graph_db, query)
	if data:
		for row in data:
			ret = {"id" : row[0]["guid"], "name" : str(row[0]["name"]) }
	else:
		ret = "User Not Found"
	return ret

#***********************************************************************************************************************

def _get_statuses_by(graph_db,user_name, user_guid):
	if user_name != None and user_guid != None :
		query = "MATCH (n:User)-[:Posted]-> (m:Status) WHERE n.guid = "+str(user_guid)+" and n.name = "+"'"+str(user_name)+"' RETURN m"
	elif user_name == None:
		query = "MATCH (n:User)-[:Posted]-> (m:Status) WHERE n.guid = "+str(user_guid)+" RETURN m"
	else:
		query = "MATCH (n:User)-[:Posted]-> (m:Status) WHERE n.name = "+"'"+str(user_name)+"'"+" RETURN m"
	data, metadata = cypher.execute(graph_db, query)
	ret = []
	if data:
		for row in data:
			ret.append({"status_id" : row[0]["status_id"], "message" : str(row[0]["message"]) })

	return ret

#***********************************************************************************************************************

def _get_comments_by(graph_db, user_name, user_guid):
	if user_name != None and user_guid != None :
		query = "MATCH (n:User)-[:comments]-> (m:Comment) WHERE n.guid = "+str(user_guid)+" and n.name = "+"'"+str(user_name)+"' RETURN m"
	elif user_name == None:
		query = "MATCH (n:User)-[:comments]-> (m:Comment) WHERE n.guid = "+str(user_guid)+" RETURN m"
	else:
		query = "MATCH (n:User)-[:comments]-> (m:Comment) WHERE n.name = "+"'"+str(user_name)+"'"+" RETURN m"
	data, metadata = cypher.execute(graph_db, query)
	ret = []
	if data:
		for row in data:
			ret.append({"id" : row[0]["comment_id"], "message" : str(row[0]["message"]) })
	return ret

#***********************************************************************************************************************

def _get_group_members(graph_db, group_name, group_guid):
 	if group_name != None and group_guid != None :
		query = "MATCH (n:User)-[:is_member]-> (m:Group) WHERE m.group_id = "+str(group_guid)+" and m.name = "+"'"+str(group_name)+"' RETURN n"
	elif group_name == None:
		query = "MATCH (n:User)-[:is_member]-> (m:Group) WHERE m.group_id = "+str(group_guid)+" RETURN n"
	else:
		query = "MATCH (n:User)-[:is_member]-> (m:Group) WHERE m.name = "+"'"+str(group_name)+"'"+" RETURN n"
	data, metadata = cypher.execute(graph_db, query)
	ret = []
	if data:
		for row in data:
			ret.append({"id" : row[0]["guid"], "name" : str(row[0]["name"]) })

	return ret

#***********************************************************************************************************************

def _get_groups_owned_by (graph_db, user_name, user_guid):
	if user_name != None and user_guid != None :
		query = "MATCH (n:User)-[:Owns]-> (m:Group) WHERE n.guid = "+str(user_guid)+" and n.name = "+"'"+str(user_name)+"' RETURN m"
	elif user_name == None:
		query = "MATCH (n:User)-[:Owns]-> (m:Group) WHERE n.guid = "+str(user_guid)+" RETURN m"
	else:
		query = "MATCH (n:User)-[:Owns]-> (m:Group) WHERE n.name = "+"'"+str(user_name)+"'"+" RETURN m"
	data, metadata = cypher.execute(graph_db, query)
	ret = []
	if data:
		for row in data:
			ret.append({"id" : row[0]["group_id"], "name" : str(row[0]["name"]) }	)		

	return ret

#***********************************************************************************************************************

def _get_all_pages(graph_db):
	query = "MATCH (n:Page) RETURN n"
	data, metadata = cypher.execute(graph_db, query)
	ret = []
	if data:
		for row in data:
			ret.append( {"guid" : row[0]["guid"], "name" : str(row[0]["name"]) } )

	return ret

#***********************************************************************************************************************

def _get_all_events(graph_db):
	query = "MATCH (n:Event) RETURN n"
	data, metadata = cypher.execute(graph_db, query)
	if data:
		ret = []
		for row in data:
			ret.append({"id":row[0]["guid"]})
	else:
		ret = "No Events"
	
	return ret
	
#***********************************************************************************************************************
def _get_events_created_by(graph_db,user_name, user_guid):
	if user_name != None and user_guid != None :
		query = "MATCH (n:Event)-[:Owner_event]-> (m:User) WHERE m.guid = "+str(user_guid)+" and m.name = "+"'"+str(user_name)+"' RETURN n"
	elif user_name == None:
		query = "MATCH (n:Event)-[:Owner_event]-> (m:User) WHERE m.guid = "+str(user_guid)+" RETURN n"
	else:
		query = "MATCH (n:Event)-[:Owner_event]-> (m:User) WHERE m.name = "+"'"+str(user_name)+"'"+" RETURN n"
	data, metadata = cypher.execute(graph_db, query)
	if data:
		ret = []
		for row in data:
			ret.append({"name":row[0]["title"], "id":row[0]["guid"]})
	else:
		ret =  "\nEvent not found.\n"

	return ret

#***********************************************************************************************************************

def _get_event_attendees (graph_db, event_name, event_guid):
	# get all the users attending the event
	
	if event_name != None and event_guid != None :
		query = "MATCH (m:User)-[:Attends]-> (n:Event) WHERE n.guid = "+str(event_guid)+" and n.title = "+"'"+str(event_name)+"' RETURN m"
	elif event_name == None:
		query = "MATCH (m:User)-[:Attends]-> (n:Event) WHERE n.guid = "+str(event_guid)+"  RETURN m"
	else:
		query = "MATCH (m:User)-[:Attends]-> (n:Event) WHERE n.title = "+"'"+str(event_name)+"'"+" RETURN m"
	data, metadata = cypher.execute(graph_db, query)
	if data:
		ret = []
		for row in data:
			ret.append({"user_name":row[0]["name"], "user_id":row[0]["guid"]})
	else:
		ret =  "\nEvent not found.\n"

	return ret

#***********************************************************************************************************************

def _get_event_info (graph_db,event_name, event_guid):
	# returns the info regarding the events.
	pass

#***********************************************************************************************************************

def _get_event_organizer (graph_db,event_name, event_guid):
	# returns the info regarding the organizers of events.
	
	if event_name != None and event_guid != None :
		query = "MATCH (n:Event) WHERE n.guid = "+str(event_guid)+" and n.title = "+"'"+str(event_name)+"' RETURN n"
	elif event_name == None:
		query = "MATCH (n:Event) WHERE n.guid = "+str(event_guid)+" RETURN n"
	else:
		query = "MATCH (n:Event) WHERE n.title = "+"'"+str(event_name)+"'"+" RETURN n"
	data, metadata = cypher.execute(graph_db, query)
	if data:
		for row in data:
			ret = {"organizer": row[0]["organizer"] }
	else:
		ret = "\nEvent not found.\n"

	return ret

#***********************************************************************************************************************

def _get_event_date (graph_db,event_name, event_guid):
	# returns the date of events.
	
	if event_name != None and event_guid != None :
		query = "MATCH (n:Event) WHERE n.guid = "+str(event_guid)+" and n.title = "+"'"+str(event_name)+"' RETURN n"
	elif event_name == None:
		query = "MATCH (n:Event) WHERE n.guid = "+str(event_guid)+" RETURN n"
	else:
		query = "MATCH (n:Event) WHERE n.title = "+"'"+str(event_name)+"'"+" RETURN n"
	data, metadata = cypher.execute(graph_db, query)
	if data:
		for row in data:
			ret =  { "Date" : time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(row[0]["created_time"])) }
	else:
		ret =  "\nEvent not found.\n"

	return ret

#***********************************************************************************************************************

def _get_event_start_time (graph_db,event_name, event_guid):
	# returns the info regarding the start time of events.
	
	if event_name != None and event_guid != None :
		query = "MATCH (n:Event) WHERE n.guid = "+str(event_guid)+" and n.title = "+"'"+str(event_name)+"' RETURN n"
	elif event_name == None:
		query = "MATCH (n:Event) WHERE n.guid = "+str(event_guid)+" RETURN n"
	else:
		query = "MATCH (n:Event) WHERE n.title = "+"'"+str(event_name)+"'"+" RETURN n"
	data, metadata = cypher.execute(graph_db, query)
	if data:
		for row in data:
			print "\nDate : "+str(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(row[0]["start_time"])))
		print
	else:
		print "\nEvent not found.\n"

#***********************************************************************************************************************

def _get_event_title (graph_db, event_guid):
	# returns the info regarding the organizers of events.
	
	if event_guid != None :
		query = "MATCH (n:Event) WHERE n.guid = "+str(event_guid)+"  RETURN n"
	data, metadata = cypher.execute(graph_db, query)
	if data:
		for row in data:
			ret = {"event_title" : row[0]["title"] }
	else:
		ret =  "\nEvent not found.\n"

#***********************************************************************************************************************

def _get_event_attendees_count(graph_db, event_name, event_guid):
	# returns the # of users attending the event
	
	if event_name != None and event_guid != None :
		query = "MATCH (m:User)-[:Attends]-> (n:Event) WHERE n.guid = "+str(event_guid)+" and n.title = "+"'"+str(event_name)+"' RETURN m"
	elif event_name == None:
		query = "MATCH (m:User)-[:Attends]-> (n:Event) WHERE n.guid = "+str(event_guid)+"  RETURN m"
	else:
		query = "MATCH (m:User)-[:Attends]-> (n:Event) WHERE n.title = "+"'"+str(event_name)+"'"+" RETURN m"
	data, metadata = cypher.execute(graph_db, query)
	if data:
		return len(data)
	else:
		return "\nEvent not found.\n"

#***********************************************************************************************************************

def _get_event_short_description(graph_db, event_name, event_guid):
	# returns the brief description about the event
	if event_name != None and event_guid != None :
		query = "MATCH (n:Event) WHERE n.event_id = "+str(event_guid)+" and n.title = "+"'"+str(event_name)+"' RETURN n"
	elif event_name == None:
		query = "MATCH (n:Event) WHERE n.event_id = "+str(event_guid)+"  RETURN n"
	else:
		query = "MATCH (n:Event) WHERE n.title = "+"'"+str(event_name)+"'"+" RETURN n"
	data, metadata = cypher.execute(graph_db, query)
	if data:
		for row in data:
			ret = {"event_short_description" : row[0]["short_desc"] }
	else:
		ret =  "\n No short description available.\n"

	return ret

#***********************************************************************************************************************

def _get_event_description(graph_db, event_name, event_guid):
	# returns the brief description about the event
	if event_name != None and event_guid != None :
		query = "MATCH (n:Event) WHERE n.event_id = "+str(event_guid)+" and n.title = "+"'"+str(event_name)+"' RETURN n"
	elif event_name == None:
		query = "MATCH (n:Event) WHERE n.event_id = "+str(event_guid)+"  RETURN n"
	else:
		query = "MATCH (n:Event) WHERE n.title = "+"'"+str(event_name)+"'"+" RETURN n"
	data, metadata = cypher.execute(graph_db, query)
	if data:
		for row in data:
			ret =  { "event_description": row[0]["description"] }
	else:
		ret =  "\n No description available.\n"

	return ret

#***********************************************************************************************************************

def _get_event_max_attendees(graph_db, event_name, event_guid):
	# returns the brief description about the event
	if event_name != None and event_guid != None :
		query = "MATCH (n:Event) WHERE n.event_id = "+str(event_guid)+" and n.title = "+"'"+str(event_name)+"' RETURN n"
	elif event_name == None:
		query = "MATCH (n:Event) WHERE n.event_id = "+str(event_guid)+"  RETURN n"
	else:
		query = "MATCH (n:Event) WHERE n.title = "+"'"+str(event_name)+"'"+" RETURN n"
	data, metadata = cypher.execute(graph_db, query)
	if data:
		for row in data:
			ret =  { "event_attendees" : row[0]["max_attendees"] }
	else:
		ret =  "\n No Event available.\n"

	return ret

#***********************************************************************************************************************

def _get_event_end_registration_day(graph_db, event_name, event_guid):
	# returns the brief description about the event
	if event_name != None and event_guid != None :
		query = "MATCH (n:Event) WHERE n.event_id = "+str(event_guid)+" and n.title = "+"'"+str(event_name)+"' RETURN n"
	elif event_name == None:
		query = "MATCH (n:Event) WHERE n.event_id = "+str(event_guid)+"  RETURN n"
	else:
		query = "MATCH (n:Event) WHERE n.title = "+"'"+str(event_name)+"'"+" RETURN n"
	data, metadata = cypher.execute(graph_db, query)
	if data:
		for row in data:
			ret =  { "event_end_registration_date" : time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(row[0]["end_registration_day"])) }
	else:
		ret =  "\n No Event/end registration day available.\n"

	return ret

#***********************************************************************************************************************

def _get_event_fee(graph_db, event_name, event_guid):
	# returns the brief description about the event
	if event_name != None and event_guid != None :
		query = "MATCH (n:Event) WHERE n.event_id = "+str(event_guid)+" and n.title = "+"'"+str(event_name)+"' RETURN n"
	elif event_name == None:
		query = "MATCH (n:Event) WHERE n.event_id = "+str(event_guid)+"  RETURN n"
	else:
		query = "MATCH (n:Event) WHERE n.title = "+"'"+str(event_name)+"'"+" RETURN n"
	data, metadata = cypher.execute(graph_db, query)
	if data:
		for row in data:
			ret =  { "event_fee" : row[0]["fee"] }
		print
	else:
		ret =  "\n No Event/Event fee available.\n"

	return ret

#***********************************************************************************************************************

def _get_event_contact_details(graph_db, event_name, event_guid):
	# returns the brief description about the event
	if event_name != None and event_guid != None :
		query = "MATCH (n:Event) WHERE n.event_id = "+str(event_guid)+" and n.title = "+"'"+str(event_name)+"' RETURN n"
	elif event_name == None:
		query = "MATCH (n:Event) WHERE n.event_id = "+str(event_guid)+"  RETURN n"
	else:
		query = "MATCH (n:Event) WHERE n.title = "+"'"+str(event_name)+"'"+" RETURN n"
	data, metadata = cypher.execute(graph_db, query)
	if data:
		for row in data:
			ret =  {"event_contact_details" : row[0]["contact_details"] }
	else:
		ret =  "\n No Event/contact details available.\n"


	return ret

#***********************************************************************************************************************

def _get_event_venue(graph_db, event_name, event_guid):
	# returns the brief description about the event
	if event_name != None and event_guid != None :
		query = "MATCH (n:Event) WHERE n.event_id = "+str(event_guid)+" and n.title = "+"'"+str(event_name)+"' RETURN n"
	elif event_name == None:
		query = "MATCH (n:Event) WHERE n.event_id = "+str(event_guid)+"  RETURN n"
	else:
		query = "MATCH (n:Event) WHERE n.title = "+"'"+str(event_name)+"'"+" RETURN n"
	data, metadata = cypher.execute(graph_db, query)
	if data:
		for row in data:
			ret =  "event_venue" : row[0]["venue"] }
	else:
		ret =  "\n No Event/venue available.\n"

	return ret

#***********************************************************************************************************************

def _get_event_location(graph_db, event_name, event_guid):
	# returns the brief description about the event
	if event_name != None and event_guid != None :
		query = "MATCH (n:Event) WHERE n.event_id = "+str(event_guid)+" and n.title = "+"'"+str(event_name)+"' RETURN n"
	elif event_name == None:
		query = "MATCH (n:Event) WHERE n.event_id = "+str(event_guid)+"  RETURN n"
	else:
		query = "MATCH (n:Event) WHERE n.title = "+"'"+str(event_name)+"'"+" RETURN n"
	data, metadata = cypher.execute(graph_db, query)
	if data:
		for row in data:
			ret =  {"event_location" : row[0]["location"] }
	else:
		ret = "\n No Event/location available.\n"

	return ret

#***********************************************************************************************************************

def _get_event_website(graph_db, event_name, event_guid):
	# returns the brief description about the event
	if event_name != None and event_guid != None :
		query = "MATCH (n:Event) WHERE n.event_id = "+str(event_guid)+" and n.title = "+"'"+str(event_name)+"' RETURN n"
	elif event_name == None:
		query = "MATCH (n:Event) WHERE n.event_id = "+str(event_guid)+"  RETURN n"
	else:
		query = "MATCH (n:Event) WHERE n.title = "+"'"+str(event_name)+"'"+" RETURN n"
	data, metadata = cypher.execute(graph_db, query)
	if data:
		for row in data:
			ret =  "event_website" : row[0]["website"] }
	else:
		ret = "\n No Event/website available.\n"

	return ret

#***********************************************************************************************************************

def _get_event_twitter_hash(graph_db, event_name, event_guid):
	# returns the brief description about the event
	if event_name != None and event_guid != None :
		query = "MATCH (n:Event) WHERE n.event_id = "+str(event_guid)+" and n.title = "+"'"+str(event_name)+"' RETURN n"
	elif event_name == None:
		query = "MATCH (n:Event) WHERE n.event_id = "+str(event_guid)+"  RETURN n"
	else:
		query = "MATCH (n:Event) WHERE n.title = "+"'"+str(event_name)+"'"+" RETURN n"
	data, metadata = cypher.execute(graph_db, query)
	if data:
		for row in data:
			ret =  "event_twitter_hash" : row[0]["twitter_hash"] }
	else:
		ret =  "\n No Event/twitter hash available.\n"

	return ret

#***********************************************************************************************************************

def _get_event_location(graph_db, event_name, event_guid):
	# returns the brief description about the event
	if event_name != None and event_guid != None :
		query = "MATCH (n:Event) WHERE n.event_id = "+str(event_guid)+" and n.title = "+"'"+str(event_name)+"' RETURN n"
	elif event_name == None:
		query = "MATCH (n:Event) WHERE n.event_id = "+str(event_guid)+"  RETURN n"
	else:
		query = "MATCH (n:Event) WHERE n.title = "+"'"+str(event_name)+"'"+" RETURN n"
	data, metadata = cypher.execute(graph_db, query)
	if data:
		for row in data:
			ret =  {"event_location" : row[0]["location"] }
	else:
		ret =  "\n No Event/location available.\n"

	return ret

#***********************************************************************************************************************

def _get_event_tags(graph_db, event_name, event_guid):
	# returns the brief description about the event
	if event_name != None and event_guid != None :
		query = "MATCH (n:Event) WHERE n.event_id = "+str(event_guid)+" and n.title = "+"'"+str(event_name)+"' RETURN n"
	elif event_name == None:
		query = "MATCH (n:Event) WHERE n.event_id = "+str(event_guid)+"  RETURN n"
	else:
		query = "MATCH (n:Event) WHERE n.title = "+"'"+str(event_name)+"'"+" RETURN n"
	data, metadata = cypher.execute(graph_db, query)
	if data:
		ret = []
		for row in data:
			#for tag in row[0]["tags"]:
			ret =  row[0]["tags"]
	else:
		ret =  "\nTags not found.\n"

	return ret



#***********************************************************************************************************************

def _get_all_pages(graph_db):
	query = "MATCH (n:Page) RETURN n"
	data, metadata = cypher.execute(graph_db, query)
	if data:
		for row in data:
			ret.append({"id":row[0]["guid"], "name":row[0]["title"]})
	else:
		ret =  "No Pages Found"

	return ret

#***********************************************************************************************************************
def _get_page_likes_count (graph_db, page_name, page_guid):
	# returns the # of users who have liked this page.
	if page_name != None and page_guid != None :
		query = "MATCH (m:User)-[:Likes]-> (n:Page) WHERE n.guid = "+str(page_guid)+" and n.title = "+"'"+str(page_name)+"' RETURN m"
	elif page_name == None:
		query = "MATCH (m:User)-[:Likes]-> (n:Page) WHERE n.guid = "+str(page_guid)+"  RETURN m"
	else:
		query = "MATCH (m:User)-[:Likes]-> (n:Page) WHERE n.title = "+"'"+str(page_name)+"'"+" RETURN m"
	data, metadata = cypher.execute(graph_db, query)
	if data:
		return len (data)
	else:
		return 0

#***********************************************************************************************************************
def _get_pages_created_by (graph_db, user_name, user_guid):
	if user_name != None and user_guid != None :
		query = "MATCH (n:User)-[:Creates]-> (m:Page) WHERE n.guid = "+str(user_guid)+" and n.name = "+"'"+str(user_name)+"' RETURN m"
	elif user_name == None:
		query = "MATCH (n:User)-[:Creates]-> (m:Page) WHERE n.guid = "+str(user_guid)+" RETURN m"
	else:
		query = "MATCH (n:User)-[:Creates]-> (m:Page) WHERE n.name = "+"'"+str(user_name)+"'"+" RETURN m"
	data, metadata = cypher.execute(graph_db, query)
	if data:
		ret = []
		for row in data:
			ret.append({"created_page":row[0]["title"], "created_apge_id":row[0]["guid"]})
	else:
		ret =  "\nPage not found.\n"

	return ret

#***********************************************************************************************************************

def _get_pages_liked_by (graph_db, user_name, user_guid):
	if user_name != None and user_guid != None :
		query = "MATCH (n:User)-[:Likes]-> (m:Page) WHERE n.guid = "+str(user_guid)+" and n.name = "+"'"+str(user_name)+"' RETURN m"
	elif user_name == None:
		query = "MATCH (n:User)-[:Likes]-> (m:Page) WHERE n.guid = "+str(user_guid)+" RETURN m"
	else:
		query = "MATCH (n:User)-[:Likes]-> (m:Page) WHERE n.name = "+"'"+str(user_name)+"'"+" RETURN m"
	data, metadata = cypher.execute(graph_db, query)
	if data:
		ret = []
		for row in data:
			ret.append({"page_name":row[0]["title"], "page_id":row[0]["guid"]})
	else:
		ret =  "\nPage not found.\n"

	return ret

#***********************************************************************************************************************

def _get_page_title (graph_db, page_guid):
	# returns the description of this page.
	if page_guid != None :
		query = "MATCH (n:Page) WHERE n.guid = "+str(page_guid)+" RETURN n"
	data, metadata = cypher.execute(graph_db, query)
	if data:
		for row in data:
			ret = {"page_title":row[0]["title"], "id":row[0]["guid"]}
	else:
		ret =  "\nUser not found.\n"

	return ret

#***********************************************************************************************************************

def _get_page_created_date (graph_db,page_name, page_guid):
	
	
	if page_name != None and page_guid != None :
		query = "MATCH (n:Page) WHERE n.guid = "+str(page_guid)+" and n.title = "+"'"+str(page_name)+"' RETURN n"
	elif page_name == None:
		query = "MATCH (n:Page) WHERE n.guid = "+str(page_guid)+" RETURN n"
	else:
		query = "MATCH (n:Page) WHERE n.title = "+"'"+str(page_name)+"'"+" RETURN n"
	data, metadata = cypher.execute(graph_db, query)
	if data:
		for row in data:
			ret =  {"date" : time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(row[0]["created_time"])) {}
	else:
		ret =  "\nPage not found.\n"

	return ret

#***********************************************************************************************************************

def _get_page_content(graph_db, page_name, page_guid):
	# returns the brief description about the page
	if page_name != None and page_guid != None :
		query = "MATCH (n:Page) WHERE n.page_id = "+str(page_guid)+" and n.title = "+"'"+str(page_name)+"' RETURN n"
	elif page_name == None:
		query = "MATCH (n:Page) WHERE n.page_id = "+str(page_guid)+"  RETURN n"
	else:
		query = "MATCH (n:Page) WHERE n.title = "+"'"+str(page_name)+"'"+" RETURN n"
	data, metadata = cypher.execute(graph_db, query)
	if data:
		for row in data:
			ret =  {"content" : row[0]["text"]}
	else:
		ret =  "\n No content available.\n"

	return ret


#***********************************************************************************************************************

def _get_page_tags(graph_db, page_name, page_guid):
	# returns the brief description about the page
	if page_name != None and page_guid != None :
		query = "MATCH (n:Page) WHERE n.page_id = "+str(page_guid)+" and n.title = "+"'"+str(page_name)+"' RETURN n"
	elif page_name == None:
		query = "MATCH (n:Page) WHERE n.page_id = "+str(page_guid)+"  RETURN n"
	else:
		query = "MATCH (n:Page) WHERE n.title = "+"'"+str(page_name)+"'"+" RETURN n"
	data, metadata = cypher.execute(graph_db, query)
	if data:
		ret = []
		for row in data:
			#for tag in row[0]["tags"]:
			ret =  row[0]["tags"]
	else:
		ret =  "\nTags not found.\n"

	return ret


#***********************************************************************************************************************

def _get_page_container_group(graph_db, page_name, page_guid):
	# returns the brief description about the page
	if page_name != None and page_guid != None :
		query = "MATCH (n:Page) WHERE n.page_id = "+str(page_guid)+" and n.title = "+"'"+str(page_name)+"' RETURN n"
	elif page_name == None:
		query = "MATCH (n:Page) WHERE n.page_id = "+str(page_guid)+"  RETURN n"
	else:
		query = "MATCH (n:Page) WHERE n.title = "+"'"+str(page_name)+"'"+" RETURN n"
	data, metadata = cypher.execute(graph_db, query)
	if data:
		for row in data:
			ret = {"container_group" :row[0]["container_group"]}
	else:
		ret "\n No page/container_group available.\n"

	return ret

#***********************************************************************************************************************

def _get_group_members(graph_db, group_name, group_guid):
 	if group_name != None and group_guid != None :
		query = "MATCH (n:User)-[:is_member]-> (m:Group) WHERE m.group_id = "+str(group_guid)+" and m.name = "+"'"+str(group_name)+"' RETURN n"
	elif group_name == None:
		query = "MATCH (n:User)-[:is_member]-> (m:Group) WHERE m.group_id = "+str(group_guid)+" RETURN n"
	else:
		query = "MATCH (n:User)-[:is_member]-> (m:Group) WHERE m.name = "+"'"+str(group_name)+"'"+" RETURN n"
	data, metadata = cypher.execute(graph_db, query)
	if data:
		ret = []
		for row in data:
			ret.append({"name":row[0]["name"], "id":row[0]["guid"]})
	else:
		ret =  "\nUser not found.\n"

	return ret

#***********************************************************************************************************************
def _get_group_members_count(graph_db, group_name, group_guid):
	# returns the # of members of the group
 	if group_name != None and group_guid != None :
		query = "MATCH (n:User)-[:is_member]-> (m:Group) WHERE m.group_id = "+str(group_guid)+" and m.name = "+"'"+str(group_name)+"' RETURN n"
	elif group_name == None:
		query = "MATCH (n:User)-[:is_member]-> (m:Group) WHERE m.group_id = "+str(group_guid)+" RETURN n"
	else:
		query = "MATCH (n:User)-[:is_member]-> (m:Group) WHERE m.name = "+"'"+str(group_name)+"'"+" RETURN n"
	data, metadata = cypher.execute(graph_db, query)
	if data:
		return len(data)
	else:
		return 0
#***********************************************************************************************************************

def _get_groups_owned_by (graph_db, user_name, user_guid):
	if user_name != None and user_guid != None :
		query = "MATCH (n:User)-[:Owns]-> (m:Group) WHERE n.guid = "+str(user_guid)+" and n.name = "+"'"+str(user_name)+"' RETURN m"
	elif user_name == None:
		query = "MATCH (n:User)-[:Owns]-> (m:Group) WHERE n.guid = "+str(user_guid)+" RETURN m"
	else:
		query = "MATCH (n:User)-[:Owns]-> (m:Group) WHERE n.name = "+"'"+str(user_name)+"'"+" RETURN m"
	data, metadata = cypher.execute(graph_db, query)
	if data:
		ret = []
		for row in data:
			ret.append({"group_name" : row[0]["name"], "group_id" : row[0]["group_id"]})
	else:
		ret =  "\nGroup not found.\n"

	return ret

#***********************************************************************************************************************

def _get_group_owner (graph_db, group_name, group_guid):
	# get the owner of the group
	
	if group_name != None and group_guid != None :
		query = "MATCH (m:User)-[:Owns]-> (n:Group) WHERE n.group_id = "+str(group_guid)+" and n.name = "+"'"+str(group_name)+"' RETURN m"
	elif group_name == None:
		query = "MATCH (m:User)-[:Owns]-> (n:Group) WHERE n.group_id = "+str(group_guid)+"  RETURN m"
	else:
		query = "MATCH (m:User)-[:Owns]-> (n:Group) WHERE n.name = "+"'"+str(group_name)+"'"+" RETURN m"
	data, metadata = cypher.execute(graph_db, query)
	if data:
		for row in data:
			ret = {"User Name" : row[0]["name"], "User Id" : row[0]["guid"]}
	else:
		ret =  "\nOwner not found.\n"

	return ret

#***********************************************************************************************************************

def _get_group_name(graph_db, group_guid):
	if group_guid != None :
		query = "MATCH (n:Group) WHERE n.group_id = "+str(group_guid)+" RETURN n"
	data, metadata = cypher.execute(graph_db, query)
	if data:
		for row in data:
			ret =  {"Group Name" : row[0]["name"] }
	else:
		ret =  "\nGroup not found.\n"

	return ret

#***********************************************************************************************************************

def _get_group_description(graph_db, group_name, group_guid):

	if group_name != None and group_guid != None :
		query = "MATCH (n:Group) WHERE n.group_id = "+str(group_guid)+" and n.name = "+"'"+str(group_name)+"' RETURN n"
	elif group_name == None:
		query = "MATCH (n:Group) WHERE n.group_id = "+str(group_guid)+"  RETURN n"
	else:
		query = "MATCH (n:Group) WHERE n.name = "+"'"+str(group_name)+"'"+" RETURN n"
	data, metadata = cypher.execute(graph_db, query)
	if data:
		for row in data:
			ret =  {"Group description" : row[0]["description"] }
	else:
		ret =  "\nGroup/description not found.\n"

	return ret

#***********************************************************************************************************************

def _get_group_brief_description(graph_db, group_name, group_guid):

	if group_name != None and group_guid != None :
		query = "MATCH (n:Group) WHERE n.group_id = "+str(group_guid)+" and n.name = "+"'"+str(group_name)+"' RETURN n"
	elif group_name == None:
		query = "MATCH (n:Group) WHERE n.group_id = "+str(group_guid)+"  RETURN n"
	else:
		query = "MATCH (n:Group) WHERE n.name = "+"'"+str(group_name)+"'"+" RETURN n"
	data, metadata = cypher.execute(graph_db, query)
	if data:
		for row in data:
			ret = {"Group brief description" : row[0]["brief_desc"] }
	else:
		ret =  "\nGroup/brief description not found.\n"

	return ret

#***********************************************************************************************************************

def _is_events_enabled_in_group(graph_db, group_name, group_guid):

	if group_name != None and group_guid != None :
		query = "MATCH (n:Group) WHERE n.group_id = "+str(group_guid)+" and n.name = "+"'"+str(group_name)+"' RETURN n"
	elif group_name == None:
		query = "MATCH (n:Group) WHERE n.group_id = "+str(group_guid)+"  RETURN n"
	else:
		query = "MATCH (n:Group) WHERE n.name = "+"'"+str(group_name)+"'"+" RETURN n"
	data, metadata = cypher.execute(graph_db, query)
	if data:
		for row in data:
			ret =  "\nis events enabled:"+str(row[0]["events_enabled"])
	else:
		ret =  "\nGroup not found.\n"

	return ret

#***********************************************************************************************************************

def _is_blogs_enabled_in_group(graph_db, group_name, group_guid):

	if group_name != None and group_guid != None :
		query = "MATCH (n:Group) WHERE n.group_id = "+str(group_guid)+" and n.name = "+"'"+str(group_name)+"' RETURN n"
	elif group_name == None:
		query = "MATCH (n:Group) WHERE n.group_id = "+str(group_guid)+"  RETURN n"
	else:
		query = "MATCH (n:Group) WHERE n.name = "+"'"+str(group_name)+"'"+" RETURN n"
	data, metadata = cypher.execute(graph_db, query)
	if data:
		for row in data:
			ret =  "\nis blogs enabled:"+str(row[0]["blogs_enabled"])
	else:
		ret =  "\nGroup not found.\n"

	return ret

#***********************************************************************************************************************

def _is_pages_enabled_in_group(graph_db, group_name, group_guid):

	if group_name != None and group_guid != None :
		query = "MATCH (n:Group) WHERE n.group_id = "+str(group_guid)+" and n.name = "+"'"+str(group_name)+"' RETURN n"
	elif group_name == None:
		query = "MATCH (n:Group) WHERE n.group_id = "+str(group_guid)+"  RETURN n"
	else:
		query = "MATCH (n:Group) WHERE n.name = "+"'"+str(group_name)+"'"+" RETURN n"
	data, metadata = cypher.execute(graph_db, query)
	if data:
		for row in data:
			ret = "\nEvents enabled:"+str(row[0]["pages_enabled"])
	else:
		ret =  "\nGroup not found.\n"	

	return ret

#***********************************************************************************************************************

def _get_blog_likers (graph_db,blog_name, blog_guid):
	# get all the users who liked the blog
	
	if blog_name != None and blog_guid != None :
		query = "MATCH (m:User)-[:Likes]-> (n:Blog) WHERE n.guid = "+str(blog_guid)+" and n.name = "+"'"+str(blog_name)+"' RETURN m"
	elif blog_name == None:
		query = "MATCH (m:User)-[:Likes]-> (n:Blog) WHERE n.guid = "+str(blog_guid)+"  RETURN m"
	else:
		query = "MATCH (m:User)-[:Likes]-> (n:Blog) WHERE n.name = "+"'"+str(blog_name)+"'"+" RETURN m"
	data, metadata = cypher.execute(graph_db, query)
	if data:
		ret = []
		for row in data:
			ret.append({"User Name" : row[0]["name"], "User Id" : row[0]["guid"] })
	else:
		ret =  "\nUser not found.\n"

	return ret	

#***********************************************************************************************************************

def _get_blog_commentators (graph_db,blog_name, blog_guid):
	# get all the users who liked the blog
	
	if blog_name != None and blog_guid != None :
		query = "MATCH (m:User)-[:comments]-> (n:Blog) WHERE n.guid = "+str(blog_guid)+" and n.name = "+"'"+str(blog_name)+"' RETURN m"
	elif blog_name == None:
		query = "MATCH (m:User)-[:comments]-> (n:Blog) WHERE n.guid = "+str(blog_guid)+"  RETURN m"
	else:
		query = "MATCH (m:User)-[:comments]-> (n:Blog) WHERE n.name = "+"'"+str(blog_name)+"'"+" RETURN m"
	data, metadata = cypher.execute(graph_db, query)
	if data:
		ret = []
		for row in data:
			ret.append({"User Name" :row[0]["name"], "User Id" : row[0]["guid"] })
	else:
		ret = "\nUser not found.\n"

	return ret


#***********************************************************************************************************************

def _get_blog_name (graph_db, blog_guid):
	
	if blog_guid != None :
		query = "MATCH (n:Blog) WHERE n.guid = "+str(blog_guid)+"  RETURN n"
	data, metadata = cypher.execute(graph_db, query)
	if data:
		for row in data:
			ret = {"Name" : row[0]["name"] }
		
	else:
		ret =  "\nUser not found.\n"

	return ret

#***********************************************************************************************************************

def _get_blog_description(graph_db, blog_name, blog_guid):
	
	if blog_name != None and blog_guid != None :
		query = "MATCH (n:Blog) WHERE n.guid = "+str(blog_guid)+" and n.name = "+"'"+str(blog_name)+"' RETURN n"
	elif blog_name == None:
		query = "MATCH (n:Blog) WHERE n.guid = "+str(blog_guid)+"  RETURN n"
	else:
		query = "MATCH (n:Blog) WHERE n.name = "+"'"+str(blog_name)+"'"+" RETURN n"
	data, metadata = cypher.execute(graph_db, query)
	if data:
		for row in data:
			ret =  { "Blog description" : row[0]["description"]}
		
	else:
		ret =  "\nBlog not found.\n"

	return ret

#***********************************************************************************************************************

def _get_blog_tags(graph_db, blog_name, blog_guid):
	
	if blog_name != None and blog_guid != None :
		query = "MATCH (n:Blog) WHERE n.guid = "+str(blog_guid)+" and n.name = "+"'"+str(blog_name)+"' RETURN n"
	elif blog_name == None:
		query = "MATCH (n:Blog) WHERE n.guid = "+str(blog_guid)+"  RETURN n"
	else:
		query = "MATCH (n:Blog) WHERE n.name = "+"'"+str(blog_name)+"'"+" RETURN n"
	data, metadata = cypher.execute(graph_db, query)
	if data:
		ret = []
		for row in data:
			#for tag in row[0]["tags"]:
			ret =  row[0]["tags"]
	else:
		ret =  "\nBlog not found.\n"

	return ret

#***********************************************************************************************************************

def _get_blog_created_time(graph_db, blog_name, blog_guid):
	
	if blog_name != None and blog_guid != None :
		query = "MATCH (n:Blog) WHERE n.guid = "+str(blog_guid)+" and n.name = "+"'"+str(blog_name)+"' RETURN n"
	elif blog_name == None:
		query = "MATCH (n:Blog) WHERE n.guid = "+str(blog_guid)+"  RETURN n"
	else:
		query = "MATCH (n:Blog) WHERE n.name = "+"'"+str(blog_name)+"'"+" RETURN n"
	data, metadata = cypher.execute(graph_db, query)
	if data:
		for row in data:
			ret = { "Blog created time":time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(row[0]["created_time"]) )}
	else:
		ret = "\nBlog not found.\n"

	return ret

#***********************************************************************************************************************


def _get_blogs_by_user (graph_db, user_name, user_guid):
	#returns all the blogs created by given user
	if user_name != None and user_guid != None :
		query = "MATCH (n:User)-[:creates]-> (m:Blog) WHERE n.guid = "+str(user_guid)+" and n.name = "+"'"+str(user_name)+"' RETURN m"
	elif user_name == None:
		query = "MATCH (n:User)-[:creates]-> (m:Blog) WHERE n.guid = "+str(user_guid)+" RETURN m"
	else:
		query = "MATCH (n:User)-[:creates]-> (m:Blog) WHERE n.name = "+"'"+str(user_name)+"'"+" RETURN m"
	data, metadata = cypher.execute(graph_db, query)
	if data:
		ret = []
		for row in data:
			ret.append( {"blog":str(row[0]["name"]), "blog_id":str(row[0]["guid"])} )
	else:
		ret = ""
	return ret

#***********************************************************************************************************************

def _get_blog_likers_count (graph_db,blog_name, blog_guid):
	# returns the # of users who liked the blog
	
	if blog_name != None and blog_guid != None :
		query = "MATCH (m:User)-[:Likes]-> (n:Blog) WHERE n.guid = "+str(blog_guid)+" and n.name = "+"'"+str(blog_name)+"' RETURN m"
	elif blog_name == None:
		query = "MATCH (m:User)-[:Likes]-> (n:Blog) WHERE n.guid = "+str(blog_guid)+"  RETURN m"
	else:
		query = "MATCH (m:User)-[:Likes]-> (n:Blog) WHERE n.name = "+"'"+str(blog_name)+"'"+" RETURN m"
	data, metadata = cypher.execute(graph_db, query)
	if data:
		return len(data)
	else:
		return 0

#***********************************************************************************************************************

def  _get_blog_commentator_count (graph_db, blog_name, blog_guid):
	# returns the # of users who commented on the blog
	
	if blog_name != None and blog_guid != None :
		query = "MATCH (m:User)-[:comments]-> (n:Blog) WHERE n.guid = "+str(blog_guid)+" and n.name = "+"'"+str(blog_name)+"' RETURN m"
	elif blog_name == None:
		query = "MATCH (m:User)-[:comments]-> (n:Blog) WHERE n.guid = "+str(blog_guid)+"  RETURN m"
	else:
		query = "MATCH (m:User)-[:comments]-> (n:Blog) WHERE n.name = "+"'"+str(blog_name)+"'"+" RETURN m"
	data, metadata = cypher.execute(graph_db, query)
	if data:
		return len(data)
	else:
		return 0

#***********************************************************************************************************************