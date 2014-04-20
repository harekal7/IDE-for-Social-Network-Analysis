import snaide

group = set([])

friends = snaide.get_all_friends(None, 47173)

for friend in friends:
	g = snaide.groups_with_user_as_member(None, friend)
	for j in g:
		if not snaide.is_user_member_of_group(47173, j):
			group.add(j)

for e in group:
	print snaide.get_group_name(e)