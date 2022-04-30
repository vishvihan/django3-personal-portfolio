from django.shortcuts import render, get_object_or_404
from .models import Blogs

def all_blogs(request):
    # blogs = Blogs.objects.all()
    # i want to show the recent added blog and show only limited blogs
    # blogs = Blogs.objects.order_by('-date')[:2]


    blogs = Blogs.objects.order_by('-date')
    return render(request, 'blog/all_blogs.html', {'blogs':blogs})


def details(request,blog_id):
    blog = get_object_or_404(Blogs, pk=blog_id)
    return render(request,'blog/detail.html', {'blog':blog})
