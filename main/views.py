from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt

import json
DB=settings.DB_JSON

def readDB(filename=DB):
    with open(filename,mode='r') as j:
        data=json.load(j)

    return data
def writeDB(obj,filename=DB):
    with open(filename,mode='r') as j:
        data=json.load(j)
        temp=data['database']["pro"]
        temp.append(obj)

    with open(filename,mode='w') as f:
        json.dump(data,f)

#httpresponse converts the code passed into a page
# Create your views here.
def login(request):
    if request.method=="POST":
        dicobj=json.load(request.body)
        if(dicobj['add']=='true'):
            o=dicobj['obj']
            writeDB(o)

        return HttpResponse('<h1>post<h1>')       

def register(request):
    # if request.method=="GET":
    data=json.load(request.body)
    temp=data['database']["pro"]
    res={'pro':temp}
    print(data)
    return JsonResponse(res)
    

        
    

        
