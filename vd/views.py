from django.shortcuts import render

from rest_framework import viewsets

from .models import Veedeo
from .serializers import VdSerializer


class VdViewSet(viewsets.ModelViewSet):
    queryset = Veedeo.objects.all()
    serializer_class = VdSerializer



def home(request):
    return render(request, 'index.html')