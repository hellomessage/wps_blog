url(r'^(?P<post_id>\d+)/edit/$', edit, name="edit"),
url(r'^(?P<post_id>\d+)/update/$' update, name="update")
url(r'^(?P<post_id>\d+/delete/$' delete, name="delete")

url(r'(?P<post_id>\d+)/comments/create/$', comments_create, name="comments-create")
