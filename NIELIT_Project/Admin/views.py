from django.shortcuts import render,redirect
# from .models import Admin,Employee
# from django.contrib import messages

# Create your views here.
def admin(request):
    return render(request,'admin.html')

def home(request):
    return render(request,'home.html')

def employee(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        # try:
        #     user = Employee.objects.get(username=username)
        #     if password == user.password:
        #         return redirect('/employee/' + username)
        #     else:
        #         messages.info(request, 'Password Incorrect')
        # except:
        #     messages.info(request,"User not found!")

        # return redirect('/employee')
        

    return render(request,'employee.html')

def adminlogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # try:
        #     user = Admin.objects.get(username=username)
        #     if password == user.password:
        #         return redirect('/Admin/'+username)
        #     else:
        #         messages.info(request,"Password Incorrect!")
        # except:
        #     messages.info(request,"User not found!")

        # return redirect('/aLogin')

    return render(request,'Adminlogin.html')

def adminregister(request):
    if request.method == 'POST':
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        phone = request.POST['phone']
        psd1 = request.POST['psd1']
        psd2 = request.POST['psd2']
        
        # if not Admin.objects.filter(username=username):
        #     if not Admin.objects.filter(phone=phone):
        #         if psd1 == psd2:
        #             user = Admin.objects.create(username=username, firstname=fname, lastname=lname, mail=email, phone=phone,password=psd1)
        #             user.save()
        #             return redirect('/aLogin')
        #         else:
        #             messages.info(request,"Password mismatch")
        #     else:
        #         messages.info(request,"Phone number already registered")
        # else:
        #     messages.info(request, "Username already registered")
        # return redirect('/aRegister')
    
    return render(request,'AdminRegister.html')

# def employeeLogged(request, name):

#     user = Employee.objects.get(username=name)
#     data = {
#         'fname': user.firstname,
#         'lname': user.lastname,
#         'email': user.mail,   
#     }
#     return render(request,'EmployeeLogged.html',data)

# def adminLogged(request, name):
#     user = Admin.objects.get(username=name)
#     employee = Employee.objects.all()
#     data = {
#         'fname': user.firstname,
#         'lname': user.lastname,
#         'email': user.mail,
#         'employee': enumerate(employee),
#     }

#     return render(request,'AdminLogged.html',data)


def createEmployee(request):
    return render(request,'createEmployee.html')

def updateEmployee(request):
    return render(request,'updateEmployee.html')

def deleteEmployee(request):
    return render(request,'deleteEmployee.html')

def searchEmployee(request):
    return render(request,'searchEmployee.html')