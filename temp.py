import snaide

g = snaide.get_all_pages()

for i in g:
  print i["name"]