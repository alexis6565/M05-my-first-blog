from django.shortcuts import render
from django.utils import timezone
#include the code from model in models.py by typing the code on line 3
from .models import Post #the dot before models means current directory or application

# Create your views here.
#views connect models and templates 
#need to take the models we want to display in our post_list view and pass them to the template 


def post_list(request):
    #create a variable for our query set called posts/ name of queryset = posts
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts}) #render function has one parameter = request(everything from the user via the internet) and another giving the template file ('blog/post_list.html')
#created a def function called post_list that takes request and will return the value it gets from calling render function 
#render function will put together our template 


#go back to template and display the queryset





























































































