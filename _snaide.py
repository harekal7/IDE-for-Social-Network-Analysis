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
	'''
	print "\n<br \>ID : "+str(row[0]["guid"])+"<br \>"
	print "Name : "+str(row[0]["name"])+"<br \>"
	print
	print "<br \>\nYour Social Network has "+str(len(data))+" Users\n<br \>"
	print
	'''

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
'''			
	print "\n<br \>ID : "+str(row[0]["guid"])+"\n<br \>"
	print "Name : "+str(row[0]["name"])+"\n<br \>"
	print
	else:
		print "\n<br \>User not found.<br \>\n"
'''
#***********************************************************************************************************************

def _get_all_events(graph_db):
	query = "MATCH (n:Event) RETURN n"
	data, metadata = cypher.execute(graph_db, query)
	ret = []
	for row in data:
		ret.append({"guid" : row[0]["guid"], "name" : str(row[0]["name"])} )

	return ret

'''
		print row[0]
		print "\nID : "+str(row[0]["guid"])
		print "Name : "+str(row[0]["name"])
	print
	print "Your Social Network has "+str(len(data))+" Events"
	print
'''

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

'''
		print "Event Found"
		for row in data:
			print "\nName : "+str(row[0]["name"])
			print "Id : "+str(row[0]["guid"])
		print
	else:
		print "\nUser not found.\n"
'''

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
'''
			print "\nName : "+str(row[0]["name"])
			print "Id : "+str(row[0]["guid"])
		print
	else:
		print "\nUser not found.\n"
'''

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
'''
			print "\nStatus : "+str(row[0]["message"])
			print "Id : "+str(row[0]["status_id"])
		print
	else:
		print "\nStatus not found.\n"
'''

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
'''			
			print "\nComment : "+str(row[0]["message"])
			print "Id : "+str(row[0]["comment_id"])
		print
	else:
		print "\nComment not found.\n"
'''

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
'''			
			print "\nName : "+str(row[0]["name"])
			print "Id : "+str(row[0]["guid"])
		print
	else:
		print "\nUser not found.\n"
'''

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
'''
			print "\nGroup : "+str(row[0]["name"])
			print "Id : "+str(row[0]["group_id"])
		print
	else:
		print "\nGroup not found.\n"
'''

#***********************************************************************************************************************

def _get_all_pages(graph_db):
	query = "MATCH (n:Page) RETURN n"
	data, metadata = cypher.execute(graph_db, query)
	ret = []
	if data:
		for row in data:
			ret.append( {"guid" : row[0]["guid"], "name" : str(row[0]["name"]) } )

	return ret

'''		
		print "\nID : "+str(row[0]["guid"])
		print "Name : "+str(row[0]["name"])
	print
	print "Your Social Network has "+str(len(data))+" Pages"
	print
'''

#***********************************************************************************************************************

def _get_all_events(graph_db):
	query = "MATCH (n:Event) RETURN n"
	data, metadata = cypher.execute(graph_db, query)
	for row in data:
		print row[0]
		print "\nID : "+str(row[0]["guid"])
		print "Name : "+str(row[0]["title"])
	print
	print "Your Social Network has "+str(len(data))+" Events"
	print

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
		print "Event Found"
		for row in data:
			print "\nName : "+str(row[0]["title"])
			print "Id : "+str(row[0]["guid"])
		print
	else:
		print "\nEvent not found.\n"


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
		for row in data:
			print "\nUser Name : "+str(row[0]["name"])
			print "User Id : "+str(row[0]["guid"])
		print
	else:
		print "\nEvent not found.\n"

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
			print "\nOrganizer : "+str(row[0]["organizer"])
		print
	else:
		print "\nEvent not found.\n"

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
			
			print "\nDate : "+str(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(row[0]["created_time"])))
		print
	else:
		print "\nEvent not found.\n"

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
			print "\nEvent Title : "+str(row[0]["title"])
		print
	else:
		print "\nEvent not found.\n"

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
		print
	else:
		print "\nEvent not found.\n"
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
			print "\n event short description : "+str(row[0]["short_desc"])
		print
	else:
		print "\n No short description available.\n"


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
			print "\n event description : "+str(row[0]["description"])
		print
	else:
		print "\n No description available.\n"


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
			print "\n event attendees : "+str(row[0]["max_attendees"])
		print
	else:
		print "\n No Event available.\n"


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
			print "\nEvent end registration date : "+str(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(row[0]["end_registration_day"])))
		print
	else:
		print "\n No Event/end registration day available.\n"


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
			print "\n event fee : "+str(row[0]["fee"])
		print
	else:
		print "\n No Event/Event fee available.\n"


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
			print "\n event contact details : "+str(row[0]["contact_details"])
		print
	else:
		print "\n No Event/contact details available.\n"


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
			print "\n event venue : "+str(row[0]["venue"])
		print
	else:
		print "\n No Event/venue available.\n"


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
			print "\n event location : "+str(row[0]["location"])
		print
	else:
		print "\n No Event/location available.\n"


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
			print "\n event website : "+str(row[0]["website"])
		print
	else:
		print "\n No Event/website available.\n"


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
			print "\n event twitter hash : "+str(row[0]["twitter_hash"])
		print
	else:
		print "\n No Event/twitter hash available.\n"


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
			print "\n event location : "+str(row[0]["location"])
		print
	else:
		print "\n No Event/location available.\n"


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
		for row in data:
			for tag in row[0]["tags"]:
				print "tag:"+ str(tag)
		print
	else:
		print "\n No Event/twitter hash available.\n"


#***********************************************************************************************************************

