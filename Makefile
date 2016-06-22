migrate:
	- python wpsblog/manage.py makemigrations user posts bitly wpsblog 
	- python wpsblog/manage.py migrate
