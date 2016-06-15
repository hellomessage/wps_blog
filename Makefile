migrate:
	- python wpsblog/manage.py makemigrations users postsbitly wpsblog 
	- python wpsblog/manage.py migrate
