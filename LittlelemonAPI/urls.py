from django.urls import path, include
from . import views
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    # path('menu-items', views.MenuItemsView.as_view()),
    path('menu-items/', views.menu_items),
    path('menu-item/<int:pk>/', views.single_menu_item),
    path('api-token-auth/', obtain_auth_token),
    path('users/', include('djoser.urls')),
    path('users/', include('djoser.urls.authtoken')), 
                                  
]