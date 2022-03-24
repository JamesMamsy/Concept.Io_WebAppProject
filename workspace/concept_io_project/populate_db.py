import os
os.environ.setdefault('CONCEPT_SETTINGS_MODULE', 'concept_io_project.settings')

import django
django.setup()
from conceptio.models import Category, Project

def populate():
    user_profiles = [{'user':'',
                      'website':'',
                      'picture':''}
                     ]

    techno_projects = [{'creator':'',
                        'title':'',
                        'desc':'',
                        'tags':'',
                        'likes':'',
                        'dislikes':''}
                       ]

    fantasy_projects = [{'creator': '',
                        'title': '',
                        'desc': '',
                        'tags': '',
                        'likes': '',
                        'dislikes': ''}
                       ]

    utility_projects = [{'creator': '',
                        'title': '',
                        'desc': '',
                        'tags': '',
                        'likes': '',
                        'dislikes': ''}
                       ]

    artistic_projects = [{'creator': '',
                        'title': '',
                        'desc': '',
                        'tags': '',
                        'likes': '',
                        'dislikes': ''}
                       ]

    scifi_projects = [{'creator': '',
                        'title': '',
                        'desc': '',
                        'tags': '',
                        'likes': '',
                        'dislikes': ''}
                       ]

    categories = [{'Technology':{'projects': techno_projects}},
                  {'Fantasy':{'projects':fantasy_projects}},
                  {'Utility':{'projects':utility_projects}},
                  {'Artistic':{'projects':artistic_projects}},
                  {'Sci-Fi':{'projects':scifi_projects}}]

    for cat, cat_data in categories.items():
        c = add_cat(cat)
        for p in cat_data['projects']:
            add_project(c, p['creator'], p['title'], p['desc'], p['tags'], p['likes'], p['dislikes'])

    for c in Category.objects.all():
        for p in Project.objects.filter(category = c):
            print(f'- {c}: {p}')

def add_cat(name):
    c = Category.objects.get_or_create(name=name)[1]
    c.save()
    return c

def add_project(cat,creator,title,desc,tags,likes,dislikes):
    p.Project.objects.get_or_create(cat=cat, title=title, creator=creator)
    p.desc = desc
    p.tags = tags
    p.likes = likes
    p.dislikes = dislikes
