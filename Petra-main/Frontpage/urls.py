from django.urls import path
from Frontpage import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('about/',views.about,name='about'),
    path('products/',views.products,name='products'),
    path('findDealers/',views.findDealers,name='findDealers'),
    path('becomeDealer/',views.becomeDealer,name='becomeDealer'),
    path('complaint/', views.registerComplaint, name='complaint'),
    path('warranty/', views.registerwarranty, name='warranty'),
    path('contact/',views.contact,name='contact'),
    path('gallery/',views.gallery,name='gallery'),
    path('testimonials/',views.testimonials,name='testimonials'),
    path('blogs/',views.blogs,name='blogs'),
    path('review/',views.review,name='review'),
]