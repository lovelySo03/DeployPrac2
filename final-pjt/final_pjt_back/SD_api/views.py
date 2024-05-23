from django.shortcuts import render
import requests
from django.http import JsonResponse,HttpResponse, HttpResponseRedirect
# from django.urls import reverse
from .models import SavingProduct,DepositProduct,DepositOption,SavingOption
# from django.core.mail import send_mail
def fetch_saving_products(request):
    url = 'https://finlife.fss.or.kr/finlifeapi/savingProductsSearch.json'
    params = {
        'auth': '60d4f09dba9c232253ef3253c212b8ec',
        'topFinGrpNo': '020000',
        'pageNo': 1
    }
    
    response = requests.get(url, params=params)
    data = response.json()

    # if data['result']['err_cd'] != '0000':
    #     return JsonResponse({'error': 'Failed to fetch data from API'})

    products = data['result']['baseList']
    options = data['result']['optionList']
    for product in products:
        fin_prdt_cd = product['fin_prdt_cd']
        # 이미 존재하는지 확인
        if not SavingProduct.objects.filter(fin_prdt_cd=fin_prdt_cd).exists():
            kor_co_nm = product['kor_co_nm']
            fin_prdt_nm = product['fin_prdt_nm']
            join_way = product.get('join_way', '')  # 가입 방법
            mtrt_int = product.get('mtrt_int', '')  # 만기 후 이자 지급 방식
            spcl_cnd = product.get('spcl_cnd', '')  # 특별 조건
            join_deny_code = product.get('join_deny', '')  # 가입 거부 여부 코드

            # 가입 거부 여부 처리
            if join_deny_code == '3':
                join_deny = True  # 일부 제한으로 설정
            else:
                join_deny = False  # 나머지 경우는 가입 거부가 없음

            join_member = product.get('join_member', '')  # 가입 대상
            etc_note = product.get('etc_note', '')  # 기타 참고 사항
            max_limit = product.get('max_limit')  # 최대 한도
            dcls_strt_day = product.get('dcls_strt_day')  # 공시 시작 일자
            dcls_end_day = product.get('dcls_end_day')  # 공시 종료 일자
            fin_co_subm_day = product.get('fin_co_subm_day')  # 금융회사 제출 일자
            
            saving_product = SavingProduct.objects.create(
                fin_prdt_cd=fin_prdt_cd,
                kor_co_nm=kor_co_nm,
                fin_prdt_nm=fin_prdt_nm,
                join_way=join_way,
                mtrt_int=mtrt_int,
                spcl_cnd=spcl_cnd,
                join_deny=join_deny,
                join_member=join_member,
                etc_note=etc_note,
                max_limit=max_limit,
                dcls_strt_day=dcls_strt_day,
                dcls_end_day=dcls_end_day,
                fin_co_subm_day=fin_co_subm_day
            )
            for option in options:
                if option['fin_prdt_cd'] == fin_prdt_cd:
                    SavingOption.objects.create(
                        saving=saving_product,
                        intr_rate_type_nm=option['intr_rate_type_nm'],
                        rsrv_type_nm=option['rsrv_type_nm'],
                        save_trm=option['save_trm'],
                        intr_rate=option['intr_rate'],
                        intr_rate2=option['intr_rate2']
                    )
    return JsonResponse({'message': 'Data fetched and saved successfully'})



def fetch_deposit_products(request):
    url = 'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json'
    params = {
        'auth': '60d4f09dba9c232253ef3253c212b8ec',
        'topFinGrpNo': '020000',
        'pageNo': 1
    }
    
    response = requests.get(url, params=params)
    data = response.json()

    if data['result']['err_cd'] != '000':
        return JsonResponse({'error': 'Failed to fetch data from API'})

    products = data['result']['baseList']
    options = data['result']['optionList']
    for product in products:
        fin_prdt_cd = product['fin_prdt_cd']
        deposit_product = DepositProduct.objects.create(
            dcls_month=product['dcls_month'],
            fin_co_no=product['fin_co_no'],
            fin_prdt_cd=product['fin_prdt_cd'],
            kor_co_nm=product['kor_co_nm'],
            fin_prdt_nm=product['fin_prdt_nm'],
            join_way=product['join_way'],
            mtrt_int=product['mtrt_int'],
            spcl_cnd=product['spcl_cnd'],
            join_deny=product['join_deny'],
            join_member=product['join_member'],
            etc_note=product['etc_note'],
            max_limit=product['max_limit'],
            dcls_strt_day=product['dcls_strt_day'],
            dcls_end_day=product['dcls_end_day'],
            fin_co_subm_day=product['fin_co_subm_day']
        )
        for option in options:
            if option['fin_prdt_cd'] == fin_prdt_cd:
                DepositOption.objects.create(
                    deposit=deposit_product,
                    intr_rate_type_nm=option['intr_rate_type_nm'],
                    save_trm=option['save_trm'],
                    intr_rate=option['intr_rate'],
                    intr_rate2=option['intr_rate2']
                )
    return JsonResponse({'message': 'Data fetched and saved successfully'})



def fetch_products_from_database(request, selected_bank):
    if request.method == 'GET':
        if SavingProduct.objects.filter(kor_co_nm=selected_bank).exists():
            saving_products = list(SavingProduct.objects.filter(kor_co_nm=selected_bank).values())
            for product in saving_products:
                product['options'] = list(SavingOption.objects.filter(saving_id=product['id']).values())
        if DepositProduct.objects.filter(kor_co_nm=selected_bank).exists():
            deposit_products = list(DepositProduct.objects.filter(kor_co_nm=selected_bank).values())
            for product in deposit_products:
                product['options'] = list(DepositOption.objects.filter(deposit_id=product['id']).values())
        return JsonResponse({'saving_products': saving_products, 'deposit_products': deposit_products})
    else:
        return JsonResponse({'error': 'Only GET requests are allowed for this endpoint.'}, status=405)
def fetch_all_products_from_database(request):
    if request.method == 'GET':
        saving_products = list(SavingProduct.objects.all().values())
        deposit_products = list(DepositProduct.objects.all().values())

        for product in saving_products:
            product['options'] = list(SavingOption.objects.filter(saving_id=product['id']).values())
        
        for product in deposit_products:
            product['options'] = list(DepositOption.objects.filter(deposit_id=product['id']).values())

        return JsonResponse({'saving_products': saving_products, 'deposit_products': deposit_products})
    else:
        return JsonResponse({'error': 'Only GET requests are allowed for this endpoint.'}, status=405)

def fetch_product_detail_from_database(request, product_id):
    if request.method == 'GET':
        if SavingProduct.objects.filter(id=product_id).exists():
            product = list(SavingProduct.objects.filter(id=product_id).values())
            product_options = list(SavingOption.objects.filter(saving_id=product_id).values())
        elif DepositProduct.objects.filter(id=product_id).exists():
            product = list(DepositProduct.objects.filter(id=product_id).values())
            product_options = list(DepositOption.objects.filter(deposit_id=product_id).values())
        else:
            return JsonResponse({'error': 'Product not found.'}, status=404)

        return JsonResponse({'product': product})
    else:
        return JsonResponse({'error': 'Only GET requests are allowed for this endpoint.'}, status=405)
# 환율 api 로드
from datetime import datetime
def Fx_Now(request):
    authkey = 'JJSEhowr02Bl1wMo12VDe4m9otJyVyMd'
    searchdate =datetime.now().date().strftime('%Y%m%d')
    data = 'AP01'
    url = f'https://www.koreaexim.go.kr/site/program/financial/exchangeJSON?authkey={authkey}&searchdate={searchdate}&data={data}'
    response = requests.get(url)
    r_data = response.json()
    print(r_data)
    return JsonResponse(r_data, safe=False)
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
# from accounts.models import User


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def subscribe_to_saving_product(request, product_id):
    saving_product = get_object_or_404(SavingProduct, id=product_id)
    user=request.user
    if saving_product in request.user.subscribed_saving.all():
        request.user.subscribed_saving.remove(saving_product)
        message = "적금 상품 가입이 취소되었습니다."
    else:
        request.user.subscribed_saving.add(saving_product)
        message = "적금 상품에 성공적으로 가입되었습니다."
        
    parsing(user)
    return Response({"message": message}, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def subscribe_to_deposit_product(request, product_id):
    deposit_product = get_object_or_404(DepositProduct, id=product_id)
    user=request.user
    if deposit_product in request.user.subscribed_deposit.all():
        request.user.subscribed_deposit.remove(deposit_product)
        message = "예금 상품 가입이 취소되었습니다."
    else:
        request.user.subscribed_deposit.add(deposit_product)
        message = "예금 상품에 성공적으로 가입되었습니다."
    parsing(user)
    return Response({"message": message}, status=status.HTTP_200_OK)



from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import SavingProduct, DepositProduct
from accounts.models import User

# parsing 함수 정의 (수정된 버전)
def parsing(user):
    # related_name을 사용해 해당 User와 연관된 SavingProduct들을 조회
    saving_queryset = user.subscribed_saving.all()  # 'subscribed_saving'은 related_name 가정
    deposit_queryset = user.subscribed_deposit.all()  # 'subscribed_deposit'은 related_name 가정
    
    financial_products = []
    
    # SavingProduct의 fin_prdt_cd 값 추가
    for saving in saving_queryset:
        financial_products.append(saving.fin_prdt_cd)
    
    # DepositProduct의 fin_prdt_cd 값 추가
    for deposit in deposit_queryset:
        financial_products.append(deposit.fin_prdt_cd)
    
    # 배열을 텍스트로 변환하여 User 모델의 텍스트 필드에 저장
    user.financial_products = ', '.join(financial_products)  # 상품명 목록을 쉼표로 구분된 문자열로 변환
    user.save()  # 변경사항 저장