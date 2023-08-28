from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from loan_users.models import User as LoanUser
from loan_users.models import UserPosition, UserSegmentation
from .serializers import UserSerializer, LoanUserSerializer


class UserViewSet(ReadOnlyModelViewSet):
    queryset = User.objects
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return super().get_queryset().filter(username=self.request.user.username)

class LoanUserViewSet(ReadOnlyModelViewSet):
    queryset = LoanUser.objects.all().order_by('-pub_date')
    serializer_class = LoanUserSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = super().get_queryset()

        for loan_user in queryset:
            loan_user.positions = UserPosition.objects.filter(user=loan_user)
            loan_user.segmentations = UserSegmentation.objects.filter(user=loan_user)

        return queryset

    def retrieve(self, request, pk=None):
        queryset = super().get_queryset()
        loan_user = get_object_or_404(queryset, pk=pk)
        loan_user.positions = UserPosition.objects.all()
        loan_user.segmentations = UserSegmentation.objects.all()

        return Response(LoanUserSerializer(loan_user).data)
