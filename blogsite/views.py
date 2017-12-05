from django.shortcuts import render
from django.utils import timezone
from .models import Post
#  Create your views here.
def post_list(request):
    posts  = Post.objects.filter(created_on__lte=timezone.now()).order_by('created_on')
    return render(request, 'blogsite/post_list.html', {'posts': posts} )
