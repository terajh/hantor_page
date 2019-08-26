from common_hantorism.models import HantorismPost, HantorismPostComment, HantorismUser
from rest_framework import viewsets
from django.shortcuts import render, render_to_response,redirect
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

rowsPerPage = 10


class ViewSet(viewsets.ModelViewSet):
    def post_list(self, request):
        current_page = request.GET.get('current_page','1')
        cur=int(current_page)
        posts = HantorismPost.objects

        filter_params = dict()
        if request.GET.get('category'):
            category = request.GET.get('category')
            posts = posts.filter(category=category)
            filter_params['category'] = category

        if request.GET.get('search'):
            search = request.GET.get('search')
            posts = posts.filter(title__contains=search).order_by('-created_date')
            filter_params['search'] = search

        posts = posts.order_by('-created_date')[(cur-1)*10:cur*10]
        totalCnt=HantorismPost.objects.all().count()

        pagingHelperIns = pagingHelper();
        total_page_list = pagingHelperIns.getTotalPageList(totalCnt,rowsPerPage)
        return render(request, 'post_list.html', {'post_list': posts,
                                                  'filter_params': filter_params})

    def create(self, request):
       redirect('/posts')

class pagingHelper:
    def getTotalPageList(self, total_cnt,rowsPerPage):
        if total_cnt % rowsPerPage == 0:
            self.total_page = total_cnt/rowsPerPage
        else:
            self.total_page = total_cnt//rowsPerPage +1

        self.total_page_list=[]
        for i in range(int(self.total_page)):
            self.total_page_list.append(i+1)

        return self.total_page_list

    def __init__(self):
        self.total_page=0
        self.total_page_list=0

def postWrite(request):
    return render(request, 'post_write.html')

@csrf_exempt
@login_required
def doPost(request):
    p=HantorismPost(user_info_id=request.user.id,
                    name=request.user.username,
                    title=request.POST['title'],
                    body=request.POST['body'],
                    category=request.POST['category'])
    p.save()
    url='/posts?current_page=1'
    return redirect(url)

def postView(request):
    pk=request.GET['post_id']
    post_data=HantorismPost.objects.get(id=pk)
    HantorismPost.objects.filter(id=pk).update(view_count=post_data.view_count+1)
    post_data=HantorismPost.objects.get(id=pk)
    post_comment = HantorismPostComment.objects.filter(post_id=pk)
    return render(request,'post_view.html', {'post_id': request.GET['post_id'],
                                             'post_data':post_data,
                                             'post_comment':post_comment})

def postSearch(request):
    searchStr=request.GET['searchStr']
    page_for_view=request.GET['page_for_view']

    totalCnt=HantorismPost.objects.filter(title__contains=searchStr).count()
    pagingHelperIns=pagingHelper()
    total_page_list=pagingHelperIns.getTotalPageList(totalCnt,rowsPerPage)
    post_list=HantorismPost.objects.filter(title__contains=searchStr).order_by('-created_date')

    return render(request,'post_search.html',{'post_list':post_list,
                                              'totalCnt':totalCnt,
                                              'page_for_view':page_for_view,
                                              'searchStr':searchStr,
                                              'total_page_list':total_page_list})


def postModify(request):
    post_id=request.GET['post_id']
    current_page = request.GET['current_page']
    searchStr=request.GET['searchStr']
    post_data=HantorismPost.objects.get(id=post_id)
    return render(request,'post_modify.html',{'post_id':post_id,
                                              'current_page':request.GET['current_page'],
                                              'searchStr':request.GET['searchStr'],
                                              'post_data':post_data})

@csrf_exempt
@login_required
def updatePost(request):
    post_id=request.POST['post_id']
    current_page=request.POST['current_page']
    searchStr=request.POST['searchStr']

    HantorismPost.objects.filter(id=post_id).update(
        title=request.POST['title'],
        body=request.POST['body']
    )
    url='/post_view/?post_id='+str(post_id)
    return redirect(url)

def postDelete(request):
    post_id=request.GET['post_id']
    current_page=request.GET['current_page']

    d=HantorismPost.objects.get(id=post_id)
    d.delete()

    totalCnt=HantorismPost.objects.all().count()
    pagingHelperIns=pagingHelper()

    total_page_list=pagingHelperIns.getTotalPageList(totalCnt,rowsPerPage)
    if int(current_page) in total_page_list:
        pass
    else:
        current_page=int(current_page)-1

    url='/posts?current_page='+str(current_page)
    return redirect(url)

@csrf_exempt
def titleSearch(request):
    searchStr=request.POST['searchStr']

    url='/post_search?page_for_view=1&searchStr='+searchStr
    return redirect(url)

@csrf_exempt
@login_required
def create_comment(request):
    comment_context = request.POST['context']
    post_id = request.POST['post_id']
    user_id = request.user.id
    user = HantorismUser.objects.filter(user_id=user_id).first()
    HantorismPostComment.objects.create(user_info_id=user.id,
                                        post_id=post_id,
                                        context=comment_context)

    url = '/post_view/?post_id=' + str(post_id)
    return redirect(url)
