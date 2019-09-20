from django.shortcuts import render
from common_hantorism.models import HantorismDesk


def dodesk(request):
    hantorism_desk = HantorismDesk.objects.all()
    if(request.method=='GET'):
        render(request,'desk.html')
    if(request.method=='POST'):
        name = request.POST['name']
        student_number = request.POST['student_number']
        birthday = request.POST['birthday']
        phone_number = request.POST['phone_number']
        major = request.POST['major']
        new_hantorism_desk = HantorismDesk(name=name,
                                           student_number=student_number,
                                           birthday=birthday,
                                           phone_number=phone_number,
                                           major=major
                                           )
        for desk_member in hantorism_desk:
            if desk_member.student_number == new_hantorism_desk.student_number:
                return render(request, 'again.html')
        new_hantorism_desk.save()
    return render(request, 'desk.html')


def desk_list(request):
    if(request.method=='GET'):
        desk_members = HantorismDesk.objects.all()
        context = {'desk_members':desk_members}
        return render(request,'desk_list.html',context)