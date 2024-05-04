from django.shortcuts import render,redirect
from django.views.generic import View
from mstore.models import Category, Order,Product, cart
from django.urls import reverse_lazy
from django.views.generic import View,ListView,CreateView
from mstore.forms import Loginform, Register, orderform
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.utils.decorators import method_decorator

# Create your views here.
class home(ListView):
    model=Category
    template_name="mstore\index.html"
    context_object_name="categories"   
    
class Category_detail(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        data=Product.objects.filter(category_id=id)
        name=Category.objects.get(id=id)
        return render(request,"mstore/category_detail.html",{"data":data,"name":name})

class Product_detail(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        data=Product.objects.get(id=id)
        return render(request,"mstore/p_detail.html",{"data":data})
    
class Registerview(CreateView):
    template_name="mstore/register.html"
    form_class=Register
    mode=User
    sucess_url=reverse_lazy("home")

class signinview(View):
    def get(self,request,*args,**kwargs):
        form=Loginform()
        return render(request,"mstore/login.html",{"form":form})
    
    def post(self,request,*args,**kwargs):
        form=Loginform(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            u_name=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            user_obj=authenticate(request,username=u_name,password=pwd)
            if user_obj:
                login(request,user_obj)
                return redirect("home")
            else:
               print("false credentials")
        return redirect("register")
    
class signout(View):
    def get(self,request,*args,**kwargs):
        logout(request)
        return redirect("home")  
    

class Addtocartview(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        data=Product.objects.get(id=id)
        cart.objects.create(item=data,user=request.user)
        print("added successfully")
        return redirect("home")

class Cart_deleteview(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        cart.objects.get(id=id).delete()
        return redirect("home")
    
def signin_required(fn):
    def wrapper(request,*args,**kwargs):
        if not request.user.is_authenticated:
            return redirect("login")
        else:
            return fn(request,*args,**kwargs)
    return wrapper         
     

@method_decorator(signin_required,name="dispatch")  
class Cart_detailview(View):
    def get(self,request,*args,**kwargs):
        data=cart.objects.filter(user=request.user)
        return render(request,"mstore/cart.html",{"data":data})   

class orderview(View):
    def get(self,request,*args,**kwargs):
        form=orderform()
        return render(request,"mstore/orderpage.html",{"form":form})
    
    def post(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        data=Product.objects.get(id=id)
        form=orderform(request.POST)
        if form.is_valid():
            qs=form.cleaned_data.get("address")
            Order.objects.create(address=qs,order_item=data,customer=request.user)
            return redirect("home")
        return redirect("cart")

class vieworder(View):
    def get(self,request,*args,**kwargs):
        data=Order.objects.filter(customer=request.user)
        return render(request,"mstore/view_order.html",{"data":data})
    
class Remove_order(View):
     def get(self,request,*args,**kwargs):
         id=kwargs.get("pk")
         Order.objects.get(id=id).delete()
         return redirect("cart")

class SearchView(View):
    def get(self,request,*args,**kwargs):
        query=request.GET.get('q')
        if query:
            results=Product.objects.filter(name__icontains=query)
        else:
            results=None
        return render(request,'mstore/search_results.html',{'results':results})