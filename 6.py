import snaide

def get_esai_user (user_name, user_id):
	status_weight_factor = 0.5
	likes_weight_factor  = 0.2
	events_weight_factor = 0.3

	# calculating status factor
	status_counts_of_user = snaide.get_statuses_count_by (user_name, user_id)
	friends_count_of_user = snaide.get_all_friends_count(user_name, user_id)
	friends_count_with_less_statuses = 0
	friends_id_list =  snaide.get_all_friends(user_name, user_id)
	for friend_id in friends_id_list:
		status_count_of_friend = snaide.get_statuses_count_by (None, friend_id)
		if (status_count_of_friend < status_counts_of_user):
			friends_count_with_less_statuses = friends_count_with_less_statuses + 1

	if friends_count_of_user == 0:
	  status_factor = 0
	else:
		status_factor = (friends_count_with_less_statuses/friends_count_of_user) * 100 * status_weight_factor

	# calculating likes factor
	status_list = snaide.get_statuses_by (user_name, user_id)
	status_likes_count = 0
	print status_list
	for status in status_list:
		status_likes_count = status_likes_count + snaide.get_likes_on_single_status(status)
	if friends_count_of_user:
	  average_likes_per_friend = 0
	else:
		average_likes_per_friend = status_likes_count/friends_count_of_user
	friends_count_with_less_likes = 0
	for friend_id in friends_id_list:
		friend_status_list = snaide.get_statuses_by(None , friend_id)
		friend_status_likes_count = 0
		for status in friend_status_list:
			friend_status_likes_count = friend_status_likes_count + snaide.get_likes_on_single_status(status)
		if (friend_status_likes_count <= status_likes_count and friend_status_likes_count <= average_likes_per_friend):
			friends_count_with_less_likes = friends_count_with_less_likes + 1

	if friends_count_of_user == 0:
	  likes_factor = 0
	else:
		likes_factor = (friends_count_with_less_likes/friends_count_of_user) * 100 * likes_weight_factor

	#calculating the event factor
	# this is partially done..
	# or do it the way it pleases you
	#event_id_list = get_events_attended_by(user_name , user_id)
	#event_attendees_count = 0
	#for event_id in event_id_list:
	#	event_attendees_count = event_attendees_count + get_event_attendees_count(None, event_id)

	events_factor = 35

	return status_factor + likes_factor + events_factor



print get_esai_user("Eileen Wehner ", None)