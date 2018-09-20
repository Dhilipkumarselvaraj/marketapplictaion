from django.shortcuts import render
from django.http import JsonResponse
import json
from django.contrib import messages
# Create your views here.
from deliverysystem.models import customer_details
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .forms import customerdetails_form
import uuid

value = 0
def test(request):
    return JsonResponse({"lol":"lol2"})

def home(request):
    customer_list = customer_details.objects.all()
    #import pdb;pdb.set_trace()
    context_dict = {'customer_list': customer_list}
    return render(request, 'deliverypage/home.html', context_dict)




def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def add_customers(request):
    if request.method == "POST":
        form = customerdetails_form(request.POST)
        if form.is_valid():
            import pdb;pdb.set_trace()
            
            # auto_increment = auto_increment
            customer_uuid = str(uuid.uuid4())
            first_name = form.cleaned_data['first_name']
            second_name = form.cleaned_data['second_name']
            email_id = form.cleaned_data['email_id']
            mobile_no_primary = form.cleaned_data['mobile_no_primary']
            mobile_no_secondary = form.cleaned_data['mobile_no_secondary']
            customer_type = form.cleaned_data['customer_type']
            period = form.cleaned_data['period']
            quantity = form.cleaned_data['quantity']
            supplier_name = form.cleaned_data['supplier_name']
            date_of_join =form.cleaned_data['date_of_join']
            area_code = form.cleaned_data['area_code']
            address = form.cleaned_data['address']
            pm_id = "#PM-"+str(area_code)+"-"#+str(auto_increment)
            values = customer_details.objects.create(
                            # auto_increment = auto_increment,
                            customer_uuid = customer_uuid,
                            pm_id = pm_id,
                            first_name = first_name,
                            second_name = second_name,
                            email_id = email_id,
                            mobile_no_primary = mobile_no_primary,
                            mobile_no_secondary = mobile_no_secondary,
                            customer_type = customer_type,
                            period = period,
                            quantity = quantity,
                            supplier_name = supplier_name,
                            date_of_join = date_of_join,
                            area_code = area_code,
                            address = address,
                            )
            #send_mail('your allocated server is'+Ip_address, 'body of the message', 'noreply@appviewx.com', [Email_id])
            return redirect("home")
        else:
            print (form.errors)
            #return redirect('home')
            return {"error":"?"}
    else:
        form = customerdetails_form()
    return render(request,'add_customers.html',{'form':form})
