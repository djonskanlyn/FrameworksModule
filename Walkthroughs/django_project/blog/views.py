from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.views.generic import ListView, DetailView, CreateView

# Create your views here.
def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html' #<app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']

class PostDetailView(DetailView):
    model = Post  

class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'content']
     
    #Overriding form_valid method 
    def form_valid(self, form):
        form.instance.author = self.request.user # Set the author on the form
        return super().form_valid(form) # Validate form by running form_valid method from parent class.


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
