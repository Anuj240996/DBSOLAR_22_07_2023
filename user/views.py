from django.shortcuts import render, redirect

from django.contrib.auth import get_user, logout, login
#from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required

import customer
from customer.models import Customer
from dashboard.models import staff_Notification
from .models import User, Profile
from .forms import CreateUserForm, UserUpdateForm, ProfileUpdateForm
from django.contrib import messages

from .models import *

# Create your views here.


def register(request):
    count1 = staff_Notification.objects.filter(staff_id=request.user.id, status=False).count()
    notification1 = staff_Notification.objects.filter(staff_id=request.user.id, status=False).order_by('-created_at')
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        #Profile.objects.create(user=form)

        if form.is_valid():
            user = form.save(commit=False)
            user.is_staff = False
            user.is_active = True
            user.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account has been created for {username}  continue to Login')
            group = Group.objects.get(name='Customers')
            user.groups.add(group)
            return redirect('user-login')
    else:
        form = CreateUserForm()
        #Profile.objects.create(user=form)
    context = {
        'form': form,
        'profile': profile,
        'count1': count1,
        'notification1': notification1,
    }
    return render(request, 'user/register.html', context)

@login_required(login_url='user-login')
def add(request):
    error=""
    count1 = staff_Notification.objects.filter(staff_id=request.user.id, status=False).count()
    notification1 = staff_Notification.objects.filter(staff_id=request.user.id, status=False).order_by('-created_at')
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
    #    Profile.objects.create(user=form)

        if form.is_valid():

            user = form.save(commit=False)
            user.set_password(request.POST.get('password1'))

            user.is_staff = True
            user.is_active = True
            user.save()
           # print(user.first_name)
            # Add the user to the Customers group
            group = Group.objects.get(name='Customers')
            user.groups.add(group)
            username = form.cleaned_data.get('username')
            messages.success(request, f'{username}  Account Created Successfully!!')
            #print(user.password)
            return redirect('user-profile-update', user.id)
    else:
        form = CreateUserForm()
#        Profile.objects.create(user=form)
    context = {
        'form': form,
        'profile': profile,
        'count1': count1,
        'notification1': notification1,
    }
    return render(request, 'user/add.html', context)


# def profile(request,pk):
#     user = User.objects.get(id=pk)
#     item = Profile.objects.get(id=pk)
#     return render(request, 'user/profile.html', locals())

# def profile(request):
#     error = ""
#     count1 = staff_Notification.objects.filter(staff_id=request.user.id, status=False).count()
#     notification1 = staff_Notification.objects.filter(staff_id=request.user.id, status=False).order_by('-created_at')
#     user = request.user
#     employee = Profile.objects.get(customer=user)
#     customer = Customer.objects.get(new_customer=user)
#     if request.method == "POST":
#       o = request.POST['oldpassword']
#       n = request.POST['newpassword']
#     try:
#         u = User.objects.get(id=request.user.id)
#         if user.check_password(o):
#             u.set_password(n)
#             u.save()
#             error = "no"
#         else:
#             error = 'not'
#     except:
#         error = "yes"
#     return render(request, 'user/profile.html', locals())

def profile(request):
    error = ""
    count1 = staff_Notification.objects.filter(staff_id=request.user.id, status=False).count()
    notification1 = staff_Notification.objects.filter(staff_id=request.user.id, status=False).order_by('-created_at')
    user = request.user
    employee = Profile.objects.get(customer=user)

    # Check if the current user is a customer and retrieve their associated object
    try:
        customer = Customer.objects.get(new_customer=user)
    except Customer.DoesNotExist:
        customer = None

    if request.method == "POST":
        old_password = request.POST['oldpassword']
        new_password = request.POST['newpassword']

        # Change the user's password if the old password is correct
        try:
            u = User.objects.get(id=request.user.id)
            if user.check_password(old_password):
                u.set_password(new_password)
                u.save()
                error = "no"
            else:
                error = 'not'
        except User.DoesNotExist:
            error = "yes"

    return render(request, 'user/profile.html', locals())



def edit_profile(request):
    error = ""
    count1 = staff_Notification.objects.filter(staff_id=request.user.id, status=False).count()
    notification1 = staff_Notification.objects.filter(staff_id=request.user.id, status=False).order_by('-created_at')
    user = request.user
    employee = Profile.objects.get(customer=user)
    bgs = Profile._meta.get_field('bg').choices

    # Check if the current user is a customer and retrieve their associated object

    try:
        customer = Customer.objects.get(new_customer=user)
    except Customer.DoesNotExist:
        customer = None

    if request.method == "POST":
        em = request.POST.get('email')
        add = request.POST.get('address')
        dob = request.POST.get('DOB')
        ph = request.POST.get('ph')
        bg = request.POST.get('bg')
        city = request.POST.get('city')
        taluka = request.POST.get('taluka')
        district = request.POST.get('district')
        add1 = request.POST.get('address1')
        ph1 = request.POST.get('ph1')
        city1 = request.POST.get('city1')
        state1 = request.POST.get('state1')
        pincode1 = request.POST.get('pincode1')
        image = request.FILES.get('image')

        if image:
            employee.image = image
        if em:
          user.email = em
        if ph:
         employee.workphone = ph
        #employee.bg = bg
        if add:
         employee.address = add
        if city:
         employee.city = city
        if taluka:
         employee.taluka = taluka
        if district:
         employee.district = district

        if dob:
            employee.DOB = dob
        if bg:
            employee.bg = bg

        if customer is not None:
            if ph1:
             customer.phone = ph1
            #employee.bg = bg
            if add1:
             customer.Address = add1
            if city1:
             customer.City = city1
            if state1:
             customer.state = state1
            if pincode1:
             customer.Pincode = pincode1

        try:
            employee.save()
            user.save()
            #customer.save()

            # print(employee.image, user.first_name, user.last_name, user.email,
            #       user.password, user.date_joined, employee.DOB, employee.department, employee.phone,
            #       employee.designation)
            # User.objects.create_user(first_name=fn,last_name=ln,username=un,password=pwd,id=ec,email=em,date_joined=jod)
            # Profile.objects.create(address=add,DOB=dob,department=dept,image=img,phone=ph)
            error="no"
        except:
            error="yes"
    return render(request, 'user/edit_profile.html', locals())


#     fn = request.POST['firstname']
    #     ln = request.POST['lastname']
    #
    #
    #     em = request.POST['email']
    #     pwd = request.POST['pwd']
    #     add = request.POST['address']
    #     dob = request.POST['DOB']
    #     jod = request.POST['jod']
    #     dept = request.POST['dept']
    #     image = request.FILES.get('image')
    #     ph = request.POST['ph']
    #     desig = request.POST['desig']
    #
    #     user.first_name = fn
    #     user.last_name = ln
    #     user.email = em
    #     user.password = pwd
    #     employee.department = dept
    #     employee.phone = ph
    #     employee.designation = desig
    #     if jod:
    #         user.date_joined = jod
    #
    #     if dob:
    #         employee.DOB = dob
    #     if image:
    #         employee.image = image
    #
    #     try:
    #         employee.save()
    #         user.save()
    #         print(employee.image, user.first_name, user.last_name, user.email,
    #               user.password, user.date_joined, employee.DOB, employee.department, employee.phone,
    #               employee.designation)
    #         # User.objects.create_user(first_name=fn,last_name=ln,username=un,password=pwd,id=ec,email=em,date_joined=jod)
    #         # Profile.objects.create(address=add,DOB=dob,department=dept,image=img,phone=ph)
    #         error="no"
    #     except:
    #         error="yes"
    # return render(request, 'user/profile.html', locals())



def profile_update(request,pk):
    error = ""
    count1 = staff_Notification.objects.filter(staff_id=request.user.id, status=False).count()
    notification1 = staff_Notification.objects.filter(staff_id=request.user.id, status=False).order_by('-created_at')
    departments = Profile._meta.get_field('department').choices
    designations = Profile._meta.get_field('designation').choices
    bgs = Profile._meta.get_field('bg').choices
    user1 = User.objects.get(id=pk)
    print(user1)
    employee = Profile.objects.get(customer_id=user1)
    print(user1)
    if request.method == "POST":
        fn = request.POST['firstname']
        ln = request.POST['lastname']
        em = request.POST['email']
        add = request.POST['address']
        dob = request.POST['DOB']
        jod = request.POST['jod']
        dept = request.POST.get('dept')
        image = request.FILES.get('image')
        ph = request.POST['ph']
        desig = request.POST.get('desig')

        bg = request.POST.get('bg')
        city = request.POST['city']
        taluka = request.POST['taluka']
        district = request.POST['district']
        pg = request.POST['pg']
        institution = request.POST['institution']
        yop = request.POST['yop']
        specili = request.POST['specili']
        name = request.POST['name']
        phone = request.POST['phone']
        emremail = request.POST['emremail']
        emraddress = request.POST['emraddress']


        user1.first_name = fn
        user1.last_name = ln
        user1.email = em

        #employee.department = dept
        employee.phone = phone
        #employee.designation = desig
        employee.address = add

        #employee.bg = bg
        employee.city = city
        employee.taluka = taluka
        employee.district = district
        employee.pg = pg
        employee.institution = institution
        employee.specili = specili
        employee.name = name
        employee.workphone = ph
        employee.email = emremail
        employee.emraddress = emraddress

        if dept:
            employee.department = dept
        if desig:
            employee.designation = desig
        if bg:
            employee.bg = bg
        if yop:
            employee.yop = yop

        if jod:
            user1.date_joined = jod

        if dob:
            employee.DOB = dob
        if image:
            employee.image = image

        try:
            user = get_user(request)
            employee.last_updated_by = user.id
            print(user)
            employee.save()
            user1.save()
            print(employee.image, user1.first_name, user1.last_name, user1.email,
                  user1.password, user1.date_joined, employee.DOB, employee.department, employee.phone,
                  employee.designation)
            logout(request)
            login(request, user)



            # User.objects.create_user(first_name=fn,last_name=ln,username=un,password=pwd,id=ec,email=em,date_joined=jod)
            # Profile.objects.create(address=add,DOB=dob,department=dept,image=img,phone=ph)
            error="no"
        except:
            error="yes"
    return render(request, 'user/profile_update.html', locals())

def profile_updatepage(request,pk):
    count1 = staff_Notification.objects.filter(staff_id=request.user.id, status=False).count()
    notification1 = staff_Notification.objects.filter(staff_id=request.user.id, status=False).order_by('-created_at')
    user1 = User.objects.get(id=pk)
    employee = Profile.objects.get(customer_id=pk)
    return render(request, 'user/profile_updatepage.html', locals())



# def profile_update(request,pk):
#     error=" "
#     item1 = User.objects.get(id=pk)
#     item = Profile.objects.get(id=pk)
#
#
#     if request.method == 'POST':
#
#         u_form = UserUpdateForm(request.POST, instance=item1)
#         p_form = ProfileUpdateForm(
#             request.POST, request.FILES, instance=item)
#
#         if u_form.is_valid() and p_form.is_valid():
#             u_form.save()
#             p_form.save()
#             return redirect('user-profile', item.id)
#     else:
#         u_form = UserUpdateForm(instance=item1)
#         p_form = ProfileUpdateForm(instance=item)
#
#     context = {
#
#         'u_form': u_form,
#         'p_form': p_form,
#     }
#     return render(request, 'user/profile_update.html', context)



