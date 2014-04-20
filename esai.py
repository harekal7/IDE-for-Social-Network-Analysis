import snaide

friends_1 = snaide.get_all_friends("Samara Gaylord", None)

print "Friend Suggester"
print
print "These are the users, You can add as your Firends"
print

for i in friends_1:
	friends_2 = snaide.get_all_friends(None, i)
  	for j in friends_2:
		if snaide.is_friend(j, i) and not snaide.is_friend(j, 47173):
		  print snaide.get_user_name(j)