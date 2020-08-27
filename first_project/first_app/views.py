from django.shortcuts import render
from django.http import HttpResponse
#from first_app.models import User
# Create your views here.

def index(request):
    my_dict = {'insert_me': 'Hello I am from first_app/index.html'}
    return render(request, 'first_app/index.html',context=my_dict)
#settings nows about this directory because it was added to DIR []

def help(request):
    help_dict = {'help_insert': 'Hello I am from first_app/help.html'}
    return render(request, 'first_app/help.html',context=help_dict)

def images(request):
    images_insert = {'images_insert': 'Hello I am from Statis/images.html'}
    return render(request, 'first_app/images.html',context=images_insert)

def model_data(request):
    return render(request,'first_app/index.html')

#def users(request):

#    user_list = User.objects.order_by.('first_name')
#    user_dict = {'users':user_list}
#    return render(request,'first_app/users.html',context=user_dict)
