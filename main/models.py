from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import datetime

# Create your models here.
class RequestersRequest(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="requestersrequest"
    )
    from_location = models.CharField(max_length=255, blank=False)
    to_location = models.CharField(max_length=255, blank=False)
    date_time = models.DateTimeField(blank=False)
    flex_timings = models.BooleanField(blank=False)
    no_of_assets = models.IntegerField(blank=False)
    asset_type_list = ["LAPTOP", "TRAVEL_BAG", "PACKAGE"]
    asset_type_options = sorted([(item, item) for item in asset_type_list])
    asset_types = models.CharField(
        max_length=20, choices=asset_type_options, blank=False
    )
    asset_sensitive_list = ["HIGHLY_SENSITIVE", "SENSITIVE", "NORMAL"]
    asset_sensitive_options = sorted([(item, item) for item in asset_sensitive_list])
    asset_sensitive = models.CharField(
        max_length=20, choices=asset_sensitive_options, blank=False
    )
    whom_to_deliver = models.CharField(max_length=255, blank=False)
    status = models.CharField(max_length=20, default="Pending")

    @property
    def accepted_person_details(self):
        return self.whom_to_deliver

    def save(self, *args, **kwargs):
        # date = datetime.strptime(
        #     datetime.fromisoformat(self.date_time), "%Y-%m-%d %H:%M:%S"
        # )
        if datetime.fromisoformat(self.date_time) < datetime.now():
            self.status = "Expired"
        super().save(*args, **kwargs)


class RiderRequest(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="riderrequest", null="True"
    )
    from_location = models.CharField(max_length=255, blank=False)
    to_location = models.CharField(max_length=255, blank=False)
    date_time = models.DateTimeField(blank=False)
    flex_timings = models.BooleanField(blank=False)
    travel_medium_list = ["CAR", "BUS", "TRAIN"]
    travel_medium_options = sorted([(item, item) for item in travel_medium_list])
    travel_medium = models.CharField(
        max_length=20, choices=travel_medium_options, blank=False
    )
    asset_quantity = models.IntegerField(blank=False)
    applied = models.BooleanField(default=False)
