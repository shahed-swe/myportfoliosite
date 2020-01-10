from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
# Create your views here.
from .models import BlogPost
from .forms import BlogPostModelForm
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

# GET - Retrieve / List
# POST - Create / Update /Delete

def blog_post_list_view(request):
    # list out objects
    #could be search
    # qs = BlogPost.objects.filter(title__icontains = "hello") #for search query
    qs = BlogPost.objects.all() #queryset -> list of python object
    template_name = 'blog/list.html'
    context = {'object_list':qs,"title": "Blog"}
    return render(request, template_name, context)

# @login_required
@staff_member_required
def blog_post_create_view(request):
    #create objects
    # ? use a form
    form = BlogPostModelForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = BlogPostModelForm()
    template_name = "blog/take_form.html"
    context = {"title":"New blog",'form': form}
    return render(request, template_name, context)


def blog_post_detail_view(request,post_slug):
    #1 object -> detail view
    obj = get_object_or_404(BlogPost, slug=post_slug)
    template_name = 'blog/detail.html'
    context = {"object": obj,"title":"Blog"}
    return render(request, template_name, context)

def blog_post_update_view(request, post_slug):
    obj = get_object_or_404(BlogPost, slug=post_slug)
    form = BlogPostModelForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
    template_name = 'blog/take_form.html'
    context = {'form': form, "title": f"update {obj.title}"}
    return render(request, template_name, context)

def blog_post_delete_view(request,post_slug):
    obj = get_object_or_404(BlogPost, slug=post_slug)
    template_name = 'blog/delete.html'
    if request.method == 'POST':
        obj.delete()
        return redirect("/blog")
    context = {"object":obj,"title":"Blog"}
    return render(request, template_name, context)