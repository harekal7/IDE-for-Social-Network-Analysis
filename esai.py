import snaide

users = snaide.get_all_users()

location_list = {}
for user in users:
	l = snaide.get_user_location(None, user)
	try:
	  l = l.split(", ")[1]
	  if location_list.has_key(l):
		  location_list[l] = location_list[l] + 1
	  else:
		  location_list[l] = 1
	except IndexError:
	  pass

max_key = ""
max_value = 0
for key,value in location_list.items():
  if value > max_value:
	max_value = value
	max_key = key
	
print max_key