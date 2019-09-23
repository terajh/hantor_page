import math

from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from django.core.exceptions import PermissionDenied

from common_hantorism.models import HantorismPost, HantorismPostComment, HantorismUser

rowsPerPage = 10


class ViewSet(viewsets.ModelViewSet):
    def post_list(self, request):
        posts = HantorismPost.objects.all()

        filter_params = dict()
        if request.GET.get('category'):
            category = request.GET.get('category')
            posts = posts.filter(category=category)
            filter_params['category'] = category

        if request.GET.get('search'):
            search = request.GET.get('search')
            posts = posts.filter(title__contains=search).order_by('-created_date')
            filter_params['search'] = search

        posts = posts.order_by('-up_post', '-created_date')
        paginator = Paginator(posts, 10)
        page = 1
        if request.GET.get('page'):
            page = request.GET.get('page')
        posts = paginator.get_page(page)

        page_range = 5
        current_block = math.ceil(int(page) / page_range)
        start_block = (current_block - 1) * page_range
        end_block = start_block + page_range
        p_range = paginator.page_range[start_block:end_block]

        return render(request, 'post_list.html', {'post_list': posts,
                                                  'filter_params': filter_params,
                                                  'p_range': p_range,
                                                  })

    def create(self, request):
        return redirect('/posts')


def post_write(request):
    return render(request, 'post_write.html')


@csrf_exempt
@login_required
def do_post(request):
    p = HantorismPost(user_info_id=request.user.id,
                      name=request.user.username,
                      title=request.POST['title'],
                      body=request.POST['body'],
                      category=request.POST['category'])
    p.save()

    if request.POST['category'] == 'notice':
        HantorismPost.objects.filter(id=p.id).update(
            up_post=True
        )

    url = '/post_view?post_id=' + str(p.id)
    return redirect(url)


def post_view(request):
    pk = request.GET['post_id']
    filter_params = dict()
    filter_params['category'] = request.GET.get('category')
    filter_params['search'] = request.GET.get('search')
    filter_params['page'] = request.GET.get('page')

    post_data = HantorismPost.objects.get(id=pk)
    HantorismPost.objects.filter(id=pk).update(view_count=post_data.view_count + 1)
    post_data = HantorismPost.objects.get(id=pk)
    post_comment = HantorismPostComment.objects.filter(post_id=pk)
    return render(request, 'post_view.html', {'post_id': request.GET['post_id'],
                                              'filter_params': filter_params,
                                              'post_data': post_data,

                                              'post_comment': post_comment})


@login_required()
def post_modify(request):
    post_id = request.GET['post_id']
    post_data = HantorismPost.objects.get(id=post_id)
    if request.user != post_data.user_info.user:
        raise PermissionDenied
    return render(request, 'post_modify.html', {'post_id': post_id,
                                                'post_data': post_data})


@csrf_exempt
@login_required
def update_post(request):
    post_id = request.POST['post_id']
    post_data = HantorismPost.objects.get(id=post_id)

    if request.user != post_data.user_info.user:
        return redirect('/posts')

    post_data = HantorismPost.objects.filter(id=post_id)
    post_data.update(
        title=request.POST['title'],
        body=request.POST['body']
    )
    url = '/post_view/?post_id=' + str(post_id)
    return redirect(url)


@csrf_exempt
@login_required
def post_delete(request):
    post_id = request.GET['post_id']

    post_data = HantorismPost.objects.get(id=post_id)
    if request.user != post_data.user_info.user:
        return redirect('/posts')

    post_data.delete()

    url = '/posts/'
    return redirect(url)


@csrf_exempt
@login_required
def create_comment(request):
    comment_context = request.POST['context']
    post_id = request.POST['post_id']
    category = request.POST['category']
    page = request.POST['page']
    search = request.POST['search']
    user_id = request.user.id
    user = HantorismUser.objects.filter(user_id=user_id).first()
    HantorismPostComment.objects.create(user_info_id=user.id,
                                        post_id=post_id,
                                        context=comment_context)

    url = '/post_view/?post_id=' + str(post_id) + '&category=' + category + '&search=' + search + '&page=' + page
    return redirect(url)
