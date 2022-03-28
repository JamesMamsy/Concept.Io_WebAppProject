import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'concept_io_project.settings')

import django
django.setup()
from conceptio.models import Category, Project, UserProfile, User

def populate():
    user_profiles = {'Tom':{'password':'12345678',
                            'first_name':'Tom',
                            'last_name':'Petty',
                            'email':'tom_petty@gmail.com',
                            'website':'www.heartbreakers.com',
                            'picture':'profile_images/tonpetty.jpg'},
                     'John':{'password':'87654321',
                             'first_name': 'Jonathan',
                             'last_name': 'Joestar',
                             'email': 'jojo@gmail.com',
                             'website': 'www.joestar.com',
                             'picture': 'profile_images/jojo.png'},
                     'Bob':{'password':'abcdefg',
                            'first_name': 'Bob',
                            'last_name': 'Bobbity',
                            'email': 'bobo@gmail.com',
                            'website': 'www.bobnbobbity.com',
                            'picture': 'profile_images/bobbob.png'},
                     'GioGio':{'password':'hijklmnop',
                               'first_name': 'Giorno',
                               'last_name': 'Giovanna',
                               'email': 'giogio@gmail.com',
                               'website': 'www.giogio.com',
                               'picture': 'profile_images/giogio.png'},
                     'Polnareff':{'password':'qrstup',
                                  'first_name': 'Jean Pierre',
                                  'last_name': 'Polnareff',
                                  'email': 'jppol@gmail.com',
                                  'website': 'www.michelpolnareff.com',
                                  'picture': 'profile_images/polnareff.png'},
                     'Rango':{'password':'wxyz',
                              'first_name': 'Rango',
                              'last_name': 'Depp',
                              'email': 'notjohnnydepp@gmail.com',
                              'website': 'www.rango.com',
                              'picture': 'profile_images/rango.jpg'}
                     }

    techno_projects = [{'creator':'Tom',
                        'title':'automatic disc thrower',
                        'desc':'throws discs really far',
                        'tags':'machine, discus, sports',
                        'likes':12},
                       {'creator': 'John',
                        'title': 'Useless Box',
                        'desc': 'box that is useless',
                        'tags': 'box, machine,fun,useless',
                        'likes': 40}
                       ]

    fantasy_projects = [{'creator':'Bob',
                        'title':'Dragon',
                        'desc':'fire breathing dragon',
                        'tags':'fire, cool, dragon',
                        'likes':6},
                       {'creator': 'Giorno',
                        'title': 'Swamp Rat',
                        'desc': 'a rat that lives in the swamp',
                        'tags': 'rat, mud, swamp, gross',
                        'likes': 71},
                        {'creator': 'Polnareff',
                         'title': 'Wizard',
                         'desc': 'a wizard on his tower',
                         'tags': 'wizard, magic, tower, miniature',
                         'likes': 80}
                       ]

    utility_projects = [{'creator':'Bob',
                        'title':'gear1',
                        'desc':'functioning gear',
                        'tags':'gear, machine',
                        'likes':12},
                        {'creator': 'Bob',
                         'title': 'gear2',
                         'desc': 'functioning gear',
                         'tags': 'gear, machine',
                         'likes': 14},
                       ]

    artistic_projects = [{'creator':'Rango',
                        'title':'A Lizard',
                        'desc':'a hawaiian shirt-wearing lizard. might be related to johnny depp.',
                        'tags':'lizard, shirt, movie ',
                        'likes':69}
                       ]

    scifi_projects = []

    categories = {'Technology':{'projects': techno_projects},
                  'Fantasy':{'projects':fantasy_projects},
                  'Utility':{'projects':utility_projects},
                  'Artistic':{'projects':artistic_projects},
                  'Sci-Fi':{'projects':scifi_projects}}

    for user, user_data in user_profiles.items():
        u = add_user(user, user_data['password'])
        add_userprofile(u, user_data['first_name'], user_data['last_name'], user_data['email'], user_data['website'], user_data['picture'])

    for cat, cat_data in categories.items():
        c = add_cat(cat)
        for p in cat_data['projects']:
            add_project(c, p['creator'], p['title'], p['desc'], p['tags'], p['likes'])

    for c in Category.objects.all():
        for p in Project.objects.filter(category = c):
            print(f'- {c}: {p}')

def add_user(user, password):
    u = User.objects.get_or_create(username = user)[0]
    u.password = password
    u.save()
    return u

def add_userprofile(user, first_name, last_name, email, website, picture):
    up = UserProfile.objects.get_or_create(user=user)[0]
    up.first_name = first_name
    up.last_name = last_name
    up.email = email
    up.website = website
    up.picture = picture
    up.save()
    return up

def add_cat(name):
    c = Category.objects.get_or_create(name=name)[0]
    c.save()
    return c

def add_project(category,creator,title,desc,tags,likes):
    p = Project.objects.get_or_create(cat= category, title=title, creator=creator)[0]
    p.desc = desc
    p.tags = tags
    p.likes = likes
    p.dislikes = dislikes
    p.save()
    return p

if __name__ == '__main__':
    print('Starting Population Script')
    populate()