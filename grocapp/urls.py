from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('login/',views.login, name='login'),
    path('contact/', views.contact, name='contact'),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('signout/', views.signout, name='signout'),
    path('why/', views.why, name='why'),
    path('mail/', views.mail, name='mail'),
    path('cart/', views.cart, name='cart'),
    path('testimonial/',views.testimonial, name='testimonial'),
    path('list/',views.list, name='list'),
    path('address/',views.address, name='address'),
    path('myorder/',views.myorder, name='myorder'),
    path('updateitm/',views.updateitem, name='updateitm'),
    path('category/<str:foo>',views.category, name='category'),
    path('searchbar/',views.searchbar, name='searchbar'),
    path('checkout/',views.checkout, name='checkout'),
    path('change_password/', views.change_password, name='change_password'),
    path('processOrder/',views.processOrder, name='processOrder'), 
    path('charge',views.charge, name='charge'),
    path('productdetails/<int:product_id>/',views.productdetails, name='productdetails'),
    path('orderdetails/<int:product_id>/',views.orderdetails, name='orderdetails'),
   

]