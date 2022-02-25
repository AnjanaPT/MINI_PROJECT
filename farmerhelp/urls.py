"""farmerhelp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from appme import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('admin_home/',views.admin_home),
    path('admin_about/',views.admin_about),
    path('farmer_home/',views.farmer_home),
    path('exporters_home/',views.exporters_home),
    path('specialist_home/',views.specialist_home),
    path('public_home/',views.public_home),

    path('common_register/',views.common_register),
    
    path('farmerreg/',views.farmerreg,name="farmerreg"),
    path('Exportersreg/',views.Exportersreg,name="Exportersreg"),
    path('publicreg/',views.publicreg,name='publicreg'),

    path('adminpublicapproval/',views.adminpublicapproval,name='adminpublicapproval'),
    path('adminfarmerapproval/',views.adminfarmerapproval,name='adminfarmerapproval'),
    path('adminExportersapproval/',views.adminExportersapproval,name='adminExportersapproval'),
    path('admin_addSpecialist/',views.admin_addSpecialist,name='admin_addSpecialist'),
    path('admin_farmer_payment/',views.admin_farmer_payment,name='admin_farmer_payment'),
    path('paymentaction/',views.paymentaction,name='paymentaction'),
   
    path('admincategoryadd/',views.admincategoryadd,name='admincategoryadd'),
    path('farmeraddproduct/',views.farmeraddproduct,name='farmeraddproduct'),
    path('farmeraddseed/',views.farmeraddseed,name='farmeraddseed'),
    path('farmeraddfamingtech/',views.farmeraddfamingtech,name='farmeraddfamingtech'),
    path('testingresult/',views.testingresult,name='testingresult'),
    path('farmeradddought/',views.farmeradddought,name='farmeradddought'),
    path('viewdouhtsbyspecialist/',views.viewdouhtsbyspecialist,name='viewdouhtsbyspecialist'),
    path('viewdoubtreplay/',views.viewdoubtreplay,name='viewdoubtreplay'),
    path('addexportrequest/',views.addexportrequest,name='addexportrequest'),
    path('adminexportersorderview/',views.adminexportersorderview,name='adminexportersorderview'),
    path('exportersaddorderrequest/',views.exportersaddorderrequest,name='exportersaddorderrequest'),
    path('farmerviewseed/',views.farmerviewseed,name='farmerviewseed'),
    path('viewseedinfo/',views.viewseedinfo,name='viewseedinfo'),
    path('addexportrequest/',views.addexportrequest,name='addexportrequest'),
    path('exporterspayment/',views.exporterspayment,name='exporterspayment'),
    path('farmerseedcart/',views.farmerseedcart,name='farmerseedcart'),
    path('farmerviewproducts/',views.farmerviewproducts,name='farmerviewproducts'),
    path('farmerproductcart/',views.farmerproductcart,name='farmerproductcart'),
    path('viewproductinfo/',views.viewproductinfo,name='viewproductinfo'),
    path('farmerseedpayment/',views.farmerseedpayment,name='farmerseedpayment'),
    path('farmerproductpayment/',views.farmerproductpayment,name='farmerproductpayment'),
    path('publicviewproduct/',views.publicviewproduct,name='publicviewproduct'),
    path('publicviewseed/',views.publicviewseed,name='publicviewseed'),
    path('publicproductcart/',views.publicproductcart,name='publicproductcart'),
    path('publicseedcart/',views.publicseedcart,name='publicseedcart'),
    path('publicseedpayment/',views.publicseedpayment,name='publicseedpayment'),
    path('publicproductpayment/',views.publicproductpayment,name='publicproductpayment'),
    path('publicviewfarmingtech/',views.publicviewfarmingtech,name='publicviewfarmingtech'),
    path('farmerviewfarmingtech/',views.farmerviewfarmingtech,name='farmerviewfarmingtech'),
    path('supplierreg/',views.supplierreg,name="supplierreg"),
    path('adminsuppliersapproval/',views.adminsuppliersapproval,name='adminsuppliersapproval'),
    path('suppliers_home/',views.suppliers_home,name='suppliers_home'),
    path('supplieraddproduct/',views.supplieraddproduct,name='supplieraddproduct'),
    path('publicpesticideview/',views.publicpesticideview,name='publicpesticideview'),
    path('viewpesticidesinfo/',views.viewpesticideinfo,name='viewpesticidesinfo'),
    path('publicpesticidecart/',views.publicpesticidecart,name='publicpesticidecart'),
    path('pesticidecartpayment/',views.pesticidecartpayment,name='pesticidecartpayment'),
    path('publiceviewquipment/',views.publiceviewquipment,name='publiceviewquipment'),
    path('viewequipmentinfo/',views.viewequipmentinfo,name='viewequipmentinfo'),
    path('publicequpmentcart/',views.publicequpmentcart,name='publicequpmentcart'),
    path('equipmentcartpayment/',views.equipmentcartpayment,name='equipmentcartpayment'),
    
    path('suppliersviewpesticide/',views.suppliersviewpesticide,name='suppliersviewpesticide'),
    path('suppliersviewequipment/',views.suppliersviewequipment,name='suppliersviewequipment'),
    path('adminaddinvestors/',views.adminaddinvestors,name='adminaddinvestors'),
    path('farmeraddcapital/',views.farmeraddcapital,name='farmeraddcapital'),
    path('adminviewcapital/',views.adminviewcapital,name='adminviewcapital'),
    path('addfeedback/',views.addfeedback,name='addfeedback'),
    path('adminviewfeedback/',views.adminviewfeedback,name='adminviewfeedback'),
    path('adminfarmerapprovedview/',views.adminfarmerapprovedview,name="adminfarmerapprovedview"),
    path('adminsupplierapproved/',views.adminsupplierapproved,name="adminsupplierapproved"),
    path('adminexportersapproved/',views.adminexportersapproved,name="adminexportersapproved"),
    path('adminviewproduct/',views.adminviewproduct,name="adminviewproduct"),
    path('admminviewseed/',views.admminviewseed,name="admminviewseed"),
    path('adminviewequeipment/',views.adminviewequeipment,name="adminviewequeipment"),
  path('farmerprofile/',views.farmerprofile,name="farmerprofile"),
    path('farmerviewdoubtreplay/',views.farmerviewdoubtreplay,name="farmerviewdoubtreplay"),
    path('publicviewproductinfo/',views.publicviewproductinfo,name="publicviewproductinfo"),
    path('publicproductpayment111/',views.publicproductpayment111,name="publicproductpayment111"),
    path('publicviewseedinfo/',views.publicviewseedinfo,name="publicviewseedinfo"),
    path('Adminviewspecialists/',views.Adminviewspecialists,name="Adminviewspecialists"),
    path('Adminviewinvestors/',views.Adminviewinvestors,name="Adminviewinvestors"),
]

