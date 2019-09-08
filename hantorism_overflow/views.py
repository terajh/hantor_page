from common_hantorism.models import HantorismOverflow, HantorismOverflowAnswer,HantorismOverflowAnswerComment, HantorismUser
from rest_framework import viewsets
from django.shortcuts import render, render_to_response,redirect
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

rowsPerPage = 10


class ViewSet(viewsets.ModelViewSet):
    def overflow_list(self, request):
        current_page = request.GET.get('current_page','1')
        cur=int(current_page)
        overflows = HantorismOverflow.objects

        filter_params=dict()
        if request.GET.get('search'):
            search = request.GET.get('search')
            overflows = overflows.filter(title__contains=search).order_by('-created_date')
            filter_params['search'] = search

        overflows = overflows.order_by('-created_date')[(cur-1)*10:cur*10]
        totalCnt=HantorismOverflow.objects.all().count()

        pagingHelperIns = pagingHelper();
        total_page_list = pagingHelperIns.getTotalPageList(totalCnt,rowsPerPage)
        return render(request, 'overflow_list.html', {'overflow_list': overflows,
                                                  'filter_params': filter_params,
                                                      'current_page':cur})

    def create(self, request):
       redirect('/overflows')

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

def overflowWrite(request):
    return render(request, 'overflow_write.html')

@csrf_exempt
@login_required
def doOverflow(request):
    p=HantorismOverflow(user_info_id=request.user.id,
                    name=request.user.username,
                    title=request.POST['title'],
                    body=request.POST['body'])
    p.save()
    url='/overflows?current_page=1'
    return redirect(url)

def overflowView(request):
    pk=request.GET['overflow_id']
    current_page = request.GET.get('current_page','1')
    cur=int(current_page)
    searchStr=request.GET.get('search','')

    overflow_data=HantorismOverflow.objects.get(id=pk)
    HantorismOverflow.objects.filter(id=pk).update(view_count=overflow_data.view_count+1)
    overflow_data=HantorismOverflow.objects.get(id=pk)
    overflow_answer = HantorismOverflowAnswer.objects.filter(overflow_id=pk).order_by('-state')
    return render(request,'overflow_view.html', {'overflow_id': request.GET['overflow_id'],
                                             'overflow_data':overflow_data,
                                             'overflow_answer':overflow_answer,
                                                'current_page':cur,
                                                 'search':searchStr})

def overflowSearch(request):
    searchStr=request.GET['searchStr']
    page_for_view=request.GET['page_for_view']

    totalCnt=HantorismOverflow.objects.filter(title__contains=searchStr).count()
    pagingHelperIns=pagingHelper()
    total_page_list=pagingHelperIns.getTotalPageList(totalCnt,rowsPerPage)
    overflow_list=HantorismOverflow.objects.filter(title__contains=searchStr).order_by('-created_date')

    return render(request,'overflow_search.html',{'overflow_list':overflow_list,
                                              'totalCnt':totalCnt,
                                              'page_for_view':page_for_view,
                                              'searchStr':searchStr,
                                              'total_page_list':total_page_list})


def overflowModify(request):
    overflow_id=request.GET['overflow_id']
    current_page = request.GET['current_page']
    searchStr=''
    if request.GET['search']:
        searchStr=request.GET['search']
    overflow_data=HantorismOverflow.objects.get(id=overflow_id)
    return render(request,'overflow_modify.html',{'overflow_id':overflow_id,
                                              'current_page':current_page,
                                              'search':searchStr,
                                              'overflow_data':overflow_data})

@csrf_exempt
@login_required
def updateOverflow(request):
    overflow_id=request.POST['overflow_id']
    current_page=request.POST['current_page']
    searchStr=request.POST['search']

    HantorismOverflow.objects.filter(id=overflow_id).update(
        title=request.POST['title'],
        body=request.POST['body']
    )
    url='/overflow_view/?overflow_id='+str(overflow_id)+'&search='+searchStr
    return redirect(url)

def overflowDelete(request):
    overflow_id=request.GET['overflow_id']
    current_page=request.GET['current_page']

    d=HantorismOverflow.objects.get(id=overflow_id)
    d.delete()

    totalCnt=HantorismOverflow.objects.all().count()
    pagingHelperIns=pagingHelper()

    total_page_list=pagingHelperIns.getTotalPageList(totalCnt,rowsPerPage)
    if int(current_page) in total_page_list:
        pass
    else:
        current_page=int(current_page)-1

    url='/overflows?current_page='+str(current_page)
    return redirect(url)

@csrf_exempt
def titleSearch(request):
    searchStr=request.POST['searchStr']

    url='/overflow_search?page_for_view=1&searchStr='+searchStr
    return redirect(url)

@csrf_exempt
@login_required
def create_answer(request):
    answer_body = request.POST['body']
    overflow_id = request.POST['overflow_id']
    current_page = request.POST['current_page']
    searchStr=request.POST['search']
    user_id = request.user.id
    user = HantorismUser.objects.filter(user_id=user_id).first()
    HantorismOverflowAnswer.objects.create(user_info_id=user.id,
                                        overflow_id=overflow_id,
                                        body=answer_body)

    url = '/overflow_view/?overflow_id=' + str(overflow_id)+'&current_page='+current_page+'&search='+searchStr
    return redirect(url)

@login_required
def overflowSelect(request):
    answer_id=request.GET['answer_id']
    overflow_id=request.GET['overflow_id']
    current_page = request.GET['current_page']
    searchStr=request.GET['search']
    HantorismOverflowAnswer.objects.filter(id=answer_id).update(
        state=True
    )
    HantorismOverflow.objects.filter(id=overflow_id).update(
        state=True
    )
    url='/overflow_view/?overflow_id='+str(overflow_id)+'&current_page='+current_page+'&search='+searchStr
    return redirect(url)