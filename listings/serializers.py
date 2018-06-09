from rest_framework import serializers
from rest_framework_mongoengine import serializers as mongoserializers
from listings.models import AdvListing


class AdvListingSerializer(mongoserializers.DocumentSerializer):
    # id = serializers.CharField(read_only=False)

    class Meta:
        model = AdvListing
        fields = '__all__'
