from django.views.generic import TemplateView
from django.views.decorators.cache import never_cache
from rest_framework import viewsets

from .models import Message, MessageSerializer


class GetTop20(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
