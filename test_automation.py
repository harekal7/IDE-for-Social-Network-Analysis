import snaide

user_guid = 48158
event_guid = 59558
page_guid = 55418
blog_guid = 59555
user_id = 48158
user1_id = 48159
user2_id = 48158
group_guid = 52252
status_id = 59122
comment_id = 59125
group_id = 52252


print snaide.get_all_users()
print


print snaide.get_all_events()
print


print snaide.get_events_owned_by(None, user_guid)
print
	


print snaide.get_statuses_by(None, user_guid)
print


print snaide.get_comments_by(None, user_guid)
print

print snaide.get_group_members(None, group_guid)
print


print snaide.get_groups_owned_by (None, user_guid)
print


print snaide.get_all_pages()
print


print snaide.get_all_events()
print

print snaide.get_events_created_by(None, user_guid)
print


print snaide.get_event_attendees (None, event_guid)
print


print snaide.get_event_organizer (None, event_guid)
print


print snaide.get_event_date (None, event_guid)
print


print snaide.get_event_start_time (None, event_guid)
print	


print snaide.get_event_title (event_guid)
print

print snaide.get_event_attendees_count(None, event_guid)
print


print snaide.get_event_short_description(None, event_guid)
print


print snaide.get_event_description(None, event_guid)
print



print snaide.get_event_max_attendees(None, event_guid)
print


print snaide.get_event_end_registration_day(None, event_guid)
print


print snaide.get_event_fee(None, event_guid)
print


print snaide.get_event_contact_details(None, event_guid)
print


print snaide.get_event_venue(None, event_guid)
print


print snaide.get_event_location(None, event_guid)
print


print snaide.get_event_website(None, event_guid)
print

print snaide.get_event_twitter_hash(None, event_guid)
print


print snaide.get_event_location(None, event_guid)
print


print snaide.get_event_tags(None, event_guid)
print


print snaide.get_all_pages()
print


print snaide.get_page_likes_count (None, page_guid)
print


print snaide.get_pages_created_by (None, user_guid)
print


print snaide.get_pages_liked_by (None, user_guid)
print

print snaide.get_page_title (page_guid)
print


print snaide.get_page_created_date (None, page_guid)
print


print snaide.get_page_content(None, page_guid)
print


print snaide.get_page_tags(None, page_guid)
print


print snaide.get_page_container_group(None, page_guid)
print


print snaide.get_group_members(None, group_guid)	
print

print snaide.get_group_members_count(None, group_guid)
print


print snaide.get_groups_owned_by (None, user_guid)
print


print snaide.get_group_owner (None, group_guid)
print	


print snaide.get_group_name(group_guid)
print


print snaide.get_group_description(None, group_guid)
print	


print snaide.get_group_brief_description(None, group_guid)
print


print snaide.is_events_enabled_in_group(None, group_guid)
print


print snaide.is_blogs_enabled_in_group(None, group_guid)
print


print snaide.is_pages_enabled_in_group(None, group_guid)
print


print snaide.get_blog_likers (None, blog_guid)
print


print snaide.get_blog_commentators (None, blog_guid)
print


print snaide.get_blog_name (blog_guid)
print


print snaide.get_blog_description(None, blog_guid)		
print


print snaide.get_blog_tags(None, blog_guid)
print	


print snaide.get_blog_created_time(None, blog_guid)		
print	


print snaide.get_blogs_by_user (None, user_guid)
print


print snaide.get_blog_likers_count (None, blog_guid)
print


print snaide.get_blog_commentator_count (None, blog_guid)	
print


print snaide.get_all_users()
print


print snaide.get_all_users_count()
print


print snaide.get_user_name(user_guid)
print


print snaide.get_user_location (None, user_guid)
print


print snaide.get_user_brief_description (None, user_guid)
print


print snaide.get_user_contact_email (None, user_guid)
print


print snaide.get_user_telephone (None, user_guid)
print


print snaide.get_user_mobile_phone (None, user_guid)
print


print snaide.get_user_website (None, user_guid)
print


print snaide.get_user_interests (None, user_guid)
print


print snaide.get_user_skills (None, user_guid)
print


print snaide.get_user_last_login (None, user_guid)
print


print snaide.get_all_statuses()
print


print snaide.get_all_statuses_count()
print


print snaide.get_all_comments_count()
print


print snaide.get_all_events_count()
print


print snaide.get_all_pages_count()
print


print snaide.get_all_blogs_count()
print


print snaide.get_all_groups_count()
print


print snaide.get_all_status_likes_count()
print


print snaide.get_all_friends(None, user_guid)
print


print snaide.get_all_friends_count(None, user_guid)
print


print snaide.get_comments_by(None, user_guid)
print


print snaide.get_group_owner (None, group_guid)
print


print snaide.is_friend (user1_id, user2_id)
print


print snaide.is_user_member_of_group (user_id, group_id)
print


print snaide.groups_with_user_as_member (None, user_guid)
print

print snaide.get_all_blogs()
print


print snaide.get_statuses_count_by(None, user_guid)	
print


print snaide.get_likes_on_single_status (status_id)
print


print snaide.get_events_attended_by(None, user_guid)
print


print snaide.get_all_groups()
print


print snaide.get_status_message(status_id)
print


print snaide.get_comment_message(comment_id)
print
