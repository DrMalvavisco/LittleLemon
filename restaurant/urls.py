from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('booking', views.BookingView.as_view()),
    path('booking/<int:pk>', views.SingleBookingView.as_view()),
    path('menu', views.MenuView.as_view()),
    path('menu/<int:pk>', views.SingleMenuView.as_view()),
    # path('about/', views.about, name='about'),
    # path('book/', views.book, name='book'),
    # path('menu/', views.menu, name='menu'),
    # path('menu_item/<int:pk>/', views.display_menu_item, name='menu_item'),
]