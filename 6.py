import snaide

def get_esai_user (user_name, user_id):
	status_weight_factor = 0.5
	likes_weight_factor  = 0.3
	events_weight_factor = 0.2

	# calculating status factor
	status_count_of_user = snaide.get_statuses_count_by (user_name, user_id)
	total_status_count = snaide.get_all_statuses_count()
	comment_count_of_user = len ( snaide.get_comments_by(user_name, user_id) )
	total_comment_count = snaide.get_all_comments_count()

	status_factor = (status_count_of_user + comment_count_of_user)/float(total_status_count + total_comment_count) * 100 * status_weight_factor

	# calculating likes factor
	total_status_likes_count = snaide.get_all_status_likes_count()
	status_id_list = snaide.get_statuses_by (user_name, user_id)
	status_likes_count_user = 0
	for status_id in status_id_list:
		status_likes_count_user = status_likes_count_user + snaide.get_likes_on_single_status(status_id)

	likes_factor = ( status_likes_count_user/float(total_status_likes_count) ) * 100 * likes_weight_factor


	#calculating the event factor
	# this is partially done..
	# or do it the way it pleases you
	event_id_list = snaide.get_events_attended_by(user_name , user_id)
	event_attendees_count = 0
	for event_id in event_id_list:
		event_attendees_count = event_attendees_count + snaide.get_event_attendees_count(None, event_id)

	events_factor = 25

	return status_factor + likes_factor + events_factor


print get_esai_user(None, 48154)
print get_esai_user("esai", None)