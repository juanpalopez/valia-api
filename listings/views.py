# from django.shortcuts import render
from rest_framework_mongoengine import viewsets
from listings.models import AdvListing
from listings.serializers import AdvListingSerializer

# Create your views here.


class AdvListingViewSet(viewsets.ModelViewSet):
    '''This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    '''
    lookup_field = 'id'
    serializer_class = AdvListingSerializer
    queryset = AdvListing.objects.all().limit(1)
