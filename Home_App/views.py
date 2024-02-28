from django.shortcuts import render, redirect
from .models import signuptable, signintable, imagetable, loginpanal, logintable, contacttable, ordertable, \
    categorytable, brandtable, slidertable

from django.contrib.sessions.models import Session

# Create your views here.
#  function for open index  page.
def index(request):
    return render(request,"index.html")
# function for open electronics  page.
def electronic(request):
    return render(request,'electronic.html')
# function for open fashion  page.
def fashion(request):
    return render(request,'fashion.html')
# function for open grocery  page.
def grocery(request):
    return render(request,'grocery.html')

# function for open About  page.
def about(request):
    return render(request,"aboutus.html")
# function for open contact  page.
def contact(request):
    return render(request,"contactus.html")


# function for open product page with get all products save in dictionary.
def product(request):
    result = imagetable.objects.all()
    return render(request,"product.html",{"results": result})

# function for insert product and details in database.
def addimgcode(request):
    i = request.FILES['image']
    n = request.POST['name']
    p = request.POST['price']
    d = request.POST['discount']
    insert = imagetable(image=i,name=n,price=p,discount=d)
    insert.save()
    return render(request,"userdashboard.html")

# function for show all products in AdminPanal and product page.

def show(request):
    result = imagetable.objects.all()
    return render(request, 'showproduct.html', {"results": result})

# function for detele  products in AdminPanal and product page by id.
def delete(request, id):
    delproduct = imagetable.objects.get(id=id)
    delproduct.delete()
    # return render(request, 'show.html/')
    # return HttpResponse("show.html")
    return redirect("../show")

# def edit(request):
#     return render(request, 'editproduct.html')

# function for edit products in AdminPanal and product page by id.
def editcode(request,id):
    results = imagetable.objects.get(id=id)
    return render(request, "editproduct.html", {'results': results})

# function for update products and product details.
def updatedata(request):
    a = request.POST['id']
    n= request.FILES['name']
    ne = request.POST['pname']
    p = request.POST['price']
    d = request.POST['discount']
    update = imagetable(id=a, image=n,name=ne,price=p,discount=d)
    update.save()
    # return render(request, "Edit.html")
    return redirect("../show")





# function for open signup page.
def signup(request):
    return render(request,"signup.html")

# function for insert signuppage details in database.
def signupinsert(request):
    name = request.POST['name']
    email= request.POST['email']
    password= request.POST['password']
    insert=signuptable(user_name=name,email_id=email,password=password)
    insert.save()
    insert1 = signintable(email_id=email,password=password)
    insert1.save()
    return redirect("../signin")

# function for show all details of signup page in Admin Panal.
def showuser(requets):
    result =signuptable.objects.all()
    return render(requets,'Show User.html',{"results":result})

# function for delete details of signup page in Admin Panal By Id.
def deleteuser(request, id):
    deluser = signuptable.objects.get(id=id)
    deluser.delete()
    # return render(request, 'show.html/')
    # return HttpResponse("show.html")
    return redirect("../showuser")

# function for open edit page.
# def edituser(request):
#     return render(request, 'edituser.html')

# function for edit details of signup page in Admin Panal by Id.
def editusercode(request,id):
    results = signuptable.objects.get(id=id)
    return render(request, "edituser.html", {'results': results})

# function for update details of signup page in Admin Panal.
def updateuser(request):
    a = request.POST['id']
    n= request.POST['name']
    p = request.POST['email']
    d = request.POST['pass']
    update = signuptable(id=a, user_name=n,emai_id=p, password=d)
    update.save()
    # return render(request, "Edit.html")
    return redirect("../showuser")

# function for open signin  page.
def signin(request):
    return render(request,"signin.html")

# function for check email and passsword is same from signup data.
def signincode(request):
    email=request.POST['email']
    password=request.POST['password']
    print(email)
    print(password)
    if email=='' and password=='':
        return render(request, "signin.html")
    else:
        if signintable.objects.filter(email_id=email).exists():
            if signintable.objects.filter(password=password).exists():
                    return render(request, "index.html")

            else:
                print("password wrong")
                return render(request, "signin.html")
        else:
            print("email wrong")
            return render(request, "signin.html")

# function for open forget page.
def forget(request):
    return render(request,"forgetpassword.html")

# function for open otp page.
def otp(request):
    return render(request,"otp.html")

# function for open newpassword page.
def newpassword(request):
    return render(request,"newpassword.html")

# function for check email in signindata.
def checkemail(request):
    email = request.POST['email']
    if email=='':
        return render(request,'signin.html')
    else:
        if signintable.objects.filter(email_id=email).exists():
            return redirect("../otp")
        else:
            return render(request, 'forgetpassword.html')

# function for check opt.
def otpcode(request):
    otp = request.POST['otp']
    if otp =='':
        return render(request,'otp.html')
    else:
        if signuptable.objects.filter(otp=otp):

          res = signuptable.objects.latest('id')
          return render(request,'newpassword.html',context={'res':res})
        else:
            return render(request,'otp.html')

# def newpasswordcode(request,id):
#     res = signuptable.objects.get(id=id)
#     return render(request,"newpassword",{'res':res})

# function for update passworrd
def updatepassword(request):
    if request.POST['pass'] == request.POST['pass1']:
        id = request.POST['id']
        name = request.POST['name']
        c = request.POST['pass1']
        e = request.POST['email']
        update= signuptable(id=id,user_name=name,email_id=e,password=c)
        update.save()
        update1=signintable(id=id,email_id=e,password=c	)
        update1.save()
        return render(request,"signin.html")
    else:
        return render(request,"otp.html")



# function for open Adminlogin page.
def login(request):
    return render(request,'loginpanal.html')

# function for open dashboard with session.
def userdashboard(request):
    if request.session.has_key('user'):
        return render(request, 'userdashboard.html')
    else:
        return render(request, 'loginpanal.html')

# function for insert Adminregister details in database.
def loginpanapinsert(request):
    a = request.POST['name']
    b= request.POST['email']
    c=request.POST['mobile']
    d= request.POST['password']
    insert=loginpanal(name=a,email=b,mobile=c,password=d)
    insert.save()
    insert1 =logintable(email=b,password=d)
    insert1.save()
    return redirect("../login")

# function for check email and passsword is same from Adminregister data.
def logincode(request,):
    email=request.POST['email']
    password=request.POST['password']
    if email=='' and password=='':
        return render(request, "loginpanal.html")
    else:
        if logintable.objects.filter(email=email).exists():
            if logintable.objects.filter(password=password).exists():
                request.session['user']=True
                return render(request, "userdashboard.html")
            else:
                print("password wrong")
                return render(request, "loginpanal.html")
        else:
            print("email wrong")
            return render(request, "loginpanal.html")

# function for open forget page.
def forgetadmin(request):
    return render(request,"forgetadmin.html")
# function for open opt
# page.
def adminotp(request):
    return render(request,"adminotp.html")

# function for newpassword page forget page.
def adminnewpassword(request):
    return render(request,"newpassadmin.html")

# function for check email from login data.
def admincheckemail(request):
    email = request.POST['email']
    if email=='':
        return render(request,'loginpanal.html')
    else:
        if logintable.objects.filter(email=email).exists():
            return redirect("../adminotp")
        else:
            return render(request, 'adminforget.html')

# function for verify otp.
def adminotpcode(request):
    admin = request.POST['admin']
    if otp =='':
        return render(request,'adminotp.html')
    else:
        if loginpanal.objects.filter(otp=admin):
          res = loginpanal.objects.latest('id')
          return render(request,'newpassadmin.html',context={'res':res})
        else:
            return render(request,'adminotp.html')

# def newadminpasswordcode(request,id):
#     res = loginpanal.objects.get(id=id)
#     return render(request,"newpassadmin",{'res':res})

def adminupdatepassword(request):
    if request.POST['pass'] == request.POST['pass1']:
        id = request.POST['id']
        name = request.POST['name']
        e = request.POST['email']
        n = request.POST['num']
        p = request.POST['pass1']

        update= loginpanal(id=id,name=name,email=e,mobile=n,password=p)
        update.save()
        update2 = logintable(id=id,email=e,password=p)
        update2.save()
        return render(request,"loginpanal.html")
    else:
        return render(request,"adminotp.html")




















def contactinsert(request):
    fn = request.POST['firstname']
    ln = request.POST['lastname']
    em= request.POST['email']
    con = request.POST['country']
    su= request.POST['subject']
    insert=contacttable(first_name=fn,last_name=ln,email=em,counrty=con,subject=su)
    insert.save()
    return redirect("../contact")

def showcontact(request):
    result = contacttable.objects.all()
    return render(request,'showcontact.html',{"results":result})

def deletecontact(request,id):
    delcontact = contacttable.objects.get(id=id)
    delcontact.delete()
    return redirect("../showcontact")


def order(request):
    return render(request,'order.html')

def orderinsert(request):
    a = request.POST['name']
    b = request.POST['price']
    c= request.POST['quit']
    d = request.POST['addr']
    insert=ordertable(order_name=a,price=b,quantity=c,Address=d)
    insert.save()
    return redirect("../")

def showorder(request):
    result = ordertable.objects.all()
    return render(request,'showorder.html',{"results":result})

def deletorder(request, id):
    delorder = ordertable.objects.get(id=id)
    delorder.delete()
    return redirect("../showorder")


def addcategorycode(request):
    i = request.FILES['image']
    p = request.POST['name']
    insert = categorytable(cate_image=i,cate_name=p)
    insert.save()
    return render(request,"userdashboard.html")


def index(request):
    showcat=categorytable.objects.all()
    showdrand = brandtable.objects.all()
    showslider = slidertable.objects.all()
    return render(request,"index.html",{"showcats":showcat,"showbr":showdrand,'showsli':showslider})

def showcatep(request):
    resultp = categorytable.objects.all()
    return render(request, 'showcategory.html', {"resultsp": resultp})



def deletcate(request, id):
    deluser = categorytable.objects.get(id=id)
    deluser.delete()
    # return render(request, 'show.html/')
    # return HttpResponse("show.html")
    return redirect("../showcatep")

def editcate(request):
    return render(request, 'editecategory.html')

def editcatecode(request,id):
    results = categorytable.objects.get(id=id)
    return render(request, "editecategory.html", {'results': results})


def updatecate(request):
    a = request.POST['id']
    n= request.FILES['catimage']
    p = request.POST['catname']
    # d = request.POST['pass']
    update = categorytable(id=a, cate_image=n,cate_name=p)
    update.save()
    # return render(request, "Edit.html")
    return redirect("../showcatep")






# brand code start
def addbrandcode(request):
    i = request.FILES['image']
    p = request.POST['name']
    insert = brandtable(brand_image=i,brand_name=p)
    insert.save()
    return render(request,"userdashboard.html")


# def index2(request):
#     showdrand=brandtable.objects.all()
#     return render(request,"index.html",{"showbr":showdrand})

def showbrandp(request):
    resultp = brandtable.objects.all()
    return render(request, 'showbrand.html', {"resultsp": resultp})



def deletbrand(request, id):
    deluser = brandtable.objects.get(id=id)
    deluser.delete()
    # return render(request, 'show.html/')
    # return HttpResponse("show.html")
    return redirect("../showbrandp")

def editbrand(request):
    return render(request, 'editbrand.html')

def editbrandcode(request,id):
    results = brandtable.objects.get(id=id)
    return render(request, "editbrand.html", {'results': results})


def updatebrand(request):
    a = request.POST['id']
    n= request.FILES['brandimage']
    p = request.POST['brandname']
    # d = request.POST['pass']
    update = brandtable(id=a, brand_image=n,brand_name=p)
    update.save()
    # return render(request, "Edit.html")
    return redirect("../showbrandp")


def search(request):
    se = request.POST['search']
    a = imagetable.objects.filter(name=se)
    if se!='':
        return render(request,'search.html',{'dics':a})
    else:
        return redirect('../index')




# function for open product page with get all products save in dictionary.
# def slider(request):
#     result = slidertable.objects.all()
#     return render(request,"index.html",{"results": result})

# function for insert product and details in database.
def addslidercode(request):
    i = request.FILES['image']
    n = request.POST['name']
    insert = slidertable(slider_image=i,slider_name=n,)
    insert.save()
    return render(request,"userdashboard.html")

# function for show all products in AdminPanal and product page.

def showslider(request):
    result = slidertable.objects.all()
    return render(request, 'showslider.html', {"results": result})

# function for detele  products in AdminPanal and product page by id.
def deleteslider(request, id):
    delslider = slidertable.objects.get(id=id)
    delslider.delete()
    # return render(request, 'show.html/')
    # return HttpResponse("show.html")
    return redirect("../showslider")

# def edit(request):
#     return render(request, 'editproduct.html')

# function for edit products in AdminPanal and product page by id.
def editslidercode(request,id):
    results = slidertable.objects.get(id=id)
    return render(request, "editslider.html", {'results': results})

# function for update products and product details.
def updateslider(request):
    a = request.POST['id']
    n= request.FILES['image']
    ne = request.POST['name']
    update = slidertable(id=a, slider_image=n,slider_name=ne)
    update.save()
    # return render(request, "Edit.html")
    return redirect("../showslider")



