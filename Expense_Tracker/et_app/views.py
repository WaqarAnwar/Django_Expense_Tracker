from django.shortcuts import render
from django.http.response import HttpResponse, JsonResponse
from .models import Entry
from .forms import EditForm, AddForm
from django.shortcuts import redirect

def index(request):
    all_data = Entry.objects.all()
    total_cash_in = sum([entry.amount for entry in Entry.objects.filter(options = 'cash_in')])
    total_cash_out = sum([entry.amount for entry in Entry.objects.filter(options = 'cash_out')])
    context = {"all_data": all_data}
    context['total_cash_in'] = total_cash_in
    context['total_cash_out'] = total_cash_out
    context['net_balance'] = total_cash_in - total_cash_out
    return render(request, 'main.html', context)

def edit(request, id):
    to_edit = Entry.objects.get(pk = id)
    context = {}
    form = EditForm(instance = to_edit)
    context['form'] = form
    return render(request, 'edit.html',context)

def save_edit(request, id):
    to_edit = Entry.objects.get(pk = id)

    if request.method == "POST":
        form = EditForm(request.POST, instance=to_edit)
        if form.is_valid():
            form.save()
        else:
            print("form invalid")
    else:
        form = EditForm()

    return redirect('/')

def add_page(request):
    form = AddForm()
    context = {}
    context['form'] = form

    return render(request, 'add.html', context)

def add(request):
    if request.method == 'POST':
        form = AddForm(request.POST)
        if form.is_valid:
            form.save()
    else:
        form = AddForm()

    return redirect('/')

def delete(request, id):
    Entry.objects.get(pk = id).delete()

    return redirect('/')