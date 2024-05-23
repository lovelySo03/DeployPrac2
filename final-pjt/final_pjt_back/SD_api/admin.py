from django.contrib import admin
from .models import SavingProduct, DepositProduct

@admin.register(SavingProduct)
class SavingProductAdmin(admin.ModelAdmin):
    list_display = ['kor_co_nm', 'fin_prdt_nm', 'join_way', 'mtrt_int', 'spcl_cnd', 'join_deny', 'max_limit', 'dcls_strt_day', 'dcls_end_day', 'fin_co_subm_day']
    search_fields = ['kor_co_nm', 'fin_prdt_nm']
    list_filter = ['kor_co_nm', 'join_deny']
    # 기타 필요한 설정을 추가할 수 있습니다.

@admin.register(DepositProduct)
class DepositProductAdmin(admin.ModelAdmin):
    list_display = ['kor_co_nm', 'fin_prdt_nm', 'join_way', 'mtrt_int', 'spcl_cnd', 'join_deny', 'max_limit', 'dcls_strt_day', 'dcls_end_day', 'fin_co_subm_day']
    search_fields = ['kor_co_nm', 'fin_prdt_nm']
    list_filter = ['kor_co_nm', 'join_deny']
    # 기타 필요한 설정을 추가할 수 있습니다.
