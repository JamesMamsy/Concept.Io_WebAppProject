import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango_with_django_project.settings')

import django
django.setup()
from conceptio.models import Category, Page

def populate():

    categories = [{'name':'Technology'},{'name','Fantasy'},{'name':'Utlity'},{'name':'Artistic'},{'name':'Sci-Fi'}]

