from django.shortcuts import render, get_object_or_404
from .serializers import CustomUserDetailsSerializer
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import CustomUserDetailsSerializer
from django.contrib.auth import get_user_model
# Serializer를 적절하게 생성 및 임포트해야 합니다.
from SD_api.serializers import SavingProductSerializer, DepositProductSerializer

User = get_user_model()
# 회원탈퇴
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_user(request):
    user = request.user
    user.delete()
    return Response({"detail": "User account has been deleted."}, status=status.HTTP_204_NO_CONTENT)






@api_view(['GET', 'PUT'])
@permission_classes([IsAuthenticated])
def user_profile(request):
    user = get_object_or_404(User, pk=request.user.pk)
    
    if request.method == 'PUT':
        # 사용자 정보 업데이트
        serializer = CustomUserDetailsSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'GET':
        # 사용자 프로필 조회
        serializer = CustomUserDetailsSerializer(user)
        user_subscribed_savings = user.subscribed_saving.all()
        user_subscribed_deposits = user.subscribed_deposit.all()

        # Serializer를 사용하여 JSON으로 변환
        savings_serializer = SavingProductSerializer(user_subscribed_savings, many=True)
        deposits_serializer = DepositProductSerializer(user_subscribed_deposits, many=True)

        # 최종 데이터를 Response로 반환
        return Response({
            'user_data': serializer.data,
            'subscribed_savings': savings_serializer.data,
            'subscribed_deposits': deposits_serializer.data
        })


# 가입상품 상세정보까지 있는 거


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_info(request):
    user = get_object_or_404(User, pk=request.user.pk)
    user_subscribed_savings = user.subscribed_saving.all()
    user_subscribed_deposits = user.subscribed_deposit.all()

    # Serializer를 사용하여 JSON으로 변환
    savings_serializer = SavingProductSerializer(
        user_subscribed_savings, many=True)
    deposits_serializer = DepositProductSerializer(
        user_subscribed_deposits, many=True)

    # 최종 데이터를 Response로 반환
    return Response({
        'user': user.username,  # 혹은 필요에 따라 다른 사용자 정보를 포함할 수 있습니다.
        'subscribed_savings': savings_serializer.data,
        'subscribed_deposits': deposits_serializer.data
    })
