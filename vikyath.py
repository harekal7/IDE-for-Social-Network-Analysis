import snaide

groups = snaide.get_all_groups()

maximum = 0

for group in groups:
	count = 0
	members = snaide.get_group_members(None, group)
	for member in members:
		count = count + len(snaide.get_blogs_by_user(None, member))

	if count > maximum:
		maximum = count
		ret_group = group

print maximum, snaide.get_group_name(ret_group)