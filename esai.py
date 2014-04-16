import snaide
for event in snaide.get_events_owned_by("esai", None):
  print event["name"]
