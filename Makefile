make migrate:
	DJANGO_SETTINGS_MODULE=back_to_back.settings.local ./back_to_back/manage.py makemigrations
	DJANGO_SETTINGS_MODULE=back_to_back.settings.local ./back_to_back/manage.py migrate

start:
	DJANGO_SETTINGS_MODULE=back_to_back.settings.local ./back_to_back/manage.py runserver_plus

shell:
	DJANGO_SETTINGS_MODULE=back_to_back.settings.local ./back_to_back/manage.py shell_plus

test:
	DJANGO_SETTINGS_MODULE=back_to_back.settings.testing ./back_to_back/manage.py test
