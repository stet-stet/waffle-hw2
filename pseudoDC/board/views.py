from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.urls import reverse
from django.views import generic
from .models import BlogPost


# Create your views here.

def four_oh_four(http_request):
    return render(http_request, 'board/PageDoesNotExist.html')


def Index(http_request):
    BList = get_list_or_404(BlogPost)
    return render(http_request, 'board/index.html', {"BlogPostList": BList})


def Read(http_request, post_id):
    B = get_object_or_404(BlogPost, pk=post_id)
    if B.private is True:
        return four_oh_four(http_request)
    else:
        return render(http_request, 'board/read.html', {"blogpost": B})


def Write(http_request):
    return render(http_request, 'board/write.html', {})


def Update(http_request, post_id):
    B = get_object_or_404(BlogPost, pk=post_id)
    if B.private is True:
        return four_oh_four(http_request)
    else:
        return render(http_request, 'board/modify.html', {"blogpost": B})


def Delete(http_request, post_id):
    B = get_object_or_404(BlogPost, pk=post_id)
    return render(http_request, 'board/delete.html', {"blogpost": B})


def Delete_action(http_request, post_id):
    B = get_object_or_404(BlogPost, pk=post_id)
    B.private = True
    return HttpResponseRedirect(reverse('board:index'))
