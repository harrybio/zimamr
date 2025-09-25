import os
from django.core.wsgi import get_wsgi_application

# Use production settings for deployment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'zimamr.settings_deploy')

application = get_wsgi_application()
