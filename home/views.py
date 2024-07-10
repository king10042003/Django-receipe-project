from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def home(request):

    peoples = [
        {'name':'Abhijeet Gupta','age': 26},
        {'name':'Rohan Sharma','age' : 28},
        {'name': 'Vicky Kausal','age': 24},
        {'name': 'Deepanshu Chourasiya','age':13},
        {'name': 'Sandeep','age':3}
    ]


    vegetable=['Pumpkin','Tomato','Potato']


    for people in peoples:
        print(people)


    return render(request , "home/index.html",context ={'page':'Django 2023 Tutorial','peoples' : peoples,'vegetable': vegetable})



def about(request):
    context = {'page' :'About'}
    return render(request,"home/about.html",context)


def contact(request):
    context = {'page' :'Contact'}
    return render(request,"home/contact.html",context)


def sucess_page(request):
    print("*" * 10)
    return HttpResponse("<h1>Hey this is a sucess pagae </h1>")