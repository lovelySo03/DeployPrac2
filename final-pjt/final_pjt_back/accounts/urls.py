from django.urls import path
from . import views

urlpatterns = [
    path('delete_user/', views.delete_user, name='delete-user'),
    # path('update_user/', views.update_user, name='update-user'),
     path('profile/', views.user_profile, name='user_profile'),
     path('info/', views.user_info, name='user_info') # 가입상품 상세정보도 있는거
]
