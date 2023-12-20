from django.shortcuts import render
from django.db import transaction

from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import HomefeedElement
from .serializers import HomefeedElementSerializer
from rest_framework.decorators import action

class HomefeedElementViewSet(viewsets.ModelViewSet):
    queryset = HomefeedElement.objects.all().order_by('order')
    serializer_class = HomefeedElementSerializer
    lookup_field = 'uuid'

    @action(detail=False, methods=['patch'], url_path='update-order')
    def update_order(self, request, *args, **kwargs):
        with transaction.atomic():
            data = request.data  # This should be a list of objects with 'uuid' and 'order'
            for item in data:
                element = HomefeedElement.objects.get(uuid=item['uuid'])
                element.order = item['order']
                element.save(update_fields=['order'])
        
        return Response(request.data)
