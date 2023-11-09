# Create your views here.
from django.shortcuts import render
from .models import Post
from .forms import PostForm

def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = PostForm()
    return render(request, 'create_post.html', {'form': form})

def search(request):
    if request.method == 'GET':
        query = request.GET.get('search_box')
        results = Post.objects.filter(title__icontains=query)
        return render(request, 'search_results.html', {'results': results})

def index(request):
    return render(request, 'index.html')
