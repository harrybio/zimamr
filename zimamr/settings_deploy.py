import os
import dj_database_url

DATABASES = {
    'default': dj_database_url.config(
        default=os.environ.get('DATABASE_URL')
    )
}

DEBUG = False
ALLOWED_HOSTS = ['*']  # Replace with Render URL later
SECRET_KEY = os.environ.get('SECRET_KEY', 'your-default-secret')
