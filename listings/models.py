# from django.db import models
import mongoengine
from mongoengine import Document, EmbeddedDocument, fields
# Create your models here.


class Area(EmbeddedDocument):
    metersSquared = fields.IntField()
    feetSquared = fields.IntField()

    # This Meta avoids creating a new collection
    class Meta:
        abstract = True


class Coordinates(EmbeddedDocument):
    geo_lat = fields.FloatField()
    geo_lng = fields.FloatField()

    class Meta:
        abstract = True


class AdvListing(Document):
    # _id = fields.EmbeddedDocumentField(required=True)
    # id = fields.StringField(required=True, primary_key=True)
    url = fields.StringField(required=True)
    title = fields.StringField(required=True)
    description = fields.StringField()
    image_urls = fields.ListField(fields.StringField(max_length=150))
    hasGreenSpace = fields.BooleanField()
    isRental = fields.BooleanField()
    landArea = fields.EmbeddedDocumentField(Area)
    location = fields.StringField()
    hasEntertaimentRoom = fields.BooleanField()
    ConvinienceStores = fields.StringField()
    hasDemoApartment = fields.BooleanField()
    isCloseToShoppingCenter = fields.BooleanField()
    hasSauna = fields.BooleanField()
    hasSellingOffice = fields.BooleanField()
    numOfLifts = fields.IntField()
    hasChildrenGames = fields.BooleanField()
    hasMeetingRoom = fields.BooleanField()
    builtArea = fields.EmbeddedDocumentField(Area)
    numBedrooms = fields.IntField()
    listingPrice = fields.StringField()
    isForProfessionalUse = fields.BooleanField()
    parentPage = fields.StringField()
    totalFloors = fields.IntField()
    hasPool = fields.BooleanField()
    apartmentsPerFloor = fields.IntField()
    comercialUse = fields.BooleanField()
    hasGrill = fields.BooleanField()
    totalBuildings = fields.IntField()
    dateAdded = fields.DateTimeField()
    isCloseToHospital = fields.BooleanField()
    listingType = fields.StringField()
    isCloseToSchools = fields.BooleanField()
    hasGym = fields.BooleanField()
    coordinates = fields.EmbeddedDocumentField(Coordinates)
    hasSportArea = fields.BooleanField()
    totalArea = fields.EmbeddedDocumentField(Area)
    hasClosePark = fields.BooleanField()
    isCloseToSea = fields.BooleanField()
    hasComputerRoom = fields.BooleanField()
