import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'concept_io_project.settings')

import django
django.setup()
from conceptio.models import Category, Project, UserProfile, User

def populate():
    users = {'Tom','John','Bob', 'conorbrown'}


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
                     'conorbrown':{'password':'wxyz',
                              'first_name': 'Rango',
                              'last_name': 'Depp',
                              'email': 'notjohnnydepp@gmail.com',
                              'website': 'www.rango.com',
                              'picture': 'profile_images/rango.jpg'}
                     }
    categories = ['Technology', 'Fantasy', 'Utility', 'Artistic', 'Sci-Fi']
    projects = [{'creator':'Tom',
                        'title':'automatic disc thrower',
                        'desc':'throws discs really far',
                        'cat': 1,
                        'tags':'machine discus sports'},



                       {'creator': 'Tom',
                        'title': 'Useless Box',
                        'desc': 'box that is useless',
                        'cat': 0,
                        'tags': 'box, machine,fun,useless'},



                        {'creator':'conorbrown',
                        'title':'Dragon',
                        'desc':'fire breathing dragon',
                         'cat': 2,
                        'tags':'fire, cool, dragon'},

                       {'creator': 'conorbrown',
                        'title': 'Swamp Rat',
                        'desc': 'a rat that lives in the swamp',
                        'cat': 3,
                        'tags': 'rat, mud, swamp, gross'},

                        {'creator': 'conorbrown',
                         'title': 'Wizard',
                         'desc': 'a wizard on his tower',
                         'cat': 1,
                         'tags': 'wizard, magic, tower, miniature'}]




    categories =['Technology','Fantasy','Utility','Artistic','Sci-Fi']

    for user in users:
        add_users(user, user_profiles[user])
    for cat in categories:
        Category.objects.get_or_create(name=cat)
        c = Category.objects.get(name=cat)
        c.save()
    for p in projects:
        add_project( p['creator'], p['title'], p['desc'],p['cat'], p['tags'])

def add_users(user, profile):
    User.objects.get_or_create(username=user)
    new_user = User.objects.get(username=user)
    UserProfile.objects.get_or_create(user=new_user)
    new_user_profile = UserProfile.objects.get(user=new_user)
    new_user_profile.password = profile['password']
    new_user_profile.email = profile['email']
    new_user_profile.website = profile['website']
    new_user_profile.picture = profile['picture']
    new_user_profile.first_name = profile['first_name']
    new_user_profile.last_name = profile['last_name']
    new_user_profile.save()
    new_user.save()

def add_cat(name):
    c = Category.objects.create(name=name)
    c.save()
    return c

def add_project(creator,title,desc,tags,cat):
    creator_user = User.objects.get(username=creator)
    Project.objects.get_or_create(creator=creator_user,title=title,desc=desc,tags=tags,cat=cat)
    p_new = Project.objects.get(creator=creator_user,title=title)
    p_new.save()


if __name__ == '__main__':
    print('Starting Population Script')
    populate()