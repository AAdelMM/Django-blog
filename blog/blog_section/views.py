from django.shortcuts import render

posts = [
    {'title':'Blog Post1',
    'author':'Ahmed Adel',
    'content':'This doing by my self',
    'date':'18 oct 2022'},

    {'title':'Blog Post2',
    'author':'Mohammed Ahmed',
    'content':'if this work',
    'date':'22 oct 2022'},

    {'title':'Blog Post3',
    'author':'ali ahmed',
    'content':'i will celebrate',
    'date':'15 oct 2022'},
]


def home(request):
    context = {'posts' : posts}
    return render(request,'blog/home.html', context)


def about(request):
    return render(request,'blog/about.html')
