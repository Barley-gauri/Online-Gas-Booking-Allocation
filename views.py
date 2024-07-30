from django.shortcuts import render
from gasapp.models import Registration,Feedback,Bookinggas,Kycupload
# Create your views here.
def index(request):
    return render(request,'index.html',{})

def userhome(request):
    return render(request,'userhome.html',{})

def about(request):
    return render(request,'about.html',{})

def contact(request):
    return render(request,'contact.html',{})

def services(request):
    return render(request,'services.html',{})

def booking(request):
    return render(request,'booking.html',{})

def uploadkyc(request):
    return render(request,'uploadkyc.html',{})

def message(request):
    return render(request,'message.html',{})

def orderhistory(request):
    uid = request.session['id']
    data=Bookinggas.objects.filter(consumerid=uid)
    return render(request,'orderhistory.html',{'data':data})

def payment(request):
    return render(request,'payment.html',{})


def storeUser(request):
    if request.method == 'POST':
        fullname = request.POST.get("tfullname")
        emailid = request.POST.get("temail")
        address = request.POST.get("taddress")
        state = request.POST.get("tstate")
        city = request.POST.get("tcity")
        zipcode = request.POST.get("tzipcode")
        contact = request.POST.get("tcontact")
        username = request.POST.get("tusername")
        password1 = request.POST.get("tpass1")
        pass2 = request.POST.get("tpass2")
        
        if password1 == pass2:
            print("1")
            obj = Registration(fullname=fullname, emailid=emailid,address=address,state=state,city=city,\
                zipcode=zipcode,contact=contact,username=username,password1=password1)
            obj.save()
            print("all done")
            return render(request,'index.html',{})
        else:
            print("Password Not Match")
    else:
        return render(request,'index.html',{})
    
def Login(request):
    if request.method=="POST":
        emailid = request.POST.get('temail')
        password1 = request.POST.get('tpass')
        name = 'hello' 
        print(name)
        
        data = Registration.objects.filter(emailid=emailid, password1=password1)
        
        if len(data)==1:   
            mydata = Registration.objects.get(emailid=emailid, password1=password1)
            print(mydata)
            print(mydata.rid)
            request.session['id'] = mydata.rid    
            request.session['name'] = emailid     
            
            return render(request,'userhome.html',{'id':mydata.rid,'name':emailid})
        else:
               
            return render(request,'message.html',{})
            # return render(request,'userhome.html',{})
        
def feedbackform(request):
    if request.method=="POST":
        fullname=request.POST.get('tfullname')
        emailid=request.POST.get('temail')
        message=request.POST.get('tmessage')
        
        obj=Feedback(fullname=fullname,emailid=emailid,message=message)
        obj.save()
        return render(request,'contact.html',{})
    else:
        return render(request,'contact.html',{})
    
def bookinggasCylinder(request):
    if request.method=="POST":
        fullname = request.POST.get("tfullname")
        emailid = request.POST.get("temail")
        bookingdate=request.POST.get("temail")
        consumerid=request.POST.get("tconsumer")
        address = request.POST.get("taddress")
        state = request.POST.get("tstate")
        city = request.POST.get("tcity")
        zipcode = request.POST.get("tzipcode")
        contactno = request.POST.get("tcontact")
        
        obj=Bookinggas(fullname=fullname,emailid=emailid,bookingdate=bookingdate,consumerid=consumerid,\
            address=address,state=state,city=city,zipcode=zipcode,contactno=contactno)
        obj.save()
        return render(request,'userhome.html',{})
    else:
        return render(request,'userhome.html',{})
    
def kycUpload(request):
    if request.method=="POST":
        adharno= request.POST.get("tadhar")
        panno= request.POST.get("tpan")
        rashancard=request.POST.get("trashan")
        
        obj=Kycupload(adharno=adharno,panno=panno,rashancard=rashancard)
        obj.save()
        return render(request,'userhome.html',{})
    else:
        print("error")
        return render(request,'userhome.html',{})