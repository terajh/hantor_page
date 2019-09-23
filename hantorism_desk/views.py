import io

import xlsxwriter
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render

from common_hantorism.models import HantorismDesk
from common_hantorism.models import HantorismUser


def dodesk(request):
    hantorism_desk = HantorismDesk.objects.all()
    if (request.method == 'GET'):
        render(request, 'desk.html')
    if (request.method == 'POST'):
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


@login_required()
def desk_list(request):
    current_user = HantorismUser.objects.get(user=request.user)
    permission = current_user.is_admin
    if (request.method == 'GET'):
        desk_members = HantorismDesk.objects.all()
        context = {'desk_members': desk_members, 'permission': permission}
        return render(request, 'desk_list.html', context)


def excel_export(request):
    output = io.BytesIO()
    desk_members = HantorismDesk.objects.all()
    desk_excel = xlsxwriter.Workbook(output)
    excel = desk_excel.add_worksheet()
    if (request.method == 'GET'):
        for member in desk_members:
            excel.write(member.id - 1, 0, member.name)
            excel.write(member.id - 1, 1, member.student_number)
            excel.write(member.id - 1, 2, member.birthday)
            excel.write(member.id - 1, 3, member.phone_number)
            excel.write(member.id - 1, 4, member.major)

    desk_excel.close()
    output.seek(0)
    filename = 'desk_list.xlsx'
    response = HttpResponse(output.read(),
                            content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    return response
