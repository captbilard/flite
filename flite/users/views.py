from rest_framework import viewsets, mixins, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .models import User, NewUserPhoneVerification
from .permissions import IsUserOrReadOnly
from .serializers import CreateUserSerializer, UserSerializer, SendNewPhonenumberSerializer
from rest_framework.views import APIView
from rest_framework.decorators import action
from django.core.exceptions import ObjectDoesNotExist
from . import utils

class UserViewSet(mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  viewsets.GenericViewSet):
    """
    Updates and retrieves user accounts
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsUserOrReadOnly,)

    @action(methods=['post'], detail=True, permission_classes=[IsUserOrReadOnly],
            url_path='deposits', url_name='deposits')
    def deposit(self, request, pk=None):
        try:
            User.objects.get(pk=pk)
        except ObjectDoesNotExist:
            return Response({"message":"User not found"}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({"message":"Your account has been credited"}, status=status.HTTP_200_OK)
    
    @action(methods=['post'], detail=True, permission_classes=[IsUserOrReadOnly],
            url_path='withdrawals', url_name='withdrawals')
    def withdrawal(self, request, pk=None):
        try:
            User.objects.get(pk=pk)
        except ObjectDoesNotExist:
            return Response({"message":"User not found"}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({"message":"Withdrawal successfull & account balance updated"}, status=status.HTTP_200_OK)




class UserCreateViewSet(mixins.CreateModelMixin,
                        viewsets.GenericViewSet):
    """
    Creates user accounts
    """
    queryset = User.objects.all()
    serializer_class = CreateUserSerializer
    permission_classes = (AllowAny,)


class SendNewPhonenumberVerifyViewSet(mixins.CreateModelMixin,mixins.UpdateModelMixin, viewsets.GenericViewSet):
    """
    Sending of verification code
    """
    queryset = NewUserPhoneVerification.objects.all()
    serializer_class = SendNewPhonenumberSerializer
    permission_classes = (AllowAny,)


    def update(self, request, pk=None,**kwargs):
        verification_object = self.get_object()
        code = request.data.get("code")

        if code is None:
            return Response({"message":"Request not successful"}, 400)    

        if verification_object.verification_code != code:
            return Response({"message":"Verification code is incorrect"}, 400)    

        code_status, msg = utils.validate_mobile_signup_sms(verification_object.phone_number, code)
        
        content = {
                'verification_code_status': str(code_status),
                'message': msg,
        }
        return Response(content, 200)    