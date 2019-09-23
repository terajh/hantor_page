import math

from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets

from common_hantorism.models import HantorismOverflow, HantorismOverflowAnswer, HantorismUser

rowsPerPage = 10


class ViewSet(viewsets.ModelViewSet):
    def overflow_list(self, request):
        overflows = HantorismOverflow.objects.all()

        filter_params = dict()
        filter_params['search'] = ''
        if request.GET.get('search'):
            search = request.GET.get('search')
            overflows = overflows.filter(title__contains=search).order_by('-created_date')
            filter_params['search'] = search

        overflows = overflows.order_by('-created_date')
        paginator = Paginator(overflows, 10)
        page = 1
        if request.GET.get('page'):
            page = request.GET.get('page')
        posts = paginator.get_page(page)

        page_range = 5
        current_block = math.ceil(int(page) / page_range)
        start_block = (current_block - 1) * page_range
        end_block = start_block + page_range
        p_range = paginator.page_range[start_block:end_block]

        return render(request, 'overflow_list.html', {'overflow_list': posts,
                                                      'filter_params': filter_params,
                                                      'p_range': p_range,
                                                      })

    def create(self, request):
        return redirect('/overflows')


@login_required
def overflow_write(request):
    return render(request, 'overflow_write.html')


@csrf_exempt
@login_required
def do_overflow(request):
    hantor_user = HantorismUser.objects.get(user_id=request.user.id)
    p = HantorismOverflow.objects.create(user_info_id=hantor_user.id,
                                         name=request.user.username,
                                         title=request.POST['title'],
                                         body=request.POST['body'],)

    user_score = hantor_user.score
    HantorismUser.objects.filter(id=request.user.id).update(
        score=user_score + 1
    )
    url = '/overflow_view/?overflow_id=' + str(p.id)
    return redirect(url)


def overflow_view(request):
    pk = request.GET['overflow_id']
    filter_params = dict()
    filter_params['search'] = request.GET.get('search')
    filter_params['page'] = request.GET.get('page')

    overflow_data = HantorismOverflow.objects.get(id=pk)
    HantorismOverflow.objects.filter(id=pk).update(view_count=overflow_data.view_count + 1)
    overflow_data = HantorismOverflow.objects.get(id=pk)
    overflow_answer = HantorismOverflowAnswer.objects.filter(overflow_id=pk).order_by('-state')
    return render(request, 'overflow_view.html', {'overflow_id': request.GET['overflow_id'],
                                                  'overflow_data': overflow_data,
                                                  'overflow_answer': overflow_answer,
                                                  'filter_params': filter_params})


def overflow_modify(request):
    overflow_id = request.GET['overflow_id']
    overflow_data = HantorismOverflow.objects.get(id=overflow_id)
    if request.user != overflow_data.user_info.user:
        return redirect('/posts')
    return render(request, 'overflow_modify.html', {'overflow_id': overflow_id,
                                                    'overflow_data': overflow_data})


@csrf_exempt
@login_required
def update_overflow(request):
    overflow_id = request.POST['overflow_id']
    overflow_data = HantorismOverflow.objects.get(id=overflow_id)

    if request.user != overflow_data.user_info.user:
        return redirect('/overflows')

    overflow_data = HantorismOverflow.objects.filter(id=overflow_id)
    overflow_data.update(
        title=request.POST['title'],
        body=request.POST['body']
    )
    url = '/overflow_view/?overflow_id=' + str(overflow_id)
    return redirect(url)


def overflow_delete(request):
    overflow_id = request.GET['overflow_id']

    overflow_data = HantorismOverflow.objects.get(id=overflow_id)
    if request.user != overflow_data.user_info.user:
        return redirect('/overflows')

    overflow_data.delete()

    url = '/overflows/'
    return redirect(url)


@csrf_exempt
@login_required
def create_answer(request):
    answer_body = request.POST['body']
    overflow_id = request.POST['overflow_id']
    page = request.POST['page']
    print(page)
    search = request.POST['search']
    user_id = request.user.id
    user = HantorismUser.objects.filter(user_id=user_id).first()
    HantorismOverflowAnswer.objects.create(user_info_id=user.id,
                                           overflow_id=overflow_id,
                                           body=answer_body)

    url = '/overflow_view/?overflow_id=' + str(overflow_id) + '&search=' + search + '&page=' + page
    return redirect(url)


@login_required
def overflow_select(request):
    answer_user_id = request.POST['answer_user_id']
    answer_id = request.POST['answer_id']
    overflow_id = request.POST['overflow_id']
    page = request.POST['page']
    search = request.POST['search']
    HantorismOverflowAnswer.objects.filter(id=answer_id).update(
        state=True
    )
    HantorismOverflow.objects.filter(id=overflow_id).update(
        state=True
    )
    user_score = HantorismUser.objects.get(id=answer_user_id).score
    HantorismUser.objects.filter(id=answer_user_id).update(
        score=user_score + 10
    )
    url = '/overflow_view/?overflow_id=' + str(overflow_id) + '&search=' + search + '&current_page=' + page
    return redirect(url)
