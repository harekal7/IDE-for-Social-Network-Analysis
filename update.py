from py2neo import neo4j
from py2neo import cypher 
import MySQLdb

#***********************************************************************************************************************

def init(_host, _user, _passwd, _db, _url):
	db = MySQLdb.connect(host=_host, user=_user, passwd=_passwd, db=_db)
	graph_db = neo4j.GraphDatabaseService(_url)
	return graph_db, db

#***********************************************************************************************************************

def clear_graph_db(graph_db):
	cypher.execute(graph_db, "start r=relationship(*) delete r;")
	cypher.execute(graph_db, "MATCH (n {}) DELETE n")
	#MATCH n-[r]-()

#***********************************************************************************************************************

def model_users_statuses_comments(db):
	i = 0
	cur1 = db.cursor() 
	cur2 = db.cursor() 
	cur3 = db.cursor()
	cur4 = db.cursor() 
	cur5 = db.cursor() 
	cur_user_data_1 = db.cursor()
	cur_user_data_2 = db.cursor()
	cur_tags_1 = db.cursor()
	cur_tags_2 = db.cursor()

	cur1.execute("SELECT name, guid, last_login FROM elgg_users_entity")
	for row1 in cur1.fetchall():
			
			#Location
			location = ""
			cur_user_data_1.execute("SELECT value_id FROM  elgg_metadata WHERE owner_guid = "+str(row1[1])+" AND name_id = 44");
			for row_user_data_1 in cur_user_data_1.fetchall():
					cur_user_data_2.execute("SELECT string FROM  elgg_metastrings WHERE id = "+str(row_user_data_1[0]))
					for row_user_data_2 in cur_user_data_2.fetchall():
							location = row_user_data_2[0]

			#brief description
			brief_desc = ""
			cur_user_data_1.execute("SELECT value_id FROM  elgg_metadata WHERE owner_guid = "+str(row1[1])+" AND name_id = 27");
			for row_user_data_1 in cur_user_data_1.fetchall():
					cur_user_data_2.execute("SELECT string FROM  elgg_metastrings WHERE id = "+str(row_user_data_1[0]))
					for row_user_data_2 in cur_user_data_2.fetchall():
							brief_desc = row_user_data_2[0]

			#contact email
			contact_email = ""
			cur_user_data_1.execute("SELECT value_id FROM  elgg_metadata WHERE owner_guid = "+str(row1[1])+" AND name_id = 409");
			for row_user_data_1 in cur_user_data_1.fetchall():
					cur_user_data_2.execute("SELECT string FROM  elgg_metastrings WHERE id = "+str(row_user_data_1[0]))
					for row_user_data_2 in cur_user_data_2.fetchall():
							contact_email = row_user_data_2[0]

			#telephone
			telephone = ""
			cur_user_data_1.execute("SELECT value_id FROM  elgg_metadata WHERE owner_guid = "+str(row1[1])+" AND name_id = 411");
			for row_user_data_1 in cur_user_data_1.fetchall():
					cur_user_data_2.execute("SELECT string FROM  elgg_metastrings WHERE id = "+str(row_user_data_1[0]))
					for row_user_data_2 in cur_user_data_2.fetchall():
							telephone = row_user_data_2[0]

			#Mobile phone
			mobile_phone = ""
			cur_user_data_1.execute("SELECT value_id FROM  elgg_metadata WHERE owner_guid = "+str(row1[1])+" AND name_id = 413");
			for row_user_data_1 in cur_user_data_1.fetchall():
					cur_user_data_2.execute("SELECT string FROM  elgg_metastrings WHERE id = "+str(row_user_data_1[0]))
					for row_user_data_2 in cur_user_data_2.fetchall():
							mobile_phone = row_user_data_2[0]


			#website
			website = ""
			cur_user_data_1.execute("SELECT value_id FROM  elgg_metadata WHERE owner_guid = "+str(row1[1])+" AND name_id = 63");
			for row_user_data_1 in cur_user_data_1.fetchall():
					cur_user_data_2.execute("SELECT string FROM  elgg_metastrings WHERE id = "+str(row_user_data_1[0]))
					for row_user_data_2 in cur_user_data_2.fetchall():
							website = row_user_data_2[0]


			#about_me
			about_me = ""
			cur_user_data_1.execute("SELECT value_id FROM  elgg_metadata WHERE owner_guid = "+str(row1[1])+" AND name_id = 387");
			for row_user_data_1 in cur_user_data_1.fetchall():
					cur_user_data_2.execute("SELECT string FROM  elgg_metastrings WHERE id = "+str(row_user_data_1[0]))
					for row_user_data_2 in cur_user_data_2.fetchall():
							about_me = row_user_data_2[0]

			#skills
			skills = ["null"]
			no = False
			cur_user_data_1.execute("SELECT value_id FROM  elgg_metadata WHERE owner_guid = "+str(row1[1])+" AND name_id = 402");
			for row_user_data_1 in cur_user_data_1.fetchall():
					cur_user_data_2.execute("SELECT string FROM  elgg_metastrings WHERE id = "+str(row_user_data_1[0]))
					for row_user_data_2 in cur_user_data_2.fetchall():
							if no==False:
								no=True
								skills.pop()
								skills.append(row_user_data_2[0])
							else:
								skills.append(row_user_data_2[0])


			#interests
			no = False
			interests = ["null"]
			cur_user_data_1.execute("SELECT value_id FROM  elgg_metadata WHERE owner_guid = "+str(row1[1])+" AND name_id = 29");
			for row_user_data_1 in cur_user_data_1.fetchall():
					cur_user_data_2.execute("SELECT string FROM  elgg_metastrings WHERE id = "+str(row_user_data_1[0]))
					for row_user_data_2 in cur_user_data_2.fetchall():
							if no==False:
								no=True
								interests.pop()
								interests.append(row_user_data_2[0])
							else:
								interests.append(row_user_data_2[0])

			i = i + 1
			print i, unicode(row1[0], errors='ignore')
			user, = graph_db.create({"name": unicode(row1[0], errors='ignore'), "guid":row1[1], "location":location,
			 "brief_description":brief_desc, "contact_email":contact_email, "telephone":telephone,
			 "mobile_phone":mobile_phone, "website":website, "about_me":about_me,
			  "interests":interests, "skills":skills, "last_login":row1[2]})
			user.add_labels("User")
			
			
			cur2.execute("SELECT guid, time_updated FROM elgg_entities WHERE owner_guid="+str(row1[1])+" AND subtype=5")
			for row2 in cur2.fetchall():
				
				#tags
				tags = ["none"]
				no = False
				cur_tags_1.execute("SELECT value_id FROM elgg_metadata WHERE name_id=50 AND entity_guid="+str(row2[0]))
				for row_tags_1 in cur_tags_1.fetchall():
					cur_tags_2.execute("SELECT string FROM elgg_metastrings WHERE id="+str(row_tags_1[0]))
					for row_tags_2 in cur_tags_2.fetchall():
						if no==False:
								no=True
								tags.pop()
								tags.append(row_tags_2[0])
						else:
								tags.append(row_tags_2[0])



				cur3.execute("SELECT description FROM elgg_objects_entity WHERE guid="+str(row2[0]))
				for row3 in cur3.fetchall():
						cur4.execute("SELECT Count(*) FROM elgg_annotations WHERE entity_guid="+str(row2[0])+" AND name_id=16")
						for row4 in cur4.fetchall():
								if cur5.execute("SELECT guid_two FROM elgg_entity_relationships WHERE guid_one="+str(row2[0])+" AND relationship like 'parent'"):
										for row5 in cur5.fetchall():
												comment, = graph_db.create({"comment_id":row2[0], "message":str(row3[0]), "updated_time":str(row2[1]), "likes":row4[0], "tags":tags })
												comment.add_labels("Comment")
												query_string = "MATCH (a:Status),(b:Comment) WHERE a.status_id ="+str(row5[0])+" AND b.comment_id = "+str(row2[0])+" CREATE (a)-[r:has_comment]->(b) CREATE (b)-[r:for_status]->(a) RETURN r"
												result = neo4j.CypherQuery(graph_db, query_string).execute()
												query_string = "MATCH (a:User),(b:Comment) WHERE a.guid ="+str(row1[1])+" AND b.comment_id = "+str(row2[0])+" CREATE (a)-[r1:comments]->(b) CREATE (b)-[r2:comment_by]->(a) RETURN r1, r2"
												result = neo4j.CypherQuery(graph_db, query_string).execute()
								else:
										status, = graph_db.create({"status_id":row2[0], "message":str(row3[0]), "updated_time":str(row2[1]), "likes":row4[0], "tags":tags })
										status.add_labels("Status")
										query_string = "MATCH (a:User),(b:Status) WHERE a.guid ="+str(row1[1])+" AND b.status_id = "+str(row2[0])+" CREATE (a)-[r1:Posted]->(b) CREATE (b)-[r2:Posted_by]->(a) RETURN r1, r2"
										result = neo4j.CypherQuery(graph_db, query_string).execute()

#**********************************************************************************************************************

def model_friends(db):
	cur1 = db.cursor() 
	cur1.execute("SELECT guid_one, guid_two FROM elgg_entity_relationships WHERE relationship like 'friend'")
	for row1 in cur1.fetchall():
	    query_string = "MATCH (a:User),(b:User) WHERE a.guid ="+str(row1[0])+" AND b.guid = "+str(row1[1])+" CREATE (a)-[r1:Friend]->(b) CREATE (b)-[r2:Friend]->(a) RETURN r1, r2"
	    result = neo4j.CypherQuery(graph_db, query_string).execute()

#**********************************************************************************************************************

#Groups:
#1. Get all group related data from elgg_groups_entity table
#2. Get group and owner of that group from elgg_entities table with type group
#3. Get group and members of that group from elgg_entity_relationships table with relationship member
#4. Create a bidirectional relationship Owns/owner b/w user and groups.
#5. Create a bidirectional relationship is_member/members b/w user and groups.

def model_groups(db):
	cur1 = db.cursor()
	cur_tags_1 = db.cursor()
	cur_tags_2 = db.cursor()

	cur1.execute("SELECT * FROM elgg_groups_entity")
	for row1 in cur1.fetchall():

			#tags
			no = False
			tags = ["none"]
			cur_tags_1.execute("SELECT value_id FROM  elgg_metadata WHERE entity_guid = "+str(row1[0])+" AND name_id = 29");
			for row_tags_1 in cur_tags_1.fetchall():
					cur_tags_2.execute("SELECT string FROM  elgg_metastrings WHERE id = "+str(row_tags_1[0]))
					for row_tags_2 in cur_tags_2.fetchall():
							if no==False:
								no=True
								tags.pop()
								tags.append(row_tags_2[0])
							else:
								tags.append(row_tags_2[0])



			#brief_desc
			brief_desc = ""
			cur_tags_1.execute("SELECT value_id FROM  elgg_metadata WHERE entity_guid = "+str(row1[0])+" AND name_id = 27");
			for row_tags_1 in cur_tags_1.fetchall():
					cur_tags_2.execute("SELECT string FROM  elgg_metastrings WHERE id = "+str(row_tags_1[0]))
					for row_tags_2 in cur_tags_2.fetchall():
							brief_desc = row_tags_2[0]


			#pages_enabled?
			cur_tags_1.execute("SELECT entity_guid FROM elgg_metadata WHERE entity_guid ="+str(row1[0])+" AND name_id = 37 AND value_id = 32")
			for row_tags_1 in cur_tags_1.fetchall():
					if row1[0] == row_tags_1[0]:
						pages_enabled = "yes"
					else:
						pages_enabled = "no"

			#blogs_enabled?
			cur_tags_1.execute("SELECT entity_guid FROM  elgg_metadata WHERE entity_guid ="+str(row1[0])+" AND name_id = 31 AND value_id = 32");
			for row_tags_1 in cur_tags_1.fetchall():
					if row1[0] == row_tags_1[0]:
						blogs_enabled = "yes"
					else:
						blogs_enabled = "no"

			#events_enabled?
			cur_tags_1.execute("SELECT entity_guid FROM  elgg_metadata WHERE entity_guid ="+str(row1[0])+" AND name_id = 96 AND value_id = 32");
			for row_tags_1 in cur_tags_1.fetchall():
					if row1[0] == row_tags_1[0]:
						events_enabled = "yes"
					else:
						events_enabled = "no"

			desc = unicode(row1[2], errors='replace')
			group, = graph_db.create({ "group_id":row1[0], "name":row1[1], "description":desc, "tags":tags,
	     "brief_desc":brief_desc, "pages_enabled":pages_enabled, "blogs_enabled":blogs_enabled,
	     "events_enabled":events_enabled})
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

def model_events(db):
	cur1 = db.cursor() 
	cur2 = db.cursor() 
	cur3 = db.cursor()
	cur4 = db.cursor()

	cur1.execute("SELECT guid , time_created, owner_guid FROM elgg_entities WHERE subtype = 7")
	for row1 in cur1.fetchall():
		
		#Location
		location = ""
		cur2.execute("SELECT value_id FROM elgg_metadata WHERE name_id=44 AND entity_guid="+str(row1[0]))
		for row2 in cur2.fetchall():
				cur3.execute("SELECT string FROM elgg_metastrings WHERE id = "+str(row2[0]))
				for row3 in cur3.fetchall():
						location = row3[0]


		#short_desc
		short_desc = ""
		cur2.execute("SELECT value_id FROM elgg_metadata WHERE name_id=51 AND entity_guid="+str(row1[0]))
		for row2 in cur2.fetchall():
				cur3.execute("SELECT string FROM elgg_metastrings WHERE id = "+str(row2[0]))
				for row3 in cur3.fetchall():
						short_desc = row3[0]



		#venue
		venue = ""
		cur2.execute("SELECT value_id FROM elgg_metadata WHERE name_id=59 AND entity_guid="+str(row1[0]))
		for row2 in cur2.fetchall():
				cur3.execute("SELECT string FROM elgg_metastrings WHERE id = "+str(row2[0]))
				for row3 in cur3.fetchall():
						venue = row3[0]


		#twitter_hash
		twitter_hash = ""
		cur2.execute("SELECT value_id FROM elgg_metadata WHERE name_id=61 AND entity_guid="+str(row1[0]))
		for row2 in cur2.fetchall():
				cur3.execute("SELECT string FROM elgg_metastrings WHERE id = "+str(row2[0]))
				for row3 in cur3.fetchall():
						twitter_hash = row3[0]


		#contact_details
		contact_details = ""
		cur2.execute("SELECT value_id FROM elgg_metadata WHERE name_id=62 AND entity_guid="+str(row1[0]))
		for row2 in cur2.fetchall():
				cur3.execute("SELECT string FROM elgg_metastrings WHERE id = "+str(row2[0]))
				for row3 in cur3.fetchall():
						contact_details = row3[0]

		#website
		website = ""
		cur2.execute("SELECT value_id FROM elgg_metadata WHERE name_id=63 AND entity_guid="+str(row1[0]))
		for row2 in cur2.fetchall():
				cur3.execute("SELECT string FROM elgg_metastrings WHERE id = "+str(row2[0]))
				for row3 in cur3.fetchall():
						website = row3[0]


		#fee
		fee = ""
		cur2.execute("SELECT value_id FROM elgg_metadata WHERE name_id=65 AND entity_guid="+str(row1[0]))
		for row2 in cur2.fetchall():
				cur3.execute("SELECT string FROM elgg_metastrings WHERE id = "+str(row2[0]))
				for row3 in cur3.fetchall():
						fee = row3[0]



		#start_day
		start_day = ""
		cur2.execute("SELECT value_id FROM elgg_metadata WHERE name_id=66 AND entity_guid="+str(row1[0]))
		for row2 in cur2.fetchall():
				cur3.execute("SELECT string FROM elgg_metastrings WHERE id = "+str(row2[0]))
				for row3 in cur3.fetchall():
						start_day = row3[0]


		#start_time
		start_time = ""
		cur2.execute("SELECT value_id FROM elgg_metadata WHERE name_id=68 AND entity_guid="+str(row1[0]))
		for row2 in cur2.fetchall():
				cur3.execute("SELECT string FROM elgg_metastrings WHERE id = "+str(row2[0]))
				for row3 in cur3.fetchall():
						start_time = row3[0]

		#end_registration_day
		end_registration_day = ""
		cur2.execute("SELECT value_id FROM elgg_metadata WHERE name_id=71 AND entity_guid="+str(row1[0]))
		for row2 in cur2.fetchall():
				cur3.execute("SELECT string FROM elgg_metastrings WHERE id = "+str(row2[0]))
				for row3 in cur3.fetchall():
						end_registration_day = row3[0]


		#organizer
		organizer = ""
		cur2.execute("SELECT value_id FROM elgg_metadata WHERE name_id=64 AND entity_guid="+str(row1[0]))
		for row2 in cur2.fetchall():
				cur3.execute("SELECT string FROM elgg_metastrings WHERE id = "+str(row2[0]))
				for row3 in cur3.fetchall():
						organizer = row3[0]



		#max_attendees
		max_attendees = ""
		cur2.execute("SELECT value_id FROM elgg_metadata WHERE name_id=58 AND entity_guid="+str(row1[0]))
		for row2 in cur2.fetchall():
				cur3.execute("SELECT string FROM elgg_metastrings WHERE id = "+str(row2[0]))
				for row3 in cur3.fetchall():
						max_attendees = row3[0]


		#tags
		no = False
		tags = ["none"]
		cur2.execute("SELECT value_id FROM  elgg_metadata WHERE entity_guid = "+str(row1[0])+" AND name_id = 50");
		for row2 in cur2.fetchall():
				cur3.execute("SELECT string FROM  elgg_metastrings WHERE id = "+str(row2[0]))
				for row3 in cur3.fetchall():
						if no==False:
							no=True
							tags.pop()
							tags.append(row3[0])
						else:
							tags.append(row3[0])


		cur2.execute("SELECT title, description FROM elgg_objects_entity WHERE guid = "+str(row1[0])+" ")
		for row2 in cur2.fetchall():
			event, = graph_db.create({"title": row2[0], "guid":row1[0], "created_time": row1[1],
				"location":location, "tags":tags, "short_desc":short_desc, "venue":venue,
				 "max_attendees":max_attendees, "organizer":organizer,
				  "end_registration_day":end_registration_day, "start_time":start_time, "start_day":start_day,
				  "fee":fee, "website":website, "contact_details":contact_details, "venue":venue,
				  "twitter_hash":twitter_hash, "description":row2[1]})
			event.add_labels("Event")
			cur3.execute("SELECT guid_two FROM elgg_entity_relationships WHERE guid_one = "+str(row1[0])+" ")
			for row3 in cur3.fetchall():
				query_string = "MATCH (a:User),(b:Event) WHERE a.guid ="+str(row3[0])+" AND b.guid = "+str(row1[0])+" CREATE (a)-[r1:Attends]->(b) CREATE (b)-[r2:Attendees]->(a) RETURN r1, r2"
				result = neo4j.CypherQuery(graph_db, query_string).execute()

		query_string = "MATCH (a:User),(b:Event) WHERE a.guid ="+str(row1[2])+" AND b.guid = "+str(row1[0])+" CREATE (a)-[r1:Owns_event]->(b) CREATE (b)-[r2:Owner_event]->(a) RETURN r1, r2"
		result = neo4j.CypherQuery(graph_db, query_string).execute()


#***********************************************************************************************************************

#Pages:
#1. Get guid from elgg_entities table with subtype value = 14
#2. Use this guid to get name of the Page from elgg_objects_entity table
#3. Get the id's of people who have liked this page(or done some kind of participation in this page) from elgg_annotations table searching for guid.
#4. Create a bidirectional relationship b/w user and page.

def model_pages(db):
	cur1 = db.cursor() 
	cur2 = db.cursor() 
	cur3 = db.cursor()
	cur4 = db.cursor()
	cur5 = db.cursor()
	cur_tags_1 = db.cursor()
	cur_tags_2 = db.cursor()

	cur1.execute("SELECT guid , time_created FROM elgg_entities WHERE subtype = 14")
	for row1 in cur1.fetchall():


			#text
			text = ""
			cur4.execute("SELECT value_id FROM elgg_annotations WHERE entity_guid = "+str(row1[0])+" AND name_id = 102 AND value_id <> 11")
			for row4 in cur4.fetchall():
					cur5.execute("SELECT string FROM elgg_metastrings WHERE id = "+str(row4[0]))
					for row5 in cur5.fetchall():
							text = row5[0]


			#tags
			no = False
			tags = ["none"]
			cur_tags_1.execute("SELECT value_id FROM  elgg_metadata WHERE entity_guid = "+str(row1[0])+" AND name_id = 50");
			for row_tags_1 in cur_tags_1.fetchall():
					cur_tags_2.execute("SELECT string FROM  elgg_metastrings WHERE id = "+str(row_tags_1[0]))
					for row_tags_2 in cur_tags_2.fetchall():
							if no==False:
								no=True
								tags.pop()
								tags.append(row_tags_2[0])
							else:
								tags.append(row_tags_2[0])



			#container_group
			cur_tags_1.execute("SELECT container_guid FROM  elgg_entities WHERE guid = "+str(row1[0]))
			for row_tags_1 in cur_tags_1.fetchall():
					container_group = row_tags_1[0]


			cur2.execute("SELECT title FROM elgg_objects_entity WHERE guid = "+str(row1[0]))
			for row2 in cur2.fetchall():
					page, = graph_db.create({"title": row2[0], "guid":row1[0], "created_time": row1[1],
	        	"text":text, "tags":tags, "container_group":container_group})
					page.add_labels("Page")
					cur3.execute("SELECT  owner_guid FROM elgg_annotations WHERE entity_guid = "+str(row1[0])+" AND name_id = 16")
					for row3 in cur3.fetchall():
							query_string = "MATCH (a:User),(b:Page) WHERE a.guid ="+str(row3[0])+" AND b.guid = "+str(row1[0])+" CREATE (a)-[r1:Likes]->(b) CREATE (b)-[r2:Liked_by]->(a) RETURN r1, r2"
							result = neo4j.CypherQuery(graph_db, query_string).execute()
					
					cur3.execute("SELECT  owner_guid FROM elgg_annotations WHERE entity_guid = "+str(row1[0])+" AND name_id = 102")
					for row3 in cur3.fetchall():
							query_string = "MATCH (a:User),(b:Page) WHERE a.guid ="+str(row3[0])+" AND b.guid = "+str(row1[0])+" CREATE (a)-[r1:Creates]->(b) CREATE (b)-[r2:Created_by]->(a) RETURN r1, r2"
							result = neo4j.CypherQuery(graph_db, query_string).execute()


#***********************************************************************************************************************


#Blogs:
#1. Get guid from elgg_entities table with subtype value = 4
#2. Use this guid to get name of the Blog from elgg_objects_entity table
#3. Get the id's of people who have liked this blog  from elgg_annotations table searching for guid and name_id = 17.
#4. Create a bidirectional relationship as user likes blog.
#5. Get the id's of people who have commented on this blog  from elgg_annotations table searching for guid and name_id = 16.
#6. Create a bidirectional relationship as user commented on  blog.
#7  Also create a bidirectional relationship user -> creates -> blog.

def model_blogs(db):
	cur1 = db.cursor() 
	cur2 = db.cursor() 
	cur3 = db.cursor()
	cur_tags_1 = db.cursor()
	cur_tags_2 = db.cursor()
	cur1.execute("SELECT guid , time_created , owner_guid FROM elgg_entities WHERE subtype = 4")
	for row1 in cur1.fetchall():
		
			#tags
			tags = ["none"]
			no = False
			cur_tags_1.execute("SELECT value_id FROM  elgg_metadata WHERE entity_guid = "+str(row1[0])+" AND name_id = 50");
			for row_tags_1 in cur_tags_1.fetchall():
					cur_tags_2.execute("SELECT string FROM  elgg_metastrings WHERE id = "+str(row_tags_1[0]))
					for row_tags_2 in cur_tags_2.fetchall():
							if no==False:
								no=True
								tags.pop()
								tags.append(row_tags_2[0])
							else:
								tags.append(row_tags_2[0])


			#container_group
			cur_tags_1.execute("SELECT container_guid FROM  elgg_entities WHERE guid = "+str(row1[0]));
			for row_tags_1 in cur_tags_1.fetchall():
					container_group = row_tags_1[0]


			cur2.execute("SELECT title, description FROM elgg_objects_entity WHERE guid = "+str(row1[0])+" ")
			for row2 in cur2.fetchall():
				blog, = graph_db.create({"name": row2[0], "guid":row1[0], "created_time": row1[1],
					"description":row2[1], "tags":tags, "container_group":container_group})
				blog.add_labels("Blog")
				#print row2[0]
				cur3.execute("SELECT  owner_guid FROM elgg_annotations WHERE entity_guid = "+str(row1[0])+" AND name_id = 16")
				for row3 in cur3.fetchall():
					query_string = "MATCH (a:User),(b:Blog) WHERE a.guid ="+str(row3[0])+" AND b.guid = "+str(row1[0])+" CREATE (a)-[r1:Likes]->(b) CREATE (b)-[r2:Liked_by]->(a) RETURN r1, r2"
					result = neo4j.CypherQuery(graph_db, query_string).execute()
					
					cur3.execute("SELECT  owner_guid FROM elgg_annotations WHERE entity_guid = "+str(row1[0])+" AND name_id = 82")
					for row3 in cur3.fetchall():
							query_string = "MATCH (a:User),(b:Blog) WHERE a.guid ="+str(row3[0])+" AND b.guid = "+str(row1[0])+" CREATE (a)-[r1:comments]->(b) CREATE (b)-[r2:has_comment]->(a) RETURN r1, r2"
							result = neo4j.CypherQuery(graph_db, query_string).execute()


			query_string = "MATCH (a:User),(b:Blog) WHERE a.guid ="+str(row1[2])+" AND b.guid = "+str(row1[0])+" CREATE (a)-[r1:creates]->(b) CREATE (b)-[r2:created_by]->(a) RETURN r1, r2"
			result = neo4j.CypherQuery(graph_db, query_string).execute()    

#***********************************************************************************************************************
if __name__ == "__main__":
	graph_db, db = init("localhost", "root", "", "elgg", "http://localhost:7474/db/data/")
	clear_graph_db(graph_db)
	print "model_users_statuses_comments"
	model_users_statuses_comments(db)
	print "model_friends"
	model_friends(db)
	print "model_groups"
	model_groups(db)
	print "model_events"
	model_events(db)
	print "model_pages"
	model_pages(db)	
	print "model_blogs"
	model_blogs(db)

#***********************************************************************************************************************