from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.urls import reverse
from django.views import generic
from django.utils import timezone
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


def Verify(http_request, post_id):
    B = get_object_or_404(BlogPost, pk=post_id)
    return render(http_request, 'board/verify.html', {"blogpost": B})


def Update(http_request, post_id, password):
    B = get_object_or_404(BlogPost, pk=post_id)
    if B.password != password:
        return four_oh_four(http_request)
    else:
        return render(http_request, 'board/modify.html', {"blogpost": B})


def Delete(http_request, post_id):
    B = get_object_or_404(BlogPost, pk=post_id)
    return render(http_request, 'board/delete.html', {"blogpost": B})

# Queries


def PostBlogpostQuery(http_request):
    B = BlogPost(
        subject=http_request.POST['subject'],
        text=http_request.POST['text'],
        password=http_request.POST['password'],
        author=http_request.POST['author'],
        pub_date=timezone.now(),
        last_modified=timezone.now(),
        private=False
    )
    B.save()
    return HttpResponseRedirect(reverse('board:read', args=(B.pk,)))


def HandleVerifyQuery(http_request, post_id):
    B = get_object_or_404(BlogPost, pk=post_id)
    if http_request.POST['password'] == B.password:
        return HttpResponseRedirect(reverse('board:update', args=(post_id, B.password)))
    else:
        return HttpResponseRedirect(reverse('board:index'))


def HandleUpdateQuery(http_request, post_id):
    B = get_object_or_404(BlogPost, pk=post_id)
    B.subject = http_request.POST['subject']
    B.text = http_request.POST['text']
    B.password = http_request.POST['password']
    B.author = http_request.POST['author']
    B.last_modified = timezone.now()
    B.save()
    return HttpResponseRedirect(reverse('board:read', args=(post_id,)))


def HandleDeleteQuery(http_request, post_id):
    B = get_object_or_404(BlogPost, pk=post_id)
    if http_request.POST['password'] == B.password:
        B.private = True
    B.save()
    return HttpResponseRedirect(reverse('board:index'))
