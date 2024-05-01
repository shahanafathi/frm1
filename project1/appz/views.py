from django.shortcuts import render,redirect
from django.http.response import HttpResponse
from .models import register,formpage,form21,modelss
from .forms import index_form,form2,mymodel,modelform


def index(request):
    return render(request,'index.html')




def regstrpage(request):
    if request.method == 'POST':
        file=request.FILES['file']
        sclnm=request.POST['sname']
        dst=request.POST['Dict']
        adrss=request.POST['adrs']
        phone=request.POST['phn_no']
        email=request.POST['email']
        pswd=request.POST['psw']
        data = register.objects.create(file=file,schlname=sclnm,district=dst,address=adrss,phone=phone,email=email, password=pswd)
        print(data)
        data.save()
        return redirect(registerpg)
    else :
        return render(request,'indexx1.html')
    
def registerpg(request):
    data1=register.objects.all()
    return render(request,'table1.html',{'m_data':data1})

def search(request):
    if request.method == 'POST':
        a = request.POST['schoolname']
        data2 = register.objects.filter(schlname=a)
        return render(request,'table1.html',{'m_data':data2})
    else:
            return render(request,'table1.html')
        
def delete(request,id):
    data_a = register.objects.get(id=id)
    data_a.delete()
    return redirect(registerpg)

def edits(request,id):
    data_b= register.objects.get(id=id)
    if request.method =='POST':
        data_b.schlname=request.POST['sname']
        data_b.district=request.POST['Dict']
        data_b.address=request.POST['adrs']
        data_b.phone=request.POST['phn_no']
        data_b.email=request.POST['email']
        data_b.password=request.POST['psw']
        data_b.save()
        return redirect(registerpg)
    else:
        return render(request,'edit.html',{'data3':data_b})
    
def page1(request):
    return render(request,'page1.html') 


def formpage(request):
    if request.method=="POST":
        form1=index_form(request.POST)
        if form1.is_valid():
            name=form1.cleaned_data['name']
            age=form1.cleaned_data['age']
            phoneno=form1.cleaned_data['phone_no']
            data=formpage.objects.create(name=name,age=age,phoneno=phoneno)
            data.save()
            return HttpResponse('finish')
    else:
        data6=index_form()
        return render(request,'forms.html',{'data':data6})
    
def form(request):
    if request.method=='POST':
        data1=form2(request.POST)
        if data1.is_valid():
            name=data1.cleaned_data['name']
            age=data1.cleaned_data['age']
            address=data1.cleaned_data['address']
            phone=data1.cleaned_data['phone']
            email=data1.cleaned_data['email']
            password=data1.cleaned_data['password']
            data2=form21.object.create(name=name,age=age,address=address,phone=phone,email=email,password=password)
            data2.save()
            return HttpResponse("sucess")
    else:
        dataa=form2()
        return render(request,'frm.html',{'data':dataa})
    
def hosp(request):
    if request.method=='POST':
        datas=mymodel(request.POST)
        if datas.is_valid():
            datas.save()
            return HttpResponse('sucessfull')
    
    else:
        data1=mymodel()
        return render(request,'hosp.html',{'data':data1})
    
def mdlform(request):
    if request.method=='POST':
        data=modelform(request.POST)
        if data.is_valid():
            data.save()
            data2=modelform.objects.all()
            return render(request,'tabel1.html',{'data':data2})
    else:
        dataas=modelform()
        return render(request,'form4.html',{'data':dataas})
    
def tblmdl(request):
    data=modelss.objects.all()
    return render (request,'tbl.html',{'datas':data})
    
    
def del_tbl(request,id):
    data1 = modelss.objects.get(id=id)
    data1.delete()
    return redirect(tblmdl)   

def edit(request,id):
    data= modelss.objects.get(id=id)
    if request.method =='POST':
        data.fname=request.POST['fname']
        data.lname=request.POST['lname']
        data.address=request.POST['address']
        data.phone=request.POST['phone']
        data.save()
        return redirect(tblmdl)
    else:
        return render(request,'form4.html',{'datas':data})