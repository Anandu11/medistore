from django.urls import path
from mstore import views
urlpatterns=[
    path('home/',views.home.as_view(),name="home"),
    path('Category/<int:pk>',views.Category_detail.as_view(),name="category_detail"),
    path("product_detail/<int:pk>",views.Product_detail.as_view(),name="p_det"),
    path("addtocart/<int:pk>",views.Addtocartview.as_view(),name="cart"),
    path("register/",views.Registerview.as_view(),name="register"),
    path("login/",views.signinview.as_view(),name="login"),
    path("logout/",views.signout.as_view(),name="log_out"),
    path("delete/<int:pk>",views.Cart_deleteview.as_view(),name="delete"),
    path("cart/",views.Cart_detailview.as_view(),name="cart"),
    path("order/<int:pk>",views.orderview.as_view(),name="order"),
    path('orderview/',views.vieworder.as_view(),name="view_order"),
    path('searchview/',views.SearchView.as_view(),name="srch"),
    

    

    
    
    
]