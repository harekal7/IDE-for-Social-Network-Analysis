from py2neo import neo4j
from py2neo import cypher 
import MySQLdb
import cgitb
cgitb.enable()

#***********************************************************************************************************************

def init(_host, _user, _passwd, _db, _url):
	db = MySQLdb.connect(host=_host, user=_user, passwd=_passwd, db=_db)
	cur1 = db.cursor() 
	cur2 = db.cursor() 
	cur3 = db.cursor()
	cur4 = db.cursor() 
	cur5 = db.cursor() 
	graph_db = neo4j.GraphDatabaseService(_url)
	return graph_db, cur1, cur2, cur3, cur4, cur5

#***********************************************************************************************************************

def clear_graph_db(graph_db):
	cypher.execute(graph_db, "start r=relationship(*) delete r;")
	cypher.execute(graph_db, "MATCH (n {}) DELETE n")

#***********************************************************************************************************************

def model_users_statuses_comments(cur1, cur2, cur3, cur4, cur5):
	cur1.execute("SELECT name, guid FROM elgg_users_entity")
	for row1 in cur1.fetchall():
	    user, = graph_db.create({"name": row1[0], "guid":row1[1]})
	    user.add_labels("User")
	    cur2.execute("SELECT guid, time_updated FROM elgg_entities WHERE owner_guid="+str(row1[1])+" AND subtype=5")
	    for row2 in cur2.fetchall():
	        cur3.execute("SELECT description FROM elgg_objects_entity WHERE guid="+str(row2[0]))
	        for row3 in cur3.fetchall():
	            cur4.execute("SELECT Count(*) FROM elgg_annotations WHERE entity_guid="+str(row2[0])+" AND name_id=16")
	            for row4 in cur4.fetchall():
	                if cur5.execute("SELECT guid_two FROM elgg_entity_relationships WHERE guid_one="+str(row2[0])+" AND relationship like 'parent'"):
	                    for row5 in cur5.fetchall():
	                        comment, = graph_db.create({"comment_id":row2[0], "message":str(row3[0]), "updated_time":str(row2[1]), "likes":row4[0] })
	                        comment.add_labels("Comment")
	                        query_string = "MATCH (a:Status),(b:Comment) WHERE a.status_id ="+str(row5[0])+" AND b.comment_id = "+str(row2[0])+" CREATE (a)-[r:has_comment]->(b) RETURN r"
	                        result = neo4j.CypherQuery(graph_db, query_string).execute()
	                        query_string = "MATCH (a:User),(b:Comment) WHERE a.guid ="+str(row1[1])+" AND b.comment_id = "+str(row2[0])+" CREATE (a)-[r:comments]->(b) RETURN r"
	                        result = neo4j.CypherQuery(graph_db, query_string).execute()
	                else:
	                    status, = graph_db.create({"status_id":row2[0], "message":str(row3[0]), "updated_time":str(row2[1]), "likes":row4[0] })
	                    status.add_labels("Status")
	                    query_string = "MATCH (a:User),(b:Status) WHERE a.guid ="+str(row1[1])+" AND b.status_id = "+str(row2[0])+" CREATE (a)-[r:Posted]->(b) RETURN r"
	                    result = neo4j.CypherQuery(graph_db, query_string).execute()

#**********************************************************************************************************************

def model_friends(cur1):
	cur1.execute("SELECT guid_one, guid_two FROM elgg_entity_relationships WHERE relationship like 'friend'")
	for row1 in cur1.fetchall():
	    query_string = "MATCH (a:User),(b:User) WHERE a.guid ="+str(row1[0])+" AND b.guid = "+str(row1[1])+" CREATE (a)-[r:Friend]->(b) RETURN r"
	    result = neo4j.CypherQuery(graph_db, query_string).execute()

#**********************************************************************************************************************

#Groups:
#1. Get all group related data from elgg_groups_entity table
#2. Get group and owner of that group from elgg_entities table with type group
#3. Get group and members of that group from elgg_entity_relationships table with relationship member
#4. Create a bidirectional relationship Owns/owner b/w user and groups.
#5. Create a bidirectional relationship is_member/members b/w user and groups.

def model_groups(cur1):
	cur1.execute("SELECT * FROM elgg_groups_entity")
	for row1 in cur1.fetchall():
	    desc = unicode(row1[2], errors='replace')
	    group, = graph_db.create({ "group_id":row1[0], "name":row1[1], "description":desc })
	    group.add_labels("Group")

	cur1.execute("SELECT guid, owner_guid FROM elgg_entities WHERE type like 'group'")
	for row1 in cur1.fetchall():
	    query_string = "MATCH (a:User),(b:Group) WHERE a.guid ="+str(row1[1])+" AND b.group_id = "+str(row1[0])+" CREATE (a)-[r1:Owns]->(b) CREATE (b)-[r2:Owner]->(a) RETURN r1, r2"
	    result = neo4j.CypherQuery(graph_db, query_string).execute()

	cur1.execute("SELECT guid_one, guid_two FROM elgg_entity_relationships WHERE relationship like 'member'")
	for row1 in cur1.fetchall():
	    query_string = "MATCH (a:User),(b:Group) WHERE a.guid ="+str(row1[0])+" AND b.group_id = "+str(row1[1])+" CREATE (a)-[r1:is_member]->(b) CREATE (b)-[r2:Members]->(a) RETURN r1, r2"
	    result = neo4j.CypherQuery(graph_db, query_string).execute()

#**********************************************************************************************************************

#Events:
#1. Get guid from elgg_entities table with subtype value = 7
#2. Use this guid to get name of the event from elgg_objects_entity table
#3. Get the id's of people attending this event from elgg_entity_relationships table searching for guid.
#4. Create a bidirectional relationship b/w user and Events.

def model_events(cur1, cur2, cur3):
	cur1.execute("SELECT guid , time_created FROM elgg_entities WHERE subtype = 7")
	for row1 in cur1.fetchall():
	    cur2.execute("SELECT title FROM elgg_objects_entity WHERE guid = "+str(row1[0])+" ")
	    for row2 in cur2.fetchall():
	        event, = graph_db.create({"name": row2[0], "guid":row1[0], "created_time": row1[1]})
	        event.add_labels("Event")
	        cur3.execute("SELECT guid_two FROM elgg_entity_relationships WHERE guid_one = "+str(row1[0])+" ")
	        for row3 in cur3.fetchall():
	            # create a relationship user -> attends -> event
	            #  create a relationship user -> attends -> event
	            query_string = "MATCH (a:User),(b:Event) WHERE a.guid ="+str(row3[0])+" AND b.guid = "+str(row1[0])+" CREATE (a)-[r1:Attends]->(b) CREATE (b)-[r2:Attendees]->(a) RETURN r1, r2"
	            result = neo4j.CypherQuery(graph_db, query_string).execute()

#***********************************************************************************************************************

#Pages:
#1. Get guid from elgg_entities table with subtype value = 14
#2. Use this guid to get name of the Page from elgg_objects_entity table
#3. Get the id's of people who have liked this page(or done some kind of participation in this page) from elgg_annotations table searching for guid.
#4. Create a bidirectional relationship b/w user and page.

def model_pages(cur1, cur2, cur3):
	cur1.execute("SELECT guid , time_created FROM elgg_entities WHERE subtype = 14")
	for row1 in cur1.fetchall():
	    cur2.execute("SELECT title FROM elgg_objects_entity WHERE guid = "+str(row1[0])+" ")
	    for row2 in cur2.fetchall():
	        page, = graph_db.create({"name": row2[0], "guid":row1[0], "created_time": row1[1]})
	        page.add_labels("Page")
	        cur3.execute("SELECT  owner_guid FROM elgg_annotations WHERE entity_guid = "+str(row1[0])+" AND name_id = 16")
	        for row3 in cur3.fetchall():
	            # create a relationship user -> likes -> page
	            #  create a relationship Page -> liked_by -> user
	            query_string = "MATCH (a:User),(b:Page) WHERE a.guid ="+str(row3[0])+" AND b.guid = "+str(row1[0])+" CREATE (a)-[r1:Likes]->(b) CREATE (b)-[r2:Liked_by]->(a) RETURN r1, r2"
	            result = neo4j.CypherQuery(graph_db, query_string).execute()

	        cur3.execute("SELECT  owner_guid FROM elgg_annotations WHERE entity_guid = "+str(row1[0])+" AND name_id = 102")
	        for row3 in cur3.fetchall():
	            # create a relationship user -> likes -> page
	            # create a relationship Page -> created_by -> user
	            query_string = "MATCH (a:User),(b:Page) WHERE a.guid ="+str(row3[0])+" AND b.guid = "+str(row1[0])+" CREATE (a)-[r1:Creates]->(b) CREATE (b)-[r2:Created_by]->(a) RETURN r1, r2"
	            result = neo4j.CypherQuery(graph_db, query_string).execute()

#***********************************************************************************************************************

def get_all_users(graph_db):
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

def get_one_user(graph_db, user_name, user_guid):
	if user_name != None and user_guid != None :
		query = "MATCH (n:User) WHERE n.name = "+"'"+str(user_name)+"' and n.guid = "+str(user_guid)+"  RETURN n"
	elif user_name == None:
		query = "MATCH (n:User) WHERE n.guid = "+str(user_guid)+" RETURN n"
	else:
		query = "MATCH (n:User) WHERE n.name = "+"'"+str(user_name)+"'"+" RETURN n"
	data, metadata = cypher.execute(graph_db, query)
	if data:
		for row in data:
			ret = ( {"guid" : row[0]["guid"], 
								 "name" : str(row[0]["name"])} 
							);
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

if __name__ == "__main__":
	graph_db, cur1, cur2, cur3, cur4, cur5 = init("localhost", "root", "", "elgg", "http://localhost:7474/db/data/")
	#clear_graph_db(graph_db)
	#model_users_statuses_comments(cur1, cur2, cur3, cur4, cur5)
	#model_friends(cur1)
	#model_groups(cur1)
	#model_events(cur1, cur2, cur3)
	#model_pages(cur1, cur2, cur3)
	#users = get_all_users(graph_db)
	#get_one_user(graph_db, "vikyath", 39)
	#get_one_user(graph_db, "vikyath", None)
	#get_one_user(graph_db, None, "39")


#***********************************************************************************************************************