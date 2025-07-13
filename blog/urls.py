#importing django path function and all views from the blog application 

from django.urls import path 
from . import views 

# view is a place where we put "logic"of our application 
# views are placed in the views.py file in the blog folder 
#assigning a view called post list to the root URL
#URL pattern will match an empty string and the Django URL resolver will ignore the domain name that prefixes the full URL path 
#name post_list is url name that will ID the view and can be the same or different name from the view

#first url pattern
urlpatterns = [
    path('', views.post_list, name='post_list')
]

