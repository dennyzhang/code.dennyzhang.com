all:refresh_link

refresh: refresh_md refresh_link

my_test:
	bash automate.sh my_test

refresh_link:
	bash automate.sh refresh_link
