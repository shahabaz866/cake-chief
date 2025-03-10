from django.urls import path,re_path
from . import views
from django.views.decorators.cache import never_cache
from django.shortcuts import render

# @never_cache
# def catch_all_view(request, path=None):
#     return render(request, 'user_side/error/error_page.html',{'error_code': 404},status=404)

urlpatterns =[
            
    path('',views.HomePage,name='home'),
    path('shop/flavor/<int:flavor_id>/', views.shoplist, name='flavor_filter'),
    path('shop/category/<int:category_id>/', views.shoplist, name='shop_by_category'),
    path('shop/', views.shoplist, name='shop'), 
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    path('contact/',views.contact,name='contact'),
    path('about/',views.about,name='about'),
    path('verify_otp/', views.verify_otp, name='verify_otp'), 
    path('resend-otp/', views.resend_otp, name='resend_otp'),
    path('login/',views.LogingPage,name='login'),
    path('forgot-password/', views.forgot_password, name='forgot_password'),
    path('password-reset-confirm/<uidb64>/<token>/', views.password_reset_confirm, name='password_reset_confirm'),
    path('reviews/', views.review_list, name='review_list'),
    path('reviews/create/', views.create_review, name='create_review'),
    path('reviews/<int:review_id>/helpful/', views.vote_helpful, name='vote_helpful'),
    path('delete-review/<int:review_id>/', views.delete_review, name='delete_review'),
    path('logout/',views.LogoutPage,name='logout'),
    path('signup/', views.SignupPage, name='SignupPage'),
    path('product/<int:product_id>/review/', views.add_review, name='add_review'),
    path('review/<int:review_id>/delete/', views.delete_review, name='delete_review'),
    path('review/<int:review_id>/helpful/', views.helpful_review, name='helpful_review'),
    
# re_path(r'^.*$', catch_all_view),
]
