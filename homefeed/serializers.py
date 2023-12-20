from rest_framework import serializers
from .models import HomefeedElement

class HomefeedElementSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomefeedElement
        exclude = ('id', )

