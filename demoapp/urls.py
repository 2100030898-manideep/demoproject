from django.urls import path
from . import views

# . represents current directory

urlpatterns = [
    path("",views.indexfunction,name="index"),
    path("formdemo",views.formdemofunction,name="formdemo"),
    path("displayform",views.displayformdatafunction,name="displayform"),
    path("logindemo",views.logindemofunction,name="logindemo"),
path("checklogindemo",views.checklogindemofunction,name="checklogindemo"),
path("addemployee",views.addemployeefunction,name="addemployee"),
path("saveemployee",views.saveemployeefunction,name="saveemployee"),

    path("registration",views.registration,name="registration"),
    path("userlogin",views.userlogin,name="userlogin"),
    path("checkuserlogin",views.checkuserlogin,name="checkuserlogin"),

path("userhome",views.userhome,name="userhome"),
path("userlogout",views.userlogout,name="userlogout"),
    path("viewusers",views.viewusers,name="viewusers")

]