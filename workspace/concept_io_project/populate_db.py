import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'concept_io_project.settings')

import django
django.setup()
from conceptio.models import Category, Project

def populate():

     technologyProjects=[
         {'project_id':1,'title':"The first technology project ever", 'desc':'This is a long description','cat':'Technology','tags':['java','modern'],'likes':12,'dislikes':2},
         {'project_id':2,'title':"My technology project", 'desc':'This is a very long description','cat':'Technology','tags':['C++','school'],'likes':2,'dislikes':4},
         {'project_id':3,'title':"The technology head", 'desc':'This is a moderately long description','cat':'Technology','tags':['python','modern'],'likes':10,'dislikes':0},
         {'project_id':4,'title':"Guide for tech bros", 'desc':'This is a short description','cat':'Technology','tags':['lifestyle','modern'],'likes':20,'dislikes':2},
     ]

     fantasyProjects=[
        {'project_id':5,'title':"The last fantasy project ever", 'desc':'Description has been lost','cat':'Fantasy','tags':['drawing','new'],'likes':12,'dislikes':5},
        {'project_id':6,'title':"The fantastic fantasy", 'desc':'Description has been found again','cat':'Fantasy','tags':['java','new'],'likes':32,'dislikes':3},
        {'project_id':7,'title':"Oh fatnsasy", 'desc':'Description available only in the morning','cat':'Fantasy','tags':['modern'],'likes':23,'dislikes':25},
        {'project_id':8,'title':"Fanta or cola", 'desc':'Description is extinct','cat':'Fantasy','tags':['novel','new'],'likes':36,'dislikes':0},

     ]
     utilityProjects=[
         {'project_id':9,'title':"Utilize your surroundings", 'desc':'Try to describe this','cat':'Utility','tags':['diagram',],'likes':15,'dislikes':4},
         {'project_id':10,'title':"Utilities in programming", 'desc':'Long dsrciption here','cat':'Utility','tags':['java','state'],'likes':10,'dislikes':24},
         {'project_id':11,'title':"How to utilize everything", 'desc':'No description for this','cat':'Utility','tags':['diagram','pseudocode'],'likes':53,'dislikes':5},
         {'project_id':12,'title':"Guide to utilites", 'desc':'Only one way to describe this','cat':'Utility','tags':['html','css'],'likes':1,'dislikes':8},
     ]

     artisticProjets=[
         {'project_id':13,'title':"Arts of the past", 'desc':'This project has been designed by me','cat':'Artistic','tags':['drawing','old'],'likes':23,'dislikes':8},
         {'project_id':14,'title':"Arts of the present", 'desc':'This project has been designed by nobody','cat':'Artistic','tags':['drawing','modern'],'likes':43,'dislikes':4},
         {'project_id':15,'title':"Arts of programing", 'desc':'One can only describe this','cat':'Artistic','tags':['java','jquery'],'likes':23,'dislikes':13},
         {'project_id':16,'title':"Arts in simple life", 'desc':'Simple as art','cat':'Artistic','tags':['html','ajax'],'likes':23,'dislikes':5},
     ]
     scifiProjects=[
         {'project_id':17,'title':"Aliens and stuff", 'desc':'Starring Will Smith','cat':'Sci-Fi','tags':['text','classic'],'likes':17,'dislikes':6},
         {'project_id':18,'title':"Plants and zombies", 'desc':'A family game','cat':'Sci-Fi','tags':['visualBasic',],'likes':37,'dislikes':8},
         {'project_id':19,'title':"Time freezing", 'desc':'A conspiracy theory','cat':'Sci-Fi','tags':['maths','physics'],'likes':72,'dislikes':9},
         {'project_id':20,'title':"Front to the past", 'desc':'The science of reverse','cat':'Sci-Fi','tags':['video',],'likes':34,'dislikes':4},
     ]

     categories = {'Technology':{'projects':technologyProjects},'Fantasy':{'projects':fantasyProjects},'Utility':{'projects':utilityProjects},'Artistic':{'projects':artisticProjets},'Sci-Fi':{'projects':scifiProjects}}

     for cat, cat_data in categories.items():
         c = add_cat(cat)
         for p in cat_data['projects']:
             add_page(c, p['title'], p['desc'],p['tags'],p['likes'],p['dislikes'])


     for c in Category.objects.all():
         for p in Project.objects.filter(category=c):
            print(f'- {c}: {p}')



def add_page(cat, title, desc,tags,likes,dislikes, views=0):
     p = Project.objects.get_or_create(category=cat, title=title)[0]
     p.desc=desc
     p.cat=cat
     p.tags=tags
     p.likes=likes
     p.dislikes=dislikes
     p.views=views
     p.save()
     return p

def add_cat(name):
    c = Category.objects.get_or_create(name=name)[0]
    c.save()
    return c

if __name__ == '__main__':
     print("Starting conceptio population..")
     populate()


