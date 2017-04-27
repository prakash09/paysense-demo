from django.shortcuts import render
from django.http import HttpResponse,HttpRequest, Http404, HttpResponseRedirect
from django.shortcuts import redirect
from .models import Post
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.


def get_client_ip(request):
    ''' This method is for getting IP address of the user '''
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def listAllPosts(request):
    ''' Landing page. List all posts '''
    all_posts=Post.objects.all()
    return render(request,'blog/index.html',{'all_posts':all_posts})

@csrf_exempt
def deletePosts(request, post_id=None):
    ''' 
        For deleting posts. 
        Cases:
        1. When post_id is present. Get the post with that id and delete.
        2. When post_id is not present. Delete all posts.

    '''
    if request.method=='POST':
        if request.POST['token']=='123xyz':
            if post_id:
                Post.objects.filter(id=int(post_id)).delete()
            else:
                Post.objects.all().delete()
            return redirect('blog:list_all_posts')
        else:
            return HttpResponse(json.dumps({"status":"Incorrect token"}),status=401)
    else:
        return Http404()


def savePost(request):
    '''
        Save all posts.
    '''
    if request.method=='POST':
        try:
            post_text=request.POST['post_text']
            Post.objects.create(user_ip=get_client_ip(request),post_text=post_text)
            return redirect('blog:list_all_posts')
        except:
            return HttpResponse(json.dumps({"status":"Input not correct"}),status=400)
    else:
        return Http404()
