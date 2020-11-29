from django.shortcuts import render

posts = [
    {
        'author': 'TobyLerone',
        'title': 'Blog Post 1',
        'content': 'First Post!',
        'date_posted': 'November 29, 2019'
    },

    {
        'author': 'Toni Rigatoni',
        'title': 'Blog Post 2',
        'content': 'Second Post!',
        'date_posted': 'November 29, 2019'
    }
]


def home(request):
    context = {
        'posts': posts,
    }

    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
