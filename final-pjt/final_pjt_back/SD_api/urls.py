from django.urls import path
from . import views

urlpatterns = [
    path('fetch/', views.fetch_saving_products, name='fetch_saving_products'),
    path('deposits/', views.fetch_deposit_products, name='fetch_deposit_products'),
    path('products/bank/<str:selected_bank>/',views.fetch_products_from_database),
    path('products/<int:product_id>/',views.fetch_product_detail_from_database),
    path('products/all/',views.fetch_all_products_from_database),
    # GUN
    path('subscribe/saving/<int:product_id>/', views.subscribe_to_saving_product, name='subscribe_to_saving'),
    path('subscribe/deposit/<int:product_id>/', views.subscribe_to_deposit_product, name='subscribe_to_deposit'),
    path('parsing/<int:user_id>/',views.parsing,name="parsing"),
    path('Fx/',views.Fx_Now),
    # path('subscribe/saving/<str:fin_prdt_cd>/', views.subscribe_to_saving_product, name='subscribe_to_saving'),
    # path('subscribe/deposit/<str:fin_prdt_cd>/', views.subscribe_to_deposit_product, name='subscribe_to_deposit'),
    # path('send/',views.sendEamil),
]