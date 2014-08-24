import snaide

maximum = 0
events = snaide.get_all_events()

for event in events:
	attendees = snaide.get_event_attendees_count(None, event)
	if maximum < attendees:
		maximum = attendees
		e = event

print "Most Popular Event : "+snaide.get_event_title(e)