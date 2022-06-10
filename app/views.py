from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, redirect
from django.contrib.auth.decorators import login_required
from .models import Computer, Instance
from django.urls import reverse
from django.contrib import messages
from .forms import ComputerForm, InstanceForm
from django.db.models import Count
from django.contrib.auth.models import User

@login_required
def index(request):

    context = {
        'count_user_instances': Instance.objects.filter(is_active=True, user=request.user).count(),
        'user_instances': Instance.objects.filter(is_active=True, user=request.user),
        'count_computers': Computer.objects.filter(is_active=True).count(),
        'count_av_computers': Computer.objects.filter(is_active=True, is_available=True).count(),
        'users': User.objects.all(),
        'count_users': User.objects.all().count(),
    }
    return render(request, 'index.html', context)

@login_required
def reports(request):
    context = {}
    return render(request, "app/reports.html", context)
    

@login_required
def users(request):

    context = {
        'count_computers': Computer.objects.filter(is_active=True).count(),
        'users': User.objects.all(),
        'count_users': User.objects.all().count(),
    }
    return render(request, 'app/users.html', context)


def view_computers(request):
    return render(request, 'view_computers.html')

@login_required
def delete_computer(request, pk):
    delete_computer = Computer.objects.get(pk=pk)
    delete_computer.is_active = False
    delete_computer.save()
    messages.success(request, 'Deleted successfully')
    return HttpResponseRedirect(reverse('app:computers'))

@login_required
def update_computer(request, pk):
    context ={}
    computer = Computer.objects.filter(is_active=True)

    obj = get_object_or_404(Computer, pk=pk)

    form = ComputerForm(request.POST or None, instance = obj)
    if form.is_valid():
        form.save()
        messages.success(request, 'Editted successfully')
        return HttpResponseRedirect(reverse('app:computers'))
    context["form"] = form
    context["computer"] = computer
    return render(request, 'app/computers.html', context)

@login_required
def computers(request):
    computer = Computer.objects.filter(is_active=True)

    if request.method == 'POST':
        form = ComputerForm(request.POST)
        if form.is_valid():
            computer = form.save(commit=False)
            computer.save()
            messages.success(request, 'Form submission successful')
            form = ComputerForm()
            computer = Computer.objects.filter(is_active=True)
            return render(request, 'app/computers.html', {'computer': computer,'form': form})
    else:
        form = ComputerForm()
    return render(request, "app/computers.html", {'computer': computer,'form': form})

@login_required
def delete_instance(request, pk):
    delete_instance = Instance.objects.get(pk=pk)
    delete_instance.is_active = False
    delete_instance.save()

    computer = Computer.objects.get(pk=delete_instance.computer.pk)
    computer.is_available = True
    computer.save()

    messages.success(request, 'Disconnected successfully')
    return HttpResponseRedirect(reverse('app:instances'))

@login_required
def update_instance(request, pk):
    context ={}
    instance = Instance.objects.filter(is_active=True)

    obj = get_object_or_404(instance, pk=pk)

    form = InstanceForm(request.POST or None, instance = obj)
    if form.is_valid():
        form.user = request.user
        form.save()
        messages.success(request, 'Editted successfully')
        return HttpResponseRedirect(reverse('app:instances'))
    context["form"] = form
    context["instance"] = instance
    return render(request, 'app/instances.html', context)

@login_required
def instances(request):
    instance = Instance.objects.filter(is_active=True, user=request.user)
    admin_instance = Instance.objects.filter(is_active=True)

    if request.method == 'POST':
        form = InstanceForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()

            computer_pk = request.POST.get('computer', '')
            computer = Computer.objects.get(pk=computer_pk)
            computer.is_available = False
            computer.save()

            messages.success(request, 'Intance started successful')
            form = InstanceForm()
            instance = Instance.objects.filter(is_active=True)
            return render(request, 'app/instances.html', {'instance': instance,'form': form,'admin_instance': admin_instance})
    else:
        form = InstanceForm()
        form.fields['computer'].queryset = Computer.objects.filter(is_available=True)
        # form.fields['user'].queryset = User.objects.filter(username=request.user)
    return render(request, "app/instances.html", {'instance': instance,'form': form,'admin_instance': admin_instance})