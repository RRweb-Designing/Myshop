"""
URL configuration for online_shopping project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.conf import settings
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from Home_App import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('electronic/',views.electronic),
    path('fashion/',views.fashion),
    path('grocery/',views.grocery),
    path('signin/', views.signin),
    path('signincode/', views.signincode),
    path('userdashboard/', views.userdashboard),

    path('signup/', views.signup),
    path('signupinsert/', views.signupinsert),

    path('about/', views.about),
    path('contact/', views.contact),
    path('product/', views.product),
    # path('addimg/', views.addimg),
    path('addimgcode/', views.addimgcode),

    path('forget/', views.forget),
    path('otp/', views.otp),
    path('newpassword/', views.newpassword),
    path('checkemail/', views.checkemail),
    path('otpcode/', views.otpcode),
    # path('newpasswordcode/',views.newpasswordcode),
    path('updatepassword/', views.updatepassword),
    path('show/',views.show),

    path('delete/<int:id>', views.delete),
    path('deletecontact/<int:id>', views.deletecontact),
    path('deleteuser/<int:id>', views.deleteuser),
    path('deletorder/<int:id>', views.deletorder),
    # path('deleteproduct/<int:id>', views.deleteproduct),

    # path('edit/',views.edit),
    path('editcode/<int:id>',views.editcode),
    path('updatedata/', views.updatedata),
    # path('panal/', views.panal),
    path('login/', views.login),
    path('loginpanapinsert/',views.loginpanapinsert),
    path('logincode/',views.logincode),

    path('showuser/',views.showuser),
    # path('edituser/', views.edituser),
    path('editusercode/<int:id>',views.editusercode),
    path('updateuser/',views.updateuser),

    path('contactinsert/',views.contactinsert),
    path('showcontact/',views.showcontact),

    path('order/',views.order),
    path('orderinsert/',views.orderinsert),
    path('showorder/',views.showorder),

    path('addcategorycode/', views.addcategorycode),
    path('deletcate/<int:id>', views.deletcate),
    path('editcate/',views.editcate),
    path('editcatecode/<int:id>',views.editcatecode),
    path('updatecate/',views.updatecate),
    path('showcatep/',views.showcatep),
    path('index/',views.index),

path('forgetadmin/',views.forgetadmin),
path('adminotp/',views.adminotp),
path('adminnewpassword/',views.adminnewpassword),
path('admincheckemail/',views.admincheckemail),
path('adminotpcode/',views.adminotpcode),
# path('newadminpasswordcode/',views.newadminpasswordcode),
path("adminupdatepassword/",views.adminupdatepassword),
    # path('test/',views.test),
path('search/',views.search),
path('searchcode/<int:id>',views.search),


                  path('addbrandcode/',views.addbrandcode),
                  path('deletbrand/<int:id>', views.deletbrand),
                  path('editbrand/',views.editbrand),
                  path('editbrandcode/<int:id>', views.editbrandcode),
                  path('updatebrand/',views.updatebrand),
                  path('showbrandp/',views.showbrandp),
                  # path('index2/',views.index2),

# path('showslider/', views.showslider),
path('addslidercode/', views.addslidercode),
path('showslider/', views.showslider),
path('deleteslider/<int:id>', views.deleteslider),
path('editslidercode/<int:id>',views.editslidercode),
path('updateslider/', views.updateslider),

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


