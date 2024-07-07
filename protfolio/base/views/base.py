from django.shortcuts import render

def index(request):
    my_dict = {"insert_me": "I am from views.py"}
    return render(request,'base.html',context=my_dict)