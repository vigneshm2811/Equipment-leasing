from django.shortcuts import render, HttpResponse, redirect
from .models import lessor, container,lesse, leasinglist


# Create your views here.
def mainpage(request):
    return render(request, 'mainpage.html')


def adminlogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username == 'admin' and password == 'admin':
            return render(request, 'adminoperation.html')

        else:
            return HttpResponse('Invalid User')

    return render(request, 'admin.html')


def lessorlogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            lessor.objects.get(username=username, password=password, status=True)
            return redirect('/lessordatas')
        except:
            return HttpResponse("Invalid Password or Username")
    return render(request, 'lessor.html')


def registers(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        username = request.POST.get('username')
        password = request.POST.get('password')
        users = lessor()
        users.name = name
        users.username = username
        users.password = password
        users.save()
    return render(request, 'register.html')


def lessordatas(request):
    if request.method == 'POST':
        container_id = request.POST.get('container_id')
        container_type = request.POST.get('container_type')
        container_history = request.POST.get('container_history')
        rate = request.POST.get('rate')
        data = container()
        data.container_id = container_id
        data.container_history = container_history
        data.container_type = container_type
        data.rate = rate
        data.save()
    return render(request, 'lessor data.html')

def lesseregister(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        username = request.POST.get('username')
        password = request.POST.get('password')
        users = lesse()
        users.name = name
        users.username = username
        users.password = password
        users.save()
    return render(request, 'lesseregister.html')

def lesselogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            lesse.objects.get(username=username, password=password, status=True)
            return redirect('/lesseview')
        except:
            return HttpResponse("Invalid Password or Username")
    return render(request, 'lesselogin.html')


def pending(request):
        details = lessor.objects.filter(status=False)
        return render(request, 'pendinglist.html', {'value': details})

def update(request,id):
    data = lessor.objects.get(id=id)
    data.status = True
    data.save()
    return redirect('/pending')

def approved(request):
    details = lessor.objects.filter(status=True)
    return render(request, 'approve.html', {'value': details})

def lessepending(request):
    details = lesse.objects.filter(status=False)
    return render(request, 'lessepending.html', {'value': details})

def lesseupdate(request,id):
    data = lesse.objects.get(id=id)
    data.status = True
    data.save()
    return redirect('/lessepending')

def lesseapproved(request):
    details = lesse.objects.filter(status=True)
    return render(request, 'lesseapprove.html', {'value': details})

def lesseview(request):
    datas = container.objects.all()
    return render(request, 'lesseview.html', {'value': datas})

def orderlesse(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        address = request.POST.get('address')
        container_id = request.POST.get('container_id')
        years = request.POST.get('years')
        list = leasinglist()
        cont = container()
        list.name = name
        list.address = address
        list.containers_id = container_id
        list.years = years
        list.save()
        return HttpResponse("Wait for lessor Approval")
    return render(request, 'orderlesse.html')

def approveorder(request):
    list = leasinglist.objects.all()
    return render(request,'approve order.html', {'value':list})

def total(request,id):
    data =  [d.containers_id for d in leasinglist.objects.all()]
    years = data.years
