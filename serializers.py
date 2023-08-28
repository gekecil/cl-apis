from rest_framework.serializers import HyperlinkedModelSerializer
from django.contrib.auth.models import User
from loan_users.models import User as LoanUser
from loan_users.models import Position, Segmentation, UserPosition, UserSegmentation


class UserSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'groups']

class LoanUserPositionSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Position
        fields = ['name']

class LoanUserSegmentationSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Segmentation
        fields = ['name']

class LoanUserUserPositionSerializer(HyperlinkedModelSerializer):
    position = LoanUserPositionSerializer()

    class Meta:
        model = UserPosition
        fields = ['id', 'position']

class LoanUserUserSegmentationSerializer(HyperlinkedModelSerializer):
    segmentation = LoanUserSegmentationSerializer()

    class Meta:
        model = UserSegmentation
        fields = ['id', 'segmentation']

class LoanUserSerializer(HyperlinkedModelSerializer):
    positions = LoanUserUserPositionSerializer(many=True)
    segmentations = LoanUserUserSegmentationSerializer(many=True)

    class Meta:
        model = LoanUser
        fields = ['id', 'email', 'positions', 'segmentations']
