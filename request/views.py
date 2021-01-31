from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from datetime import date, timedelta, datetime
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.core.mail import send_mail, send_mass_mail

from .forms import *

# Create your views here.
from .models import Item


@login_required
def req_new(request):
    context = {}
    sent = False
    nuid_r = request.user.id
    adminemail = "unofpinfo@gmail.com"
    email_r = request.user.email
    if request.method == "POST":
        # form = RequestForm(request.POST)
        # if form.is_valid():
        #    req = form.save(commit=False)

        #    req.save()
        #    req = Request.objects.filter()
        #    return render(request, 'req_list.html',
        #                  {'req': req})

        # nuid_r = request.user.id
        nuid_r = request.user.id
        bag = request.POST.get('bag')
        dt = request.POST.get('request_date')
        request_date = datetime.strptime(dt, '%Y-%m-%d').date()
        food_allergy = request.POST.get('food_allergy')
        additional_request = request.POST.get('additional_request')
        created = Request.objects.create(username_id=nuid_r, bag=bag, request_date=request_date,
                                         food_allergy=food_allergy,
                                         additional_request=additional_request, status='New')
        # username_r = request.user.id
        subject: str = "UNO Guest House Booking Request"
        message = f"Your booking request has been submitted \nOnce your request is processed you should recieve another email.\n\nThank you, UNOFP Staff. "
        message2 = f"New booking request has been submitted. Please fill in the requested items."
        msg1 = (subject, message, 'unofpinfo@gmail.com', [email_r])
        msg2 = (subject, message2, 'unofpinfo@gmail.com', [adminemail])
        send_mass_mail((msg1, msg2), fail_silently=False)
        sent = True
        reqs = Request.objects.filter(username=nuid_r)

        return render(request, 'submit_request.html', {'sent': sent, 'email_r': email_r})
    else:
        form = RequestForm()
    return render(request, 'add_req.html', {'form': form})


@login_required
def req_list(request):
    username_r = request.user.id
    reqs = Request.objects.filter(username=username_r)
    return render(request, 'req_list.html', {'reqs': reqs})


@login_required
def req_delete(request, pk):
    delreq = get_object_or_404(Request, pk=pk)
    delreq.delete()
    return redirect('req_list')


@login_required
def req_edit(request, pk):
    reqs = get_object_or_404(Request, pk=pk)
    if request.method == "POST":
        form = RequestForm(request.POST, instance=reqs)
        if form.is_valid():
            reqs = form.save()
            reqs.save()
            reqs = Request.objects.filter()
            return render(request, 'req_update_confirmation.html', {'form': form})
    else:
        # print("else")
        form = RequestForm(instance=reqs)
    return render(request, 'req_edit.html', {'form': form})


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return render(request, 'update_password_confirmation.html')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'change_password.html', {
        'form': form
    })


def admin_req_list(request):
    reqs = Request.objects.filter()
    return render(request, 'admin_req_list.html', {'reqs': reqs})


def req_approve(request, pk):

    reqs = get_object_or_404(Request, pk=pk)
    reqs.status = 'Ready'
    reqs.save()

    reqs = Request.objects.filter()
    return render(request, 'admin_req_list.html', {'reqs': reqs})


def req_delivered(request, pk):
    reqs = get_object_or_404(Request, pk=pk)
    reqs.status = 'Delivered'
    reqs.save()
    reqs = Request.objects.filter()
    return render(request, 'admin_req_list.html', {'reqs': reqs})


@login_required
def item_new(request):
    if request.method == "POST":
        form = ItemForm(request.POST)
        if form.is_valid():
            reqs = form.save(commit=False)

            reqs.save()
            reqs = Item.objects.filter()
            return render(request, 'item_list.html',
                          {'reqs': reqs})
    else:
        form = ItemForm()
    return render(request, 'add_item.html', {'form': form})


def item_list(request):
    reqs = Item.objects.filter()
    return render(request, 'item_list.html', {'reqs': reqs})


@login_required
def item_delete(request, pk):
    item = get_object_or_404(Item, pk=pk)
    item.delete()
    return redirect('item_list')


def item_edit(request, pk):
    reqs = get_object_or_404(Item, pk=pk)
    if request.method == "POST":
        form = ItemForm(request.POST, instance=reqs)
        if form.is_valid():
            reqs = form.save()

            reqs.save()
            reqs = Item.objects.filter()
            return render(request, 'item_list.html', {'reqs': reqs})
    else:
        # print("else")
        form = ItemForm(instance=reqs)
    return render(request, 'item_edit.html', {'form': form})
