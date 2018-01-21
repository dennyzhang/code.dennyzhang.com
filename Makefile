all:refresh_link

refresh: refresh_link refresh_md

refresh_link:
	bash automate.sh refresh_link
refresh_md:
	bash automate.sh refresh_md
