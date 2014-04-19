import snaide

groups = snaide.get_all_groups()

maxie = 0

for group in groups:
	count = 0
	members = snaide.get_group_members(None, group["guid"])
	for member in members:
		count = count + len(snaide.get_blogs_by_user(None, member["guid"]))

	if count > maxie:
		maxie = count
		ret_group = group

print maxie, snaide.get_group_name(ret_group["guid"])