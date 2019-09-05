from django.shortcuts import render
from common_hantorism.models import HantorismDesk


def desk(request):
    hantorism_desk = HantorismDesk.objects.all()
    context = {'hantorism_desk': hantorism_desk}
    return render(request, 'desk.html', context )