all:refresh-link

refresh-link:
	bash automate.sh refresh_link

refresh-wordpress:
	bash automate.sh refresh_wordpress

refresh-wordpress-all:
	MAX_DAYS=730 bash automate.sh refresh_wordpress

my_test:
	bash automate.sh my_test

git-pull:
	bash automate.sh git_pull

git-push:
	bash automate.sh git_push
