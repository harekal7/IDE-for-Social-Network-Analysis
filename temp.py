import snaide

print snaide.get_all_users()
for page in snaide.get_all_pages():
	print page["name"]
g = snaide.get_all_pages()
