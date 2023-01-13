from rest_framework import serializers
from main.models import *


class RequestersRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequestersRequest
        fields = "__all__"


class CreateRequestersRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequestersRequest
        fields = (
            "from_location",
            "to_location",
            "date_time",
            "flex_timings",
            "no_of_assets",
            "asset_types",
            "asset_sensitive",
            "whom_to_deliver",
        )


class RiderRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = RiderRequest
        fields = "__all__"


class CreateRiderRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = RiderRequest
        fields = (
            "from_location",
            "to_location",
            "date_time",
            "flex_timings",
            "travel_medium",
            "asset_quantity",
        )


class GetRequestersRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequestersRequest
        fields = (
            "from_location",
            "to_location",
            "date_time",
            "no_of_assets",
            "asset_types",
            "asset_sensitive",
            "whom_to_deliver",
            "accepted_person_details",
            "status",
        )


class GetRiderRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = RiderRequest
        fields = "__all__"


class UpdateRiderRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = RiderRequest
        fields = "__all__"
