import snaide
graph_db, cur1, cur2, cur3, cur4, cur5 = snaide.init("localhost", "root", "", "elgg", "http://localhost:7474/db/data/")
user = snaide.get_one_user(graph_db, "vikyath", None)
print user
print

a = [1, 2, 3, 4, 5]

for i in a:
  print i