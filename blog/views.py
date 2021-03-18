from django.shortcuts import render

posts = [
    {
        'author': 'EvaristoFM',
        'title': 'Blog post 1',
        'content': 'Primeiro post',
        'date_posted': '17 Mar 2021'
    },
    {
        'author': 'Aryanne',
        'title': 'Blog post 1',
        'content': 'Primeiro post',
        'date_posted': '17 Mar 2021'
    },
    {
        'author': 'Juliooo',
        'title': 'Blog post 1',
        'content': 'Primeiro post',
        'date_posted': '17 Mar 2021'
    }
]


def home(request):
    return render(request, 'blog/home.html', {'posts': posts})

def about(request):
    return render(request, 'blog/about.html')