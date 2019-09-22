from common_hantorism.models import HantorismPost, HantorismPostComment, HantorismUser
from rest_framework import viewsets
from django.shortcuts import render, render_to_response,redirect
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
import math

rowsPerPage = 10


class ViewSet(viewsets.ModelViewSet):
    def post_list(self, request):
        current_page = request.GET.get('current_page','1')
        cur=int(current_page)
        posts = HantorismPost.objects

        filter_params=dict()
        if request.GET.get('category'):
            category = request.GET.get('category')
            posts = posts.filter(category=category)
            filter_params['category'] = category

        if request.GET.get('search'):
            search = request.GET.get('search')
            posts = posts.filter(title__contains=search).order_by('-created_date')
            filter_params['search'] = search

        posts = posts.order_by('-created_date')[(cur-1)*10:cur*10]
        paginator = Paginator(posts, 2);
        page = 1
        if request.GET.get('page'):
            page = request.GET.get('page')
        posts = paginator.get_page(page)

        page_range = 5
        current_block = math.ceil(int(page)/page_range)
        start_block = (current_block-1) * page_range
        end_block = start_block + page_range
        p_range = paginator.page_range[start_block:end_block]
        print(p_range)

        return render(request, 'post_list.html', {'post_list': posts,
                                                  'filter_params': filter_params,
                                                  'p_range': p_range,
                                                  })

    def create(self, request):
       redirect('/posts')


def postWrite(request):
    return render(request, 'post_write.html')


@csrf_exempt
@login_required
def doPost(request):
    p = HantorismPost(user_info_id=request.user.id,
                    name=request.user.username,
                    title=request.POST['title'],
                    body=request.POST['body'],
                    category=request.POST['category'])
    p.save()

    url = '/post_view?post_id=' + str(p.id)
    return redirect(url)

def postView(request):
    pk=request.GET['post_id']
    current_page = request.GET.get('current_page','1')
    cur=int(current_page)
    category=request.GET.get('category','')
    searchStr=request.GET.get('search','')

    post_data=HantorismPost.objects.get(id=pk)
    HantorismPost.objects.filter(id=pk).update(view_count=post_data.view_count+1)
    post_data=HantorismPost.objects.get(id=pk)
    post_comment = HantorismPostComment.objects.filter(post_id=pk)
    return render(request,'post_view.html', {'post_id': request.GET['post_id'],
                                             'current_page':cur,
                                             'category':category,
                                             'search':searchStr,
                                             'post_data':post_data,
                                             'post_comment':post_comment})


def postModify(request):
    post_id = request.GET['post_id']
    post_data = HantorismPost.objects.get(id=post_id)
    return render(request,'post_modify.html',{'post_id':post_id,
                                              'post_data':post_data})

@csrf_exempt
@login_required
def updatePost(request):
    post_id=request.POST['post_id']

    HantorismPost.objects.filter(id=post_id).update(
        title=request.POST['title'],
        body=request.POST['body']
    )
    url='/post_view/?post_id='+str(post_id)
    return redirect(url)

def postDelete(request):
    post_id=request.GET['post_id']

    d=HantorismPost.objects.get(id=post_id)
    d.delete()

    url='/posts/'
    return redirect(url)


@csrf_exempt
@login_required
def create_comment(request):
    comment_context = request.POST['context']
    post_id = request.POST['post_id']
    category = request.POST['category']
    current_page = request.POST['current_page']
    searchStr=request.POST['search']
    user_id = request.user.id
    user = HantorismUser.objects.filter(user_id=user_id).first()
    HantorismPostComment.objects.create(user_info_id=user.id,
                                        post_id=post_id,
                                        context=comment_context)

    url = '/post_view/?post_id='+ str(post_id) +'&category='+category+'&current_page='+current_page+'&search='+searchStr
    return redirect(url)
