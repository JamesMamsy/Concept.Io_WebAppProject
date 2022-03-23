import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'concept_io_project.settings')

import django
django.setup()
from conceptio.models import Category, Project

def populate():

    categories = [{'name':'Technology'},{'name','Fantasy'},{'name':'Utlity'},{'name':'Artistic'},{'name':'Sci-Fi'}]

