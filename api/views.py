from django.shortcuts import render
from rest_framework import generics, status, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend, OrderingFilter
from .serializers import *
from main.models import *

# Create your views here.
class CreateRequestersRequestView(APIView):
    serializer_class = CreateRequestersRequestSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            from_location = serializer.data.get("from_location")
            to_location = serializer.data.get("to_location")
            date_time = serializer.data.get("date_time")
            flex_timings = serializer.data.get("flex_timings")
            no_of_assets = serializer.data.get("no_of_assets")
            asset_types = serializer.data.get("asset_types")
            asset_sensitive = serializer.data.get("asset_sensitive")
            whom_to_deliver = serializer.data.get("whom_to_deliver")

            req = RequestersRequest(
                user_id=request.user.id,
                from_location=from_location,
                to_location=to_location,
                date_time=date_time,
                flex_timings=flex_timings,
                no_of_assets=no_of_assets,
                asset_types=asset_types,
                asset_sensitive=asset_sensitive,
                whom_to_deliver=whom_to_deliver,
            )

            req.save()

            return Response(
                CreateRequestersRequestSerializer(req).data,
                status=status.HTTP_201_CREATED,
            )

        return Response(
            {"Bad Request": "Invalid data..."}, status=status.HTTP_400_BAD_REQUEST
        )


class CreateRiderRequestView(APIView):
    serializer_class = CreateRiderRequestSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            from_location = serializer.data.get("from_location")
            to_location = serializer.data.get("to_location")
            date_time = serializer.data.get("date_time")
            flex_timings = serializer.data.get("flex_timings")
            travel_medium = serializer.data.get("travel_medium")
            asset_quantity = serializer.data.get("asset_quantity")

            req = RiderRequest(
                user_id=request.user.id,
                from_location=from_location,
                to_location=to_location,
                date_time=date_time,
                flex_timings=flex_timings,
                travel_medium=travel_medium,
                asset_quantity=asset_quantity,
            )

            req.save()

            return Response(
                CreateRiderRequestSerializer(req).data,
                status=status.HTTP_201_CREATED,
            )

        return Response(
            {"Bad Request": "Invalid data..."}, status=status.HTTP_400_BAD_REQUEST
        )


class GetRequestersRequestView(generics.ListAPIView):
    queryset = RequestersRequest.objects.all()
    serializer_class = GetRequestersRequestSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ["status", "asset_types"]
    ordering_fields = ["date_time"]

    def get(self, request, format=None):
        id = request.user.id
        if id != None:
            req = RequestersRequest.objects.filter(user_id=id)
            if req.exists():
                data = GetRequestersRequestSerializer(req, many=True).data
                return Response(data, status=status.HTTP_200_OK)

            return Response(
                {"Requesters Id Not Found": "Invalid Search Name."},
                status=status.HTTP_404_NOT_FOUND,
            )

        return Response(
            {"Bad Request": "Requesters Id paramater not found in request"},
            status=status.HTTP_400_BAD_REQUEST,
        )


class GetRiderRequestView(APIView):
    serializer_class = GetRiderRequestSerializer
    permission_classes = [permissions.IsAuthenticated]
    look_up_kwarg = "req_no"

    def get(self, request, format=None):
        id = request.user.id
        req_no = request.GET.get(self.look_up_kwarg)
        if id != None and req_no != None:
            req = RequestersRequest.objects.filter(user_id=id, id=req_no)
            if req.exists():
                rider_req = RiderRequest.objects.filter(
                    from_location=req[0].from_location,
                    to_location=req[0].to_location,
                    date_time__date=req[0].date_time.date(),
                )
                data = GetRiderRequestSerializer(rider_req, many=True).data
                return Response(data, status=status.HTTP_200_OK)

            return Response(
                {"Requesters Id Not Found": "Invalid Search Name."},
                status=status.HTTP_404_NOT_FOUND,
            )

        return Response(
            {"Bad Request": "Requesters Id paramater not found in request"},
            status=status.HTTP_400_BAD_REQUEST,
        )


class UpdateRiderRequestView(APIView):
    serializer_class = UpdateRiderRequestSerializer
    permission_classes = [permissions.IsAuthenticated]
    look_up_kwarg = "req_no"

    def patch(self, request, format=None):
        req_no = request.GET.get(self.look_up_kwarg)
        if req_no != None:
            queryset = RiderRequest.objects.filter(id=req_no)
            rider_req = queryset[0]
            rider_req.applied = True
            rider_req.save(update_fields=["applied"])
            return Response(
                UpdateRiderRequestSerializer(rider_req).data, status=status.HTTP_200_OK
            )
        return Response(
            {"Bad Request": "Invalid Data..."}, status=status.HTTP_400_BAD_REQUEST
        )
