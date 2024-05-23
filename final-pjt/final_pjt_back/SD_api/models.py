from django.db import models
from django.conf import settings

class SavingProduct(models.Model):
    fin_prdt_cd = models.CharField(max_length=100, unique=True)
    kor_co_nm = models.CharField(max_length=100)
    fin_prdt_nm = models.CharField(max_length=100)
    join_way = models.TextField()  # 가입 방법
    mtrt_int = models.TextField()  # 만기 후 이자 지급 방식
    spcl_cnd = models.TextField()  # 특별 조건
    join_deny = models.BooleanField(default=False)  # 가입 거부 여부
    join_member = models.TextField()  # 가입 대상
    etc_note = models.TextField()  # 기타 참고 사항
    max_limit = models.IntegerField(null=True, blank=True)  # 최대 한도
    dcls_strt_day = models.CharField(max_length=8)  # 공시 시작 일자
    dcls_end_day = models.CharField(max_length=8, null=True, blank=True)  # 공시 종료 일자
    fin_co_subm_day = models.CharField(max_length=12)  # 금융회사 제출 일자
    subscribe_user= models.ManyToManyField(settings.AUTH_USER_MODEL , related_name='subscribed_saving')

class DepositProduct(models.Model):
    dcls_month = models.CharField(max_length=6)
    fin_co_no = models.CharField(max_length=10)
    fin_prdt_cd = models.CharField(max_length=20, unique=True)
    kor_co_nm = models.CharField(max_length=100)
    fin_prdt_nm = models.CharField(max_length=100)
    join_way = models.TextField()
    mtrt_int = models.TextField()
    spcl_cnd = models.CharField(max_length=100)
    join_deny = models.CharField(max_length=10)
    join_member = models.CharField(max_length=100)
    etc_note = models.TextField()
    max_limit = models.IntegerField(null=True, blank=True)
    dcls_strt_day = models.CharField(max_length=8)
    dcls_end_day = models.CharField(max_length=8, null=True, blank=True)
    fin_co_subm_day = models.CharField(max_length=12)
    subscribe_user= models.ManyToManyField(settings.AUTH_USER_MODEL , related_name='subscribed_deposit')
class DepositOption(models.Model):
    deposit = models.ForeignKey(DepositProduct, on_delete=models.CASCADE)
    intr_rate_type_nm = models.CharField(max_length=2)
    save_trm = models.CharField(max_length=3)
    intr_rate = models.FloatField(null=True)
    intr_rate2 = models.FloatField(null=True)

class SavingOption(models.Model):
    saving=models.ForeignKey(SavingProduct, on_delete=models.CASCADE)
    intr_rate_type_nm = models.CharField(max_length=2)
    rsrv_type_nm = models.CharField(max_length=10)
    save_trm = models.CharField(max_length=3)
    intr_rate = models.FloatField(null=True)
    intr_rate2 = models.FloatField(null=True)