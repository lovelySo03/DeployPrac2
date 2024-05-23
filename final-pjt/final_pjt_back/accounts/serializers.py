from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer
from dj_rest_auth.serializers import UserDetailsSerializer
from .models import User
from django.contrib.auth import get_user_model
UserModel = get_user_model()


class CustomRegisterSerializer(RegisterSerializer):
    nickname = serializers.CharField(
        required=False,
        allow_blank=True,
        max_length=100
    )
    age = serializers.IntegerField(required=False, allow_null=True)
    money = serializers.IntegerField(required=False, allow_null=True)
    salary = serializers.IntegerField(required=False, allow_null=True)
    # financial_products = serializers.CharField(required=False, allow_blank=True)

    def get_cleaned_data(self):
        return {
            'username': self.validated_data.get('username', ''),
            'password1': self.validated_data.get('password1', ''),
            'nickname': self.validated_data.get('nickname', ''),
            'age': self.validated_data.get('age', None),
            'money': self.validated_data.get('money', None),
            'salary': self.validated_data.get('salary', None),
            # 'financial_products': self.validated_data.get('financial_products', '')
        }


from rest_framework import serializers
from SD_api.models import SavingProduct, DepositProduct
# from SD_api.serializers import SavingProductSerializer, DepositProductSerializer

class CustomUserDetailsSerializer(UserDetailsSerializer):
    # saving_products = serializers.SerializerMethodField()
    # deposit_products = serializers.SerializerMethodField()

    class Meta:
        extra_fields = []
        if hasattr(UserModel, 'USERNAME_FIELD'):
            extra_fields.append(UserModel.USERNAME_FIELD)
        if hasattr(UserModel, 'EMAIL_FIELD'):
            extra_fields.append(UserModel.EMAIL_FIELD)
        if hasattr(UserModel, 'first_name'):
            extra_fields.append('first_name')
        if hasattr(UserModel, 'last_name'):
            extra_fields.append('last_name')
        if hasattr(UserModel, 'nickname'):
            extra_fields.append('nickname')
        if hasattr(UserModel, 'age'):
            extra_fields.append('age')
        if hasattr(UserModel, 'money'):
            extra_fields.append('money')
        if hasattr(UserModel, 'salary'):
            extra_fields.append('salary')
        if hasattr(UserModel, 'financial_products'):
            extra_fields.append('financial_products')
        model = UserModel
        fields = ('pk', *extra_fields)
        read_only_fields = ('username','nickname','email','financial_products')

    def update(self, instance, validated_data):
        instance = super().update(instance, validated_data)
        for attr, value in validated_data.items():
            if attr in self.Meta.extra_fields:
                setattr(instance, attr, value)
        instance.save()
        return instance

    # def get_saving_products(self, obj):
    #     if obj.financial_products:  # financial_products가 None이 아닌지 확인
    #         saving_products_ids = [int(pid) for pid in obj.financial_products.split(',') if pid.startswith('s')]
    #         saving_products = SavingProduct.objects.filter(id__in=saving_products_ids)
    #         return SavingProductSerializer(saving_products, many=True).data
    #     else:
    #         return []  # financial_products가 None일 경우 빈 리스트 반환

    # def get_deposit_products(self, obj):
    #     if obj.financial_products:  # financial_products가 None이 아닌지 확인
    #         deposit_products_ids = [int(pid) for pid in obj.financial_products.split(',') if pid.startswith('d')]
    #         deposit_products = DepositProduct.objects.filter(id__in=deposit_products_ids)
    #         return DepositProductSerializer(deposit_products, many=True).data
    #     else:
    #         return []  # financial_products가 None일 경우 빈 리스트 반환
