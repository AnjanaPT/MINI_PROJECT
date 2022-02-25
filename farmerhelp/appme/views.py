from django.shortcuts import render,HttpResponseRedirect
import pymysql
from django.core.files.storage import FileSystemStorage
from datetime import datetime
from datetime import date
# Create your views here.
db=pymysql.connect("localhost","root","","mycolorfarm")
c=db.cursor()

def index(request):
    if request.POST:
        Username=request.POST.get("Username")
        request.session["username"]=Username
        Password=request.POST.get("Password")
        print("select count(*),usertype,status from login where username='" + Username + "' and password='" + Password + "'")
        res=c.execute("select count(*),usertype,status from login where username='" + Username + "' and password='" + Password + "'")
        rs=c.fetchone()
        db.commit()
        print(rs)
        if rs[0]>0 and rs[1]=="admin" and rs[2]=="Approved":
            return HttpResponseRedirect('/admin_home/')
        if rs[0]>0 and rs[1]=="Public" and rs[2]=="Approved":
                 return HttpResponseRedirect('/public_home/')
        
        if rs[0]>0 and rs[1]=="farmer" and rs[2]=="Approved":
                    return HttpResponseRedirect('/farmer_home/')
        if rs[0]>0 and rs[1]=="Exporters" and rs[2]=="Approved":                        
                        return HttpResponseRedirect('/exporters_home/')
        if rs[0]>0 and rs[1]=="Specialist" and rs[2]=="Approved":
            return HttpResponseRedirect('/specialist_home/')
        if rs[0]>0 and rs[1]=="suppliers" and rs[2]=="Approved":
            return HttpResponseRedirect('/suppliers_home/')
        else:
            msg="invalid username"
    return render(request,'common/common_login.html')
def admin_home(request):
    return render(request,'admin/admin_home.html')

def admin_about(request):
    return render(request,'admin/admin_about.html')

def farmer_home(request):
    return render(request,'farmer/farmer_home.html')

def exportersaddorderrequest(request):

    from datetime import datetime
    print("*"*50)
    if request.POST:
        Productname=request.POST.get("Productname")
        Quantity=request.POST.get("Quantity")
        email=request.session["username"]
        dates=datetime.today().strftime("%Y-%m-%d")
        print("insert into exportersorder(Productname,Quantity,email,dates,status) values ('"+Productname+"','"+Quantity+"','"+email+"','"+dates+"','pending')")
        c.execute("insert into exportersorder(Productname,Quantity,email,dates,status) values ('"+Productname+"','"+Quantity+"','"+email+"','"+dates+"','pending')")
    return render(request,'exporters/exportersaddorderrequest.html')

def exporters_home(request):
    return render(request,'exporters/exportershome.html')

def specialist_home(request):
    return render(request,'specialist/specialisthome.html')
def public_home(request):
    return render(request,'public/public_home.html')
def suppliers_home(request):
    return render(request,'suppliers/suppliershome.html')

def common_register(request):
    return render(request,'common/common_register.html')


def farmerreg(request):
    msg=""
    res=0
    qry=""
    rs=""
    if request.POST and request.FILES.get("uploads"):  
        
        FarmersName=request.POST.get("FarmersName")
        HouseName=request.POST.get("HouseName")
        State=request.POST.get("State")
        District=request.POST.get("District")
        panchayath=request.POST.get("panchayath")
        Postoffice=request.POST.get("Postoffice")
        PostalZipCode=request.POST.get("PostalZipCode")
        email=request.POST.get("email")
        PhoneNumber=request.POST.get("PhoneNumber")
        password=request.POST.get("password")
        status="Pending"
        AccountNumber=request.POST.get("AccountNumber")
        NameoftheBank=request.POST.get("NameoftheBank")
        IFSC=request.POST.get("IFSC")
        c.execute("select count(*) as cnt from farmerreg where email='" + str(email) + "' or phonenumber='" + str(PhoneNumber) +"'")
        rs=c.fetchone()
        db.commit()
        
        if rs[0]>0 :
            msg="Already registread"
        else: 
                          
            myfile=request.FILES.get("uploads")
            fs=FileSystemStorage()
            filename=fs.save(myfile.name,myfile)
            uploadurl=fs.url(filename)
            c.execute("insert into farmerreg(FarmersName,HouseName,State,District,panchayath,Postoffice,PostalZipCode,email,phonenumber,proof,password,status,AccountNumber,NameoftheBank,IFSC) values('" + str(FarmersName) +"','" + str(HouseName) + "','" + str(State) + "','" + str(District) + "','" + str(panchayath) + "','" + str(Postoffice) + "','" + str(PostalZipCode) + "','" + str(email) + "','" + str(PhoneNumber) + "','" + str(uploadurl) + "','" + str(password) + "','" + str(status) + "','" + str(AccountNumber) + "','" + str(NameoftheBank) + "','" + str(IFSC) + "')")
            db.commit()
            usertype="farmer"
            status="pending"
            c.execute("insert into login(username,password,usertype,status) values('" + str(email) +"','" + str(password) +"','" + str(usertype) + "','" + str(status) + "')")
            db.commit()
            msg="saved"
        
    return render(request,'common/farmerreg.html')
def Exportersreg(request):
    msg=''
    if request.POST and request.FILES.get("uploads"):
       
        ExpotrersName=request.POST.get("ExpotrersName")
        RegistraionCode=request.POST.get("RegistraionCode")
        Country=request.POST.get("Country")
        State=request.POST.get("State")
        District=request.POST.get("District")
        PhoneNumber=request.POST.get("PhoneNumber")
        dates=request.POST.get("dates")
        email=request.POST.get("email")
        Password=request.POST.get("password")
        AccountNumber=request.POST.get("AccountNumber")
        BankName=request.POST.get("BankName")
        IFSC=request.POST.get("IFSC")
        print("hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh")
        print("select count(*) as cnt from Exporters where RegistraionCode='" + str(RegistraionCode) + "' or PhoneNumber='" + str(PhoneNumber) + "' or email='" + str(email) + "'")
        res=c.execute("select count(*) as cnt from Exporters where RegistraionCode='" + str(RegistraionCode) + "' or PhoneNumber='" + str(PhoneNumber) + "' or email='" + str(email) + "'")
        rs=c.fetchone()
        db.commit()
        print(rs[0])
        if rs[0]>0:
            msg="already registred"
        else:
            myfile=request.FILES.get("uploads")
            fs=FileSystemStorage()
            filename=fs.save(myfile.name,myfile)
            uploadurl=fs.url(filename)
            status="pending"
            print("hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh")
            print("insert into Exporters(ExpotrersName,RegistraionCode,Country,State,District,PhoneNumber,dates,file,email,Password,AccountNumber,BankName,IFSC,status) values('" + str(ExpotrersName) + "','" + str(RegistraionCode) + "','" + str(Country) + "','" + str(State) + "','" + str(District) + "','" + str(PhoneNumber) + "','" + str(dates) + "','" + str(uploadurl) + "','" + str(email) + "','" + str(Password) + "','" + str(AccountNumber) + "','" + str(BankName) + "','" + str(IFSC) + "','" + str(status) + "')")
            c.execute("insert into Exporters(ExpotrersName,RegistraionCode,Country,State,District,PhoneNumber,dates,file,email,Password,AccountNumber,BankName,IFSC,status) values('" + str(ExpotrersName) + "','" + str(RegistraionCode) + "','" + str(Country) + "','" + str(State) + "','" + str(District) + "','" + str(PhoneNumber) + "','" + str(dates) + "','" + str(uploadurl) + "','" + str(email) + "','" + str(Password) + "','" + str(AccountNumber) + "','" + str(BankName) + "','" + str(IFSC) + "','" + str(status) + "')")
            usertype="Exporters"
            c.execute("insert into login(username,password,usertype,status) values('"+ email +"','" + Password + "','Exporters','pending')")
            db.commit()
            msg="saved"
    return render(request,'common/Exporters.html')
def publicreg(request):
    rs=''
    if request.POST:
        yourname=request.POST.get("yourname")
        phonenumber=request.POST.get("phonenumber")
        Username=request.POST.get("Username")
        Password=request.POST.get("Password")
        res=c.execute("select count(*) as cnt from publicreg where phonenumber='" + phonenumber + "' or Username='" + Username + "'")
        rs=c.fetchone()
        db.commit()
        if rs[0]>0:
            msg="Already registred"
        else:
            c.execute("insert into publicreg(yourname,phonenumber,Username,Password) values('" + str(yourname) + "','" + str(phonenumber) + "','" + str(Username) + "','" + str(Password) + "')")
            usertype="Public"
            status="Approved"
            c.execute("insert into login(username,password,usertype,status) values('" + str(Username) +"','" + str(Password) +"','" + str(usertype) + "','" + str(status) + "')")
            db.commit()
            
    return render(request,'common/common_register.html')

def adminpublicapproval(request):
    c.execute("select * from publicreg")
    res=c.fetchall()
    
   
    return render(request,'admin/admin_publicapproval.html',{"res":res})

def adminfarmerapproval(request):
    status="Pending"
    c.execute("select * from farmerreg where status='Pending'")
    res=c.fetchall()
    if request.GET.get("id"):
        id=request.GET.get("id")
        c.execute("select email from farmerreg where farmerid='"+ id +"' ")
        
        email=c.fetchone()
        c.execute("update farmerreg set status='Approved' where farmerid ='" + id + "'")
        c.execute("update login set status='Approved' where username='" + email[0] + "'")
        db.commit()
   
    return render(request,'admin/adminfarmerapproval.html',{"res":res})
def adminExportersapproval(request):
    status="pending"
    c.execute("select * from exporters where status='pending'")
    res=c.fetchall()
    db.commit()
    if request.GET.get("id"):
        id=request.GET.get("id")
        c.execute("select * from exporters where Exp_regnumber='" + id + "'")
        res1=c.fetchone()
        db.commit()
        email=res1[9]
        c.execute("update exporters set status='Approved' where Exp_regnumber='" + id + "'")
        c.execute("update login set status='Approved' where username='" + email + "'")
        db.commit()
    return render(request,'admin/adminExportersapproval.html',{"res":res})
def admin_addSpecialist(request):
    msg=""
    res=0
    res1=0
    if request.POST:
        Name=request.POST.get("Name")
        Email=request.POST.get("Email")
        MobileNumber=request.POST.get("MobileNumber")
        OfficeName=request.POST.get("OfficeName")
        OfficeContact=request.POST.get("OfficeContact")
        Designation=request.POST.get("Designation")
        Specialized=request.POST.get("Specialized")
        Message=request.POST.get("Message")
        res=c.execute("select count(*) as cnt from specialized where Email='" + str(Email) + "' or MobileNumber='" + str(MobileNumber) + "'or OfficeContact='" + str(OfficeContact) + "'")
        res=c.fetchone()
        res1=c.execute("select count(*) as cnt1 from login where username='" + str(Email) + "'")
        res1=c.fetchone()
        db.commit()
      
        if res[0]>0 or res1[0]>0:
            msg="alreadyregistred"
        else:
            status="Approved"
            usertype="Specialist"
            c.execute("insert into specialized(Name,Email,MobileNumber,OfficeName,OfficeContact,Designation,Specialized,Message) values('"+ str(Name) +"','"+ str(Email) +"','"+ str(MobileNumber) +"','"+ str(OfficeName) +"','"+ str(OfficeContact) +"','"+ str(Designation) +"','"+ str(Specialized) +"','"+ str(Message) +"')")
            c.execute("insert into login(username,password,usertype,status) values('" + str(Email) + "','" + str(MobileNumber) +"','" + str(usertype) + "','" + str(status) +"')")
            db.commit()
            msg="saved"

   
    return render(request,'admin/admin_addSpecialist.html')
def admin_farmer_payment(request):
    res=""
    rs=0 
    res=c.execute("select * from farmerreg")
    rs=c.fetchall()
    return render(request,'admin/admin_farmer_payment.html',{'rs':rs})
def paymentaction(request):
    res1=""
    from datetime import datetime
    if request.GET.get("id"):
        id=request.GET.get("id")
        c.execute("select * from farmerreg where  farmerid='" + id + "'")
        res1=c.fetchall()
        res1=res1[0]
        
    if request.POST:        
        farmerid=request.POST.get("farmerid")
        dates=datetime.today().strftime('%Y-%m-%d')
        amount=request.POST.get("Amount")
        c.execute("insert into farmerpayment(farmerid,amount,dts) values('" + farmerid + "','" + dates + "','" + amount + "')")
        db.commit()
        return HttpResponseRedirect('/admin_farmer_payment/')
    return render(request,'admin/paymentaction.html',{"res1":res1})

    
    
def admincategoryadd(request):
    if request.POST:
        name=request.POST.get("CatName")
        c.execute("insert into category(Categoryname) values('" + name + "')")
        db.commit()
    return render(request,'admin/category.html')
def farmeraddproduct(request):
    c.execute("select * from category")
    rs=c.fetchall()
    if request.POST and request.FILES.get("file1"):
        cat=request.POST.get("cat")
        Name=request.POST.get("Name")
        myfile=request.FILES.get("file1")
        fs=FileSystemStorage()
        filename=fs.save(myfile.name,myfile)
        uploadurl=fs.url(filename)
        unit=request.POST.get("unit")
        rate=request.POST.get("rate")
        quantity=request.POST.get("quantity")
        email=request.session["username"]
        


        c.execute("insert into product(cat,productname,file,unit,rate,quantity,email) values('" + cat + "','" + Name + "','" + uploadurl + "','" + unit + "','" + rate + "','" + quantity + "','" + email + "')")
        db.commit()
    return render(request,'farmer/farmeraddproduct.html',{'data':rs})
def farmeraddseed(request):
    if request.POST and request.FILES.get("file1"):
        
        Name=request.POST.get("Name")
        scientificname=request.POST.get("scientificname")
        verity=request.POST.get("verity")
        rate=request.POST.get("rate")
        quantity=request.POST.get("quantity")
        Description=request.POST.get("Description")
        unit=request.POST.get("unit")
        myfile=request.FILES.get("file1")
        fs=FileSystemStorage()
        filename=fs.save(myfile.name,myfile)
        uploadurl=fs.url(filename)
        email=request.session["username"]
        
        c.execute("insert into seed(Name,file1,scientificname,verity,rate,quantity,Description,unit,email) values('" + Name + "','" +uploadurl + "','" + scientificname + "','" + verity + "','" + rate + "','" + quantity + "','" + Description + "','" + unit + "','" + email + "')")
        db.commit()
    return render(request,'farmer/farmeraddseed.html')
def farmeraddfamingtech(request):
    if request.POST:
        
        Itemname=request.POST.get("Itemname")
        #file1=request.POST.get("file1")
        file1="gggggggg"
        techniqueue=request.POST.get("techniqueue")
        Followups=request.POST.get("Followups")
        #email=request.session["username"]
        email="hhhh"
        c.execute("insert into farmingtechnique(itemname,techniquename,followups,email) values('" + Itemname + "','" + techniqueue + "','" + Followups + "','" + email + "')")
        db.commit()
    return render(request,'farmer/farmeraddfamingtech.html')
def testingresult(request):
    if request.POST:
        Productname=request.POST.get("Productname")
        #file1=request.POST.get("file1")
        file1="gggggggg"
        testname=request.POST.get("testname")
        result=request.POST.get("result")
        Description=request.POST.get("Description")
        #email=request.session["username"]
        email="hhhh"
        c.execute("insert into testing(Productname,testname,file1,result,Description,email) values('" + Productname + "','" + testname + "','" + file1 + "','" + result + "','" + Description + "','" + email + "')")
        db.commit()
    return render(request,'farmer/testingresult.html')
def farmeradddought(request):
    from datetime import datetime
    if request.POST:
        Productname=request.POST.get("Productname")
        #file1=request.POST.get("file1")
        #file1="gggggggg"
        doubt=request.POST.get("doubt")
        dts=datetime.today().strftime('%Y-%m-%d')
        email=request.session["username"]
       
        c.execute("insert into doubt(Productname,doubt,dates,email) values('" + str(Productname) + "','" + str(doubt) + "','" + str(dts) + "','" + str(email) + "')")
        db.commit()
    return render(request,'farmer/farmeradddought.html')
    
def viewdouhtsbyspecialist(request):
    rs=""
    res=""
    rs=c.execute("select * from doubt")
    rs=c.fetchall()
    
    return render(request,'specialist/viewdouhtsbyspecialist.html',{'rs':rs})
def viewdoubtreplay(request):
    from datetime import datetime
    res=""
    if request.GET.get("id"):
        id=request.GET.get("id")
        res=c.execute("select * from doubt where doubtid='" + id + "'")
        res=c.fetchone()
    if request.POST:
        dates=datetime.today().strftime("%Y-%m-%d")
        Productname=request.POST.get("Productname")
        dts=request.POST.get("dts")
        email=request.POST.get("email")
        doubt=request.POST.get("doubt")
        replay=request.POST.get("replay")
        c.execute("insert into doubtreplay(Productname,dts,email,doubt,replay,dates) values('" + Productname + "','" + dts + "','" + email + "','" + doubt + "','" + replay + "','" + dates + "')")
        db.commit()
        return HttpResponseRedirect("/viewdouhtsbyspecialist/")
    return render(request,'specialist/viewdoubtreplay.html',{'res':res})
def addexportrequest(request):
    from datetime import datetime
    print("*"*50)
    if request.POST:
        Productname=request.POST.get("Productname")
        Quantity=request.POST.get("Quantity")
        email=request.session["username"]
        dates=datetime.today().strftime("%Y-%m-%d")
        print(Productname,Quantity,email,dates)
        c.execute("insert into exportersorder(Productname,Quantity,email,dates,status) values('" + Productname + "','" + Quantity + "','" + email + "','" + dates + "','pending')")
        db.commit()
    return render(request,'exporters/exportersaddorderrequest.html')

def adminexportersorderview(request):
    res=c.execute("select exporters.*, exportersorder.* from  exporters inner join exportersorder on  exporters.email=exportersorder.email where exportersorder.status='pending'")
    rs=c.fetchall()
    db.commit()
    if request.GET.get("id"):
        id=request.GET.get("id")
        c.execute("update exportersorder set status='Approved' where orderid='" + id + "'")
        db.commit()
    return render(request,'admin/adminexportersorderview.html',{'data':rs})
def farmerviewseed(request):

    res=c.execute("select * from seed")
    rs=c.fetchall()
    db.commit()
    id=rs[0][0]
    na=rs[0][1]

    return render(request,'farmer/FarmerViewSeed.html',{'data':rs})
def viewseedinfo(request):
    id=request.GET.get("id")
    res=c.execute("select * from seed where seedid='"+str(id)+"'")
    rs=c.fetchall()
    db.commit()
    sid=rs[0][0]
    na=rs[0][1]
    da=date.today()
    id=request.GET.get("id")
    if request.POST:
        id=request.POST.get("Name")
        ca=request.POST.get("scientificname")
        qu=request.POST.get("quantity")
        em=request.session["username"]
        re=c.execute("insert into seedcart(seedid,dates,email) values('"+str(id)+"','"+str(da)+"','"+str(em)+"')")
        db.commit()
        res=c.execute("select * from seed")
        rs=c.fetchall()
        db.commit()
        id=rs[0][0]
        na=rs[0][1]
        return render(request,'farmer/FarmerViewSeed.html',{'data':rs})
    return render(request,'farmer/farmerpurchaseseed.html',{'id':sid,'ca':na})

# def exportersaddproduct(request):
#     nb="select * from exporterscategory"
#     fd=c.execute(nb)
#     ds=c.fetchall()
#     if 'submitproduct' in request.POST:

#         cat=request.POST.get("category")
#         Name=request.POST.get("Name")
#         uploaded_file_url=""
#         myfile=request.FILES.get("f1")
#         fs=FileSystemStorage()
#         filename=fs.save(myfile.name , myfile)
#         uploaded_file_url = fs.url(filename)
#         #file1=request.POST.get("file1")
#         unit=request.POST.get("unit")
#         rate=request.POST.get("rate")
#         quantity=request.POST.get("quantity")
#         email=request.session["uname"]
#         res=c.execute("insert into product(cat,productname,file,rate,quantity,email) values('"+str(cat)+"','"+str(Name)+"','"+str(uploaded_file_url)+"','"+str(rate)+"','"+str(quantity)+"','"+str(email)+"')")
#         db.commit()
#     return render(request,'exporters/exportersaddproduct.html',{'data':ds})
def exporterspayment(request):
    if request.POST:
        cardnumber=request.POST.get("cardnumber")
        cvv=request.POST.get("cardnumber")
        accountnumber=request.POST.get("cardnumber")
        ifsc=request.POST.get("ifsc")
        dates=request.POST.get("dates")
        amount=request.POST.get("amount")
        email=request.session["username"]
        print("hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh")
        print("update exportersorder set cardnumber='" + cardnumber + "', cvv='" + cvv + "',accountnumber='" + accountnumber + "',ifsc='" + ifsc + "',amount='" + amount + "' where email='" + email + "' and dates='" + dates + "'")
        c.execute("update exportersorder set cardnumber='" + cardnumber + "', cvv='" + cvv + "',accountnumber='" + accountnumber + "',ifsc='" + ifsc + "',amount='" + amount + "' where email='" + email + "' and dates='" + dates + "'")
        db.commit()
    return render(request,'exporters/exporterspayment.html')
def farmerseedcart(request):
    email=request.session["username"]
    dates=datetime.today().strftime("%Y-%m-%d")
    
    c.execute("select seed.*,seedcart.* from seed inner join seedcart on seed.seedid=seedcart.seedid where seedcart.email='" + email + "' and seedcart.dates='" + dates + "'")
    res=c.fetchall()
    db.commit()
    
    if request.GET.get("id"):
        id=request.GET.get("id")
        c.execute("delete from seedcart where cartno='" + id + "'")
        db.commit()
    if 'checkout' in request.POST:
        
        return HttpResponseRedirect("/farmerseedpayment")

    return render(request,"farmer/farmerseedcart.html",{'res':res})
def farmerviewproducts(request):

    res=c.execute("select * from product")
    rs=c.fetchall()
    db.commit()
    id=rs[0][0]
    na=rs[0][1]

    return render(request,'farmer/farmerviewproducts.html',{'data':rs})
def farmerproductcart(request):
    email=request.session["username"]
    dates=datetime.today().strftime("%Y-%m-%d")
    
    c.execute("select product.*,productcart.* from product inner join productcart on product.productid=productcart.productid where productcart.email='" + email + "' and productcart.dates='" + dates + "'")
    res=c.fetchall()
    db.commit()
    if request.GET.get("id"):
        id=request.GET.get("id")
        c.execute("delete from productcart where cartno='" + id + "'")
        db.commit()
    if 'checkout' in request.POST:
        
        return HttpResponseRedirect("/farmerproductpayment")

    return render(request,"farmer/farmerproductcart.html",{'res':res})
   
def viewproductinfo(request):
    id=request.GET.get("id")
    res=c.execute("select * from product where productid='"+str(id)+"'")
    rs=c.fetchall()
    db.commit()
    sid=rs[0][0]
    na=rs[0][2]
    da=date.today()
    id=request.GET.get("id")
    if request.POST:
        id=request.POST.get("Name")
        ca=request.POST.get("scientificname")
        qu=request.POST.get("quantity")
        em=request.session["username"]
        re=c.execute("insert into productcart(productid,dates,email) values('"+str(id)+"','"+str(da)+"','"+str(em)+"')")
        db.commit()
        res=c.execute("select * from product")
        rs=c.fetchall()
        db.commit()
        id=rs[0][0]
        na=rs[0][1]
        return render(request,'farmer/FarmerViewproducts.html',{'data':rs})
    return render(request,'farmer/farmerproductpurchase.html',{'id':sid,'ca':na})
def farmerseedpayment(request):
    email=request.session["username"]
    dates=datetime.today().strftime("%Y-%m-%d")
    c.execute("select sum(seed.rate),seedcart.* from seed inner join seedcart on seed.seedid=seedcart.seedid where seedcart.email='" + email + "' and seedcart.dates='" + dates + "'")
    res=c.fetchall()
    db.commit()
    if 'pay' in request.POST:
        print("hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh")
        cardnumber=request.POST.get("cardnumber")
        cvv=request.POST.get("cardnumber")
        accountnumber=request.POST.get("cardnumber")
        ifsc=request.POST.get("ifsc")
        dates=request.POST.get("dates")
        amount=request.POST.get("amount")
        email=request.session["username"]
        user="farmer"
       
        c.execute("insert into seedpayment(cardnumber,cvv,accountnumber,ifsc,amount,dates,user) values('" + cardnumber + "','" + cvv + "','" + accountnumber + "','" + ifsc + "','" + amount + "','" + dates + "','farmer')")
        db.commit()
        return render(request,"farmer/farmer_home.html")
    return render(request,'farmer/seedcartpayment.html',{'res':res})
def farmerproductpayment(request):
    email=request.session["username"]
    dates=datetime.today().strftime("%Y-%m-%d")
    c.execute("select sum(product.rate),product.* from product inner join productcart on product.productid=productcart.productid where productcart.email='" + email + "' and productcart.dates='" + dates + "'")
    res=c.fetchall()
    db.commit()
    if 'pay' in request.POST:
        
        cardnumber=request.POST.get("cardnumber")
        cvv=request.POST.get("cardnumber")
        accountnumber=request.POST.get("cardnumber")
        ifsc=request.POST.get("ifsc")
        dates=request.POST.get("dates")
        amount=request.POST.get("amount")
        email=request.session["username"]
        user="farmer"
       
        c.execute("insert into productpayment(cardnumber,cvv,accountnumber,ifsc,amount,dates,user) values('" + cardnumber + "','" + cvv + "','" + accountnumber + "','" + ifsc + "','" + amount + "','" + dates + "','farmer')")
        db.commit()
        return render(request,"farmer/farmer_home.html")
    return render(request,'farmer/productcartpayment.html',{'res':res})
def publicviewproduct(request):

    res=c.execute("select * from product")
    rs=c.fetchall()
    db.commit()
    id=rs[0][0]
    na=rs[0][1]

    return render(request,'public/publicviewproducts.html',{'data':rs})
def publicviewseed(request):

    res=c.execute("select * from seed")
    rs=c.fetchall()
    db.commit()
    id=rs[0][0]
    na=rs[0][1]

    return render(request,'public/publicViewSeed.html',{'data':rs})
def publicproductcart(request):
    email=request.session["username"]
    dates=datetime.today().strftime("%Y-%m-%d")
    
    c.execute("select product.*,productcart.* from product inner join productcart on product.productid=productcart.productid where productcart.email='" + email + "' and productcart.dates='" + dates + "'")
    res=c.fetchall()
    db.commit()
    if request.GET.get("id"):
        id=request.GET.get("id")
        c.execute("delete from productcart where cartno='" + id + "'")
        db.commit()
    if 'checkout' in request.POST:
        
        return HttpResponseRedirect("/publicproductpayment111")

    return render(request,"public/publicproductcart.html",{'res':res})
def farmerseedcart(request):
    email=request.session["username"]
    dates=datetime.today().strftime("%Y-%m-%d")
    
    c.execute("select seed.*,seedcart.* from seed inner join seedcart on seed.seedid=seedcart.seedid where seedcart.email='" + email + "' and seedcart.dates='" + dates + "'")
    res=c.fetchall()
    db.commit()
    
    if request.GET.get("id"):
        id=request.GET.get("id")
        c.execute("delete from seedcart where cartno='" + id + "'")
        db.commit()
    if 'checkout' in request.POST:
        
        return HttpResponseRedirect("/farmerseedpayment")

    return render(request,"farmer/farmerseedcart.html",{'res':res})
def farmerviewproducts(request):

    res=c.execute("select * from product")
    rs=c.fetchall()
    db.commit()
    id=rs[0][0]
    na=rs[0][1]

    return render(request,'farmer/farmerviewproducts.html',{'data':rs})
def farmerseedcart(request):
    email=request.session["username"]
    dates=datetime.today().strftime("%Y-%m-%d")
    
    c.execute("select seed.*,seedcart.* from seed inner join seedcart on seed.seedid=seedcart.seedid where seedcart.email='" + email + "' and seedcart.dates='" + dates + "'")
    res=c.fetchall()
    db.commit()
    
    if request.GET.get("id"):
        id=request.GET.get("id")
        c.execute("delete from seedcart where cartno='" + id + "'")
        db.commit()
    if 'checkout' in request.POST:
        
        return HttpResponseRedirect("/farmerseedpayment")

    return render(request,"farmer/farmerseedcart.html",{'res':res})
def farmerviewproducts(request):

    res=c.execute("select * from product")
    rs=c.fetchall()
    db.commit()
    id=rs[0][0]
    na=rs[0][1]

    return render(request,'farmer/farmerviewproducts.html',{'data':rs})
def farmerproductcart(request):
    email=request.session["username"]
    dates=datetime.today().strftime("%Y-%m-%d")
    
    c.execute("select product.*,productcart.* from product inner join productcart on product.productid=productcart.productid where productcart.email='" + email + "' and productcart.dates='" + dates + "'")
    res=c.fetchall()
    db.commit()
    if request.GET.get("id"):
        id=request.GET.get("id")
        c.execute("delete from productcart where cartno='" + id + "'")
        db.commit()
    if 'checkout' in request.POST:
        
        return HttpResponseRedirect("/publicproductpayment")

    return render(request,"farmer/farmerproductcart.html",{'res':res})
def publicseedcart(request):
    email=request.session["username"]
    dates=datetime.today().strftime("%Y-%m-%d")
    
    c.execute("select seed.*,seedcart.* from seed inner join seedcart on seed.seedid=seedcart.seedid where seedcart.email='" + email + "' and seedcart.dates='" + dates + "'")
    res=c.fetchall()
    db.commit()
    
    if request.GET.get("id"):
        id=request.GET.get("id")
        c.execute("delete from seedcart where cartno='" + id + "'")
        db.commit()
    if 'checkout' in request.POST:
        
        return HttpResponseRedirect("/publicseedpayment")

    return render(request,"public/publicseedcart.html",{'res':res})
def publicseedpayment(request):
    email=request.session["username"]
    dates=datetime.today().strftime("%Y-%m-%d")
    c.execute("select sum(seed.rate),seedcart.* from seed inner join seedcart on seed.seedid=seedcart.seedid where seedcart.email='" + email + "' and seedcart.dates='" + dates + "'")
    res=c.fetchall()
    db.commit()
    if 'pay' in request.POST:
        print("hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh")
        cardnumber=request.POST.get("cardnumber")
        cvv=request.POST.get("cardnumber")
        accountnumber=request.POST.get("cardnumber")
        ifsc=request.POST.get("ifsc")
        dates=request.POST.get("dates")
        amount=request.POST.get("amount")
        email=request.session["username"]
        user="farmer"
       
        c.execute("insert into seedpayment(cardnumber,cvv,accountnumber,ifsc,amount,dates,user) values('" + cardnumber + "','" + cvv + "','" + accountnumber + "','" + ifsc + "','" + amount + "','" + dates + "','public')")
        db.commit()
        return render(request,"public/public_home.html")
    return render(request,'public/seedcartpayment.html',{'res':res})
def publicproductpayment(request):
    email=request.session["username"]
    dates=datetime.today().strftime("%Y-%m-%d")
    c.execute("select sum(product.rate),product.* from product inner join productcart on product.productid=productcart.productid where productcart.email='" + email + "' and productcart.dates='" + dates + "'")
    res=c.fetchall()
    db.commit()
    if 'pay' in request.POST:
        
        cardnumber=request.POST.get("cardnumber")
        cvv=request.POST.get("cardnumber")
        accountnumber=request.POST.get("cardnumber")
        ifsc=request.POST.get("ifsc")
        dates=request.POST.get("dates")
        amount=request.POST.get("amount")
        email=request.session["username"]
        #user="public"
       
        c.execute("insert into productpayment(cardnumber,cvv,accountnumber,ifsc,amount,dates,user) values('" + cardnumber + "','" + cvv + "','" + accountnumber + "','" + ifsc + "','" + amount + "','" + dates + "','public')")
        db.commit()
        return render(request,"farmer/farmer_home.html")
    return render(request,'farmer/productcartpayment.html',{'res':res})
def publicviewfarmingtech(request):
    c.execute("select * from farmingtechnique")
    res=c.fetchall()
    return render(request,'public/publicviewfarmingtech.html',{'data':res})
def farmerviewfarmingtech(request):
    c.execute("select * from farmingtechnique")
    res=c.fetchall()
    return render(request,'farmer/farmerviewfarmingtech.html',{'data':res})
def supplierreg(request):
    if request.POST and request.FILES.get("uploads"):
       
        suppliersName=request.POST.get("suppliersName")
        RegistraionCode=request.POST.get("RegistraionCode")
        
        Category=request.POST.get("Category")
        District=request.POST.get("District")
        PhoneNumber=request.POST.get("PhoneNumber")
       
        email=request.POST.get("email")
        Password=request.POST.get("password")
        AccountNumber=request.POST.get("AccountNumber")
        BankName=request.POST.get("BankName")
        IFSC=request.POST.get("IFSC")
        res=c.execute("select count(*) as cnt from suppliers where RegistraionCode='" + str(RegistraionCode) + "' or PhoneNumber='" + str(PhoneNumber) + "' or email='" + str(email) + "'")
        rs=c.fetchone()
        db.commit()
        print(rs[0])
        if rs[0]>0:
            msg="already registred"
        else:
            myfile=request.FILES.get("uploads")
            fs=FileSystemStorage()
            filename=fs.save(myfile.name,myfile)
            uploadurl=fs.url(filename)
            status="pending"
            c.execute("insert into suppliers(suppliersName,RegistraionCode,category,District,PhoneNumber,file,email,Password,AccountNumber,BankName,IFSC,status) values('" + str(suppliersName) + "','" + str(RegistraionCode) + "','" + str(Category) + "','" + str(District) + "','" + str(PhoneNumber) + "','" + str(uploadurl) + "','" + str(email) + "','" + str(Password) + "','" + str(AccountNumber) + "','" + str(BankName) + "','" + str(IFSC) + "','" + str(status) + "')")
            usertype="suppliers"
            c.execute("insert into login(username,password,usertype,status) values('"+ email +"','" + Password + "','suppliers','pending')")
            db.commit()
            msg="saved"
    return render(request,'common/suppliersreg.html')
def adminsuppliersapproval(request):
    status="pending"
    c.execute("select * from suppliers where status='pending'")
    res=c.fetchall()
    db.commit()
    if request.GET.get("id"):
        id=request.GET.get("id")
        c.execute("select * from suppliers where sup_regnumber='" + id + "'")
        res1=c.fetchone()
        db.commit()
        email=res1[7]
        c.execute("update suppliers set status='Approved' where sup_regnumber='" + id + "'")
        c.execute("update login set status='Approved' where username='" + email + "'")
        db.commit()
    return render(request,'admin/adminsuppliersapproval.html',{"res":res})
def supplieraddproduct(request):
    c.execute("select * from suppliers")
    rs=c.fetchall()
    if request.POST and request.FILES.get("file1"):
        
        Name=request.POST.get("Name")
        cat=request.POST.get("Category")
        myfile=request.FILES.get("file1")
        fs=FileSystemStorage()
        filename=fs.save(myfile.name,myfile)
        uploadurl=fs.url(filename)
        PName= Name=request.POST.get("PName")
        unit=request.POST.get("unit")
        rate=request.POST.get("rate")
        quantity=request.POST.get("quantity")
        email=request.session["username"]
        c.execute("insert into suppliersproduct(suppliername,cat,productname,file,unit,rate,quantity,email) values('" + Name + "','" + cat + "','" + PName + "','" + uploadurl + "','" + unit + "','" + rate + "','" + quantity + "','" + email + "')")
        db.commit()
    return render(request,'suppliers/suppliersproduct.html',{'data':rs})
def publicpesticideview(request):

    res=c.execute("select * from suppliersproduct where cat='Pesticides'")
    rs=c.fetchall()
    db.commit()
    id=rs[0][0]
    na=rs[0][1]

    return render(request,'farmer/publicviewpesticides.html',{'data':rs})
def viewpesticideinfo(request):
    id=request.GET.get("id")
    res=c.execute("select * from suppliersproduct where productid='"+str(id)+"'")
    rs=c.fetchall()
    db.commit()
    sid=rs[0][0]
    na=rs[0][3]
    da=date.today()
    id=request.GET.get("id")
    if request.POST:
        id=request.POST.get("Name")
        ca=request.POST.get("scientificname")
        qu=request.POST.get("quantity")
        em=request.session["username"]
        re=c.execute("insert into pesticidecart(productid,dates,email,status) values('"+str(id)+"','"+str(da)+"','"+str(em)+"','pending')")
        db.commit()
        res=c.execute("select * from suppliersproduct")
        rs=c.fetchall()
        db.commit()
        id=rs[0][0]
        na=rs[0][1]
        return render(request,'farmer/publicviewpesticides.html',{'data':rs})
    return render(request,'farmer/publicpurchasepesticides.html',{'id':sid,'ca':na})
def publicpesticidecart(request):
    email=request.session["username"]
    dates=datetime.today().strftime("%Y-%m-%d")
    
    c.execute("select suppliersproduct.*,pesticidecart.* from suppliersproduct inner join pesticidecart on suppliersproduct.productid=pesticidecart.productid where pesticidecart.email='" + email + "' and pesticidecart.dates='" + dates + "'")
    res=c.fetchall()
    db.commit()
    if request.GET.get("id"):
        id=request.GET.get("id")
        c.execute("delete from pesticidecart where cartno='" + id + "'")
        db.commit()
    if 'checkout' in request.POST:
        
        return HttpResponseRedirect("/pesticidecartpayment")

    return render(request,"farmer/publicpesticideecart.html",{'res':res})
def pesticidecartpayment(request):
    email=request.session["username"]
    dates=datetime.today().strftime("%Y-%m-%d")
    c.execute("select sum(suppliersproduct.rate),pesticidecart.* from suppliersproduct inner join pesticidecart on suppliersproduct.productid=pesticidecart.productid where pesticidecart.email='" + email + "' and pesticidecart.dates='" + dates + "'")
    res=c.fetchall()
    db.commit()
    if 'pay' in request.POST:
        
        cardnumber=request.POST.get("cardnumber")
        cvv=request.POST.get("cardnumber")
        accountnumber=request.POST.get("cardnumber")
        ifsc=request.POST.get("ifsc")
        dates=request.POST.get("dates")
        amount=request.POST.get("amount")
        email=request.session["username"]
        user="farmer"
       
        c.execute("insert into pesticidepayment(cardnumber,cvv,accountnumber,ifsc,amount,dates,user) values('" + cardnumber + "','" + cvv + "','" + accountnumber + "','" + ifsc + "','" + amount + "','" + dates + "','public')")
        db.commit()
        return HttpResponseRedirect("/farmer_home")
    return render(request,"farmer/pesticidecartpayment.html",{'res':res})
def publiceviewquipment(request):
    res=c.execute("select * from suppliersproduct where cat='Equipments'")
    rs=c.fetchall()
    db.commit()
    id=rs[0][0]
    na=rs[0][1]

    return render(request,'farmer/publicviewequpmentview.html',{'data':rs})
def viewequipmentinfo(request):
    id=request.GET.get("id")
    res=c.execute("select * from suppliersproduct where productid='"+str(id)+"'")
    rs=c.fetchall()
    db.commit()
    sid=rs[0][0]
    na=rs[0][3]
    da=date.today()
    id=request.GET.get("id")
    if request.POST:
        id=request.POST.get("Name")
        ca=request.POST.get("scientificname")
        qu=request.POST.get("quantity")
        em=request.session["username"]
        re=c.execute("insert into equipmentcart(productid,dates,email,status) values('"+str(id)+"','"+str(da)+"','"+str(em)+"','pending')")
        db.commit()
        res=c.execute("select * from suppliersproduct where cat='Equipments'")
        rs=c.fetchall()
        db.commit()
        id=rs[0][0]
        na=rs[0][1]
        return render(request,'farmer/publicviewequpmentview.html',{'data':rs})
    return render(request,'farmer/publicpurchaseequeipment.html',{'id':sid,'ca':na})
def publicpesticidecart(request):
    email=request.session["username"]
    dates=datetime.today().strftime("%Y-%m-%d")
    
    c.execute("select suppliersproduct.*,pesticidecart.* from suppliersproduct inner join pesticidecart on suppliersproduct.productid=pesticidecart.productid where pesticidecart.email='" + email + "' and pesticidecart.dates='" + dates + "'")
    res=c.fetchall()
    db.commit()
    if request.GET.get("id"):
        id=request.GET.get("id")
        c.execute("delete from pesticidecart where cartno='" + id + "'")
        db.commit()
    if 'checkout' in request.POST:
        
        return HttpResponseRedirect("/pesticidecartpayment")

    return render(request,"farmer/publicpesticideecart.html",{'res':res})

def publicequpmentcart(request):
    email=request.session["username"]
    dates=datetime.today().strftime("%Y-%m-%d")
    
    c.execute("select suppliersproduct.*,equipmentcart.* from suppliersproduct inner join equipmentcart on suppliersproduct.productid=equipmentcart.productid where equipmentcart.email='" + email + "' and equipmentcart.dates='" + dates + "'")
    res=c.fetchall()
    db.commit()
    if request.GET.get("id"):
        id=request.GET.get("id")
        c.execute("delete from equipmentcart where cartno='" + id + "'")
        db.commit()
    if 'checkout' in request.POST:
        
        return HttpResponseRedirect("/equipmentcartpayment")

    return render(request,"farmer/publicpesticideecart.html",{'res':res})
def equipmentcartpayment(request):
    email=request.session["username"]
    dates=datetime.today().strftime("%Y-%m-%d")
    c.execute("select sum(suppliersproduct.rate),pesticidecart.* from suppliersproduct inner join pesticidecart on suppliersproduct.productid=pesticidecart.productid where pesticidecart.email='" + email + "' and pesticidecart.dates='" + dates + "'")
    res=c.fetchall()
    db.commit()
    if 'pay' in request.POST:
        
        cardnumber=request.POST.get("cardnumber")
        cvv=request.POST.get("cardnumber")
        accountnumber=request.POST.get("cardnumber")
        ifsc=request.POST.get("ifsc")
        dates=request.POST.get("dates")
        amount=request.POST.get("amount")
        email=request.session["username"]
        user="farmer"
       
        c.execute("insert into pesticidepayment(cardnumber,cvv,accountnumber,ifsc,amount,dates,user) values('" + cardnumber + "','" + cvv + "','" + accountnumber + "','" + ifsc + "','" + amount + "','" + dates + "','public')")
        db.commit()
    return render(request,"farmer/publicequipmentpayment.html",{'res':res})
def pesticidecartpayment(request):
    email=request.session["username"]
    dates=datetime.today().strftime("%Y-%m-%d")
    c.execute("select sum(suppliersproduct.rate),pesticidecart.* from suppliersproduct inner join pesticidecart on suppliersproduct.productid=pesticidecart.productid where pesticidecart.email='" + email + "' and pesticidecart.dates='" + dates + "'")
    res=c.fetchall()
    db.commit()
    if 'pay' in request.POST:
        
        cardnumber=request.POST.get("cardnumber")
        cvv=request.POST.get("cardnumber")
        accountnumber=request.POST.get("cardnumber")
        ifsc=request.POST.get("ifsc")
        dates=request.POST.get("dates")
        amount=request.POST.get("amount")
        email=request.session["username"]
        user="farmer"
       
        c.execute("insert into pesticidepayment(cardnumber,cvv,accountnumber,ifsc,amount,dates,user) values('" + cardnumber + "','" + cvv + "','" + accountnumber + "','" + ifsc + "','" + amount + "','" + dates + "','public')")
        db.commit()
        return HttpResponseRedirect("/farmer_home/")
    return render(request,"public/pesticidecartpayment.html",{'res':res})
def publicequipmentcartpayment(request):
    email=request.session["username"]
    dates=datetime.today().strftime("%Y-%m-%d")
    c.execute("select sum(suppliersproduct.rate),equipmentcart.* from suppliersproduct inner join equipmentcart on suppliersproduct.productid=equipmentcart.productid where equipmentcart.email='" + email + "' and equipmentcart.dates='" + dates + "'")
    res=c.fetchall()
    db.commit()
    if 'pay' in request.POST:
        
        cardnumber=request.POST.get("cardnumber")
        cvv=request.POST.get("cardnumber")
        accountnumber=request.POST.get("cardnumber")
        ifsc=request.POST.get("ifsc")
        dates=request.POST.get("dates")
        amount=request.POST.get("amount")
        email=request.session["username"]
        user="farmer"
       
        c.execute("insert into equipmentpayment(cardnumber,cvv,accountnumber,ifsc,amount,dates,user) values('" + cardnumber + "','" + cvv + "','" + accountnumber + "','" + ifsc + "','" + amount + "','" + dates + "','public')")
        db.commit()
    return render(request,"public/publicequipmentpayment.html",{'res':res})
def suppliersviewpesticide(request):
    c.execute("select * from  pesticidecart where status='pending'")
    res=c.fetchall()
    if request.GET.get("id"):
        id=request.GET.get("id")
        c.execute("update pesticidecart set status='Approve' where cartno='" + id + "'")
        db.commit()
    return render(request,'suppliers/supplierviewpesticide.html',{'data':res})
def suppliersviewequipment(request):
    c.execute("select * from  equipmentcart where status='pending'")
    res=c.fetchall()
    if request.GET.get("id"):
        id=request.GET.get("id")
        c.execute("update equipmentcart set status='Approve' where cartno='" + id + "'")
        db.commit()
    return render(request,'suppliers/supplierviewequipment.html',{'data':res})
def adminaddinvestors(request):
    msg=""
    res=0
    res1=0
    if request.POST:
        print("hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh")
        Name=request.POST.get("Name")
        Email=request.POST.get("Email")
        MobileNumber=request.POST.get("MobileNumber")
        OfficeName=request.POST.get("OfficeName")
        OfficeContact=request.POST.get("OfficeContact")
        Designation=request.POST.get("Designation")
        Specialized=request.POST.get("Specialized")
        Message=request.POST.get("Message")
        res=c.execute("select count(*) as cnt from  investors where Email='" + str(Email) + "' or MobileNumber='" + str(MobileNumber) + "'or OfficeContact='" + str(OfficeContact) + "'")
        res=c.fetchone()
       
      
        if res[0]>0:
            msg="alreadyregistred"
        else:
            status="Approved"
            usertype="investor"
            c.execute("insert into  investors(Name,Email,MobileNumber,OfficeName,OfficeContact,Designation,Specialized,Message) values('"+ str(Name) +"','"+ str(Email) +"','"+ str(MobileNumber) +"','"+ str(OfficeName) +"','"+ str(OfficeContact) +"','"+ str(Designation) +"','"+ str(Specialized) +"','"+ str(Message) +"')")
           
            db.commit()
            msg="saved"

   
    return render(request,'admin/adminaddinvesters.html')
def farmeraddcapital(request):
    if request.POST:
        Name=request.POST.get("Name")
        Mobile=request.POST.get("Mobile")
        Amount=request.POST.get("Amount")
        email=request.session["username"]
        dates=datetime.today().strftime("%Y-%m-%d")
        c.execute("insert into farmentcapitalrequest(name,mobile,amount,email,dates) values('" + Name + "','" + Mobile + "','" + Amount + "','" + email + "','" + dates + "')")
        db.commit()
    return render(request,'farmer/farmeraddforcapital.html')
def adminviewcapital(request):
    c.execute("select * from  farmentcapitalrequest")
    res=c.fetchall()


    return render(request,'admin/adminviewcapital.html',{'data':res})
def addfeedback(request):
    if request.POST:
        Name=request.POST.get("Name")
        Mobile=request.POST.get("Mobile")
        Feedback=request.POST.get("Feedback")
        email=request.session["username"]
        dates=datetime.today().strftime("%Y-%m-%d")
        c.execute("insert into feedback(name,mobile,email,dates,feedback) values('" + Name + "','" + Mobile + "','" + email + "','" + dates + "','" + Feedback + "')")
        db.commit()
    return render(request,'public/feedback.html')
def adminviewfeedback(request):
    c.execute("select * from  feedback")
    res=c.fetchall()
    return render(request,'admin/adminviewfeedback.html',{'data':res})
def adminfarmerapprovedview(request):
    status="Pending"
    c.execute("select * from farmerreg where status='Approved'")
    res=c.fetchall()
    return render(request,'admin/adminfarmerapprovedview.html',{"res":res})
def adminsupplierapproved(request):
   c.execute("select * from suppliers where status='Approved'")
   res=c.fetchall()
   db.commit()
   return render(request,'admin/adminsupplierapproved.html',{"res":res})
def adminexportersapproved(request):
    c.execute("select * from exporters where status='Approved'")
    res=c.fetchall()
    db.commit()
    return render(request,'admin/adminexportersapproved.html',{"res":res})
def adminviewproduct(request):
    c.execute("select * from product")
    res=c.fetchall()
    db.commit()
    return render(request,'admin/adminviewproduct.html',{"res":res})
def admminviewseed(request):
    c.execute("select * from seed")
    res=c.fetchall()
    db.commit()
    return render(request,'admin/admminviewseed.html',{"res":res})
def adminviewequeipment(request):
    c.execute("select * from suppliersproduct")
    res=c.fetchall()
    db.commit()
    return render(request,'admin/adminviewequeipment.html',{"res":res})
def farmerprofile(request):
    Username=request.session["username"]
    print("select * from farmerreg where email='" + Username + "'")
    c.execute("select * from farmerreg where email='" + Username + "'")
    res=c.fetchone()
    db.commit()
    if request.POST:
        FarmersName=request.POST.get("FarmersName")
        HouseName=request.POST.get("HouseName")
        State=request.POST.get("State")
        District=request.POST.get("District")
        panchayath=request.POST.get("panchayath")
        Postoffice=request.POST.get("Postoffice")
        PostalZipCode=request.POST.get("PostalZipCode")
        email=request.POST.get("email")
        PhoneNumber=request.POST.get("PhoneNumber")
        password=request.POST.get("password")
        status="Pending"
        AccountNumber=request.POST.get("AccountNumber")
        NameoftheBank=request.POST.get("NameoftheBank")
        IFSC=request.POST.get("IFSC")
        #myfile=request.FILES.get("uploads")
        #fs=FileSystemStorage()
        #filename=fs.save(myfile.name,myfile)
        #uploadurl=fs.url(filename)
        c.execute("update farmerreg set FarmersName='" + str(FarmersName) +"',HouseName='" + str(HouseName) + "',State='" + str(State) + "',District='" + str(District) + "',panchayath='" + str(panchayath) + "',Postoffice='" + str(Postoffice) + "',PostalZipCode='" + str(PostalZipCode) + "',email='" + str(email) + "',phonenumber='" + str(PhoneNumber) + "',password='" + str(password) + "',AccountNumber='" + str(AccountNumber) + "',NameoftheBank='" + str(NameoftheBank) + "',IFSC='" + str(IFSC) + "' where email='" + str(email) + "'")
        db.commit()
        
        msg="saved"
    return render(request,'farmer/farmerprofile.html',{"data":res})
def viewpesticideinfo(request):
    id=request.GET.get("id")
    res=c.execute("select * from suppliersproduct where productid='"+str(id)+"'")
    rs=c.fetchall()
    db.commit()
    sid=rs[0][0]
    na=rs[0][3]
    da=date.today()
    id=request.GET.get("id")
    if request.POST:
        id=request.POST.get("Name")
        ca=request.POST.get("scientificname")
        qu=request.POST.get("quantity")
        em=request.session["username"]
        re=c.execute("insert into pesticidecart(productid,dates,email,status) values('"+str(id)+"','"+str(da)+"','"+str(em)+"','pending')")
        db.commit()
        res=c.execute("select * from suppliersproduct where cat='Pesticides'")
        rs=c.fetchall()
        db.commit()
        id=rs[0][0]
        na=rs[0][1]
        return render(request,'farmer/publicviewpesticides.html',{'data':rs})
    return render(request,'farmer/publicpurchasepesticides.html',{'id':sid,'ca':na})
def farmerviewdoubtreplay(request):
    username=request.session["username"]
    print("hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh")
    print("select * from doubtreplay where email='" + username + "'")
    c.execute("select * from doubtreplay where email='" + username + "'")
    res=c.fetchall()
    return render(request,"farmer/farmerfinalyviewdoughtreplay.html",{'data':res})
def publicviewproductinfo(request):
    id=request.GET.get("id")
    res=c.execute("select * from product where productid='"+str(id)+"'")
    rs=c.fetchall()
    db.commit()
    sid=rs[0][0]
    na=rs[0][2]
    da=date.today()
    id=request.GET.get("id")
    if request.POST:
        id=request.POST.get("Name")
        ca=request.POST.get("scientificname")
        qu=request.POST.get("quantity")
        em=request.session["username"]
        re=c.execute("insert into productcart(productid,dates,email) values('"+str(id)+"','"+str(da)+"','"+str(em)+"')")
        db.commit()
        res=c.execute("select * from product")
        rs=c.fetchall()
        db.commit()
        id=rs[0][0]
        na=rs[0][1]
        return render(request,'public/publicviewproducts.html',{'data':rs})
    return render(request,'public/publicproductpurchase.html',{'id':sid,'ca':na})

def publicproductpayment111(request):
    email=request.session["username"]
    dates=datetime.today().strftime("%Y-%m-%d")
    c.execute("select sum(product.rate),product.* from product inner join productcart on product.productid=productcart.productid where productcart.email='" + email + "' and productcart.dates='" + dates + "'")
    res=c.fetchall()
    db.commit()
    if 'pay' in request.POST:
        
        cardnumber=request.POST.get("cardnumber")
        cvv=request.POST.get("cardnumber")
        accountnumber=request.POST.get("cardnumber")
        ifsc=request.POST.get("ifsc")
        dates=request.POST.get("dates")
        amount=request.POST.get("amount")
        email=request.session["username"]
        #user="public"
       
        c.execute("insert into productpayment(cardnumber,cvv,accountnumber,ifsc,amount,dates,user) values('" + cardnumber + "','" + cvv + "','" + accountnumber + "','" + ifsc + "','" + amount + "','" + dates + "','public')")
        db.commit()
        return render(request,"public/public_home.html")
    return render(request,'public/productcartpayment.html',{'res':res})
def publicviewseedinfo(request):
    id=request.GET.get("id")
    res=c.execute("select * from seed where seedid='"+str(id)+"'")
    rs=c.fetchall()
    db.commit()
    sid=rs[0][0]
    na=rs[0][1]
    da=date.today()
    id=request.GET.get("id")
    if request.POST:
        id=request.POST.get("Name")
        ca=request.POST.get("scientificname")
        qu=request.POST.get("quantity")
        em=request.session["username"]
        re=c.execute("insert into seedcart(seedid,dates,email) values('"+str(id)+"','"+str(da)+"','"+str(em)+"')")
        db.commit()
        res=c.execute("select * from seed")
        rs=c.fetchall()
        db.commit()
        id=rs[0][0]
        na=rs[0][1]
        return render(request,'public/publicViewSeed.html',{'data':rs})
    return render(request,'public/publicpurchaseseed.html',{'id':sid,'ca':na})
def Adminviewspecialists(request):
    c.execute("select * from specialized")
    res=c.fetchall()
    return render(request,'admin/Adminviewspecialist.html',{'res':res})
def Adminviewinvestors(request):
    c.execute("select * from investors")
    res=c.fetchall()
    return render(request,'admin/Adminviewinvesters.html',{'res':res})