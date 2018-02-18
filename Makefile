make db:
	DJANGO_SETTINGS_MODULE=back_to_back.settings.local ./back_to_back/manage.py makemigrations
	DJANGO_SETTINGS_MODULE=back_to_back.settings.local ./back_to_back/manage.py migrate

start:
	DJANGO_SETTINGS_MODULE=back_to_back.settings.local ./back_to_back/manage.py runserver

shell:
	DJANGO_SETTINGS_MODULE=back_to_back.settings.local ./back_to_back/manage.py shell_plus

test:
	cd back_to_back && DJANGO_SETTINGS_MODULE=back_to_back.settings.testing ./manage.py test 8000
