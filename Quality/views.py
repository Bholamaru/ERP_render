from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import viewsets
from .models import *
from .serializers import *
# Create your views here.



@api_view(['GET'])
def test_view(request):
    return Response({"message": "Quality is coming"})



from rest_framework.views import APIView
from rest_framework.response import Response
from Purchase.models import PurchasePO
from Purchase.serializers import OOPurchaseSerializer


class PurchasePOforInwardtestlist(APIView):

    def get(self, request):

        supplier = request.GET.get('supplier')
        start_date = request.GET.get('start_date')
        end_date = request.GET.get('end_date')

        queryset = PurchasePO.objects.prefetch_related(
            'Item_Detail_Enter',
            'Gst_Details',
            'Item_Details_Other',
            'Schedule_Line',
            'Ship_To_Add'
        ).all().order_by('-PoDate')

        if supplier:
            queryset = queryset.filter(Supplier__icontains=supplier)

        if start_date and end_date:
            queryset = queryset.filter(PoDate__range=[start_date, end_date])

        serializer =OOPurchaseSerializer(queryset, many=True)

        return Response({
            "count": queryset.count(),
            "results": serializer.data
        })



from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import (
    InwardtestQCinfo,
    InwardtestDimensional,
    Inwardtestvisulainspection,
    InwardtestreworkQty,
    InwardtestrejectQty
)
from .serializers import InwardtestQCinfoSerializer


class InwardtestQCinfoViewSet(viewsets.ModelViewSet):

    queryset = InwardtestQCinfo.objects.all().order_by('-id')
    serializer_class = InwardtestQCinfoSerializer


    # CREATE
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({
            "status": True,
            "message": "QC Info created successfully",
            "data": serializer.data
        }, status=status.HTTP_201_CREATED)


    # LIST
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)

        return Response({
            "status": True,
            "data": serializer.data
        })


    # RETRIEVE SINGLE
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)

        return Response({
            "status": True,
            "data": serializer.data
        })


    # UPDATE
    def update(self, request, *args, **kwargs):
        instance = self.get_object()

        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({
            "status": True,
            "message": "QC Info updated successfully",
            "data": serializer.data
        })


    # DELETE
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()

        return Response({
            "status": True,
            "message": "QC Info deleted successfully"
        }, status=status.HTTP_204_NO_CONTENT)
    



class SubconJobworkQCInfoListCreateView(APIView):
   
    def get(self, request):
        qc = SubconJobworkQCInfo.objects.all().order_by('-id')
        serializer = SubconJobworkQCInfoSerializer(qc, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SubconJobworkQCInfoSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({
                "message": "QC Created Successfully",
                "data": serializer.data
            }, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class SubconJobworkQCInfoDetailView(APIView):   
    def get(self, request, pk):
        qc = get_object_or_404(SubconJobworkQCInfo, pk=pk)
        serializer = SubconJobworkQCInfoSerializer(qc)
        return Response(serializer.data)

    def put(self, request, pk):
        qc = get_object_or_404(SubconJobworkQCInfo, pk=pk)

        serializer = SubconJobworkQCInfoSerializer(
            qc,
            data=request.data
        )

        if serializer.is_valid():
            serializer.save()
            return Response({
                "message": "QC Updated Successfully",
                "data": serializer.data
            })

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    # PATCH partial update
    def patch(self, request, pk):
        qc = get_object_or_404(SubconJobworkQCInfo, pk=pk)

        serializer = SubconJobworkQCInfoSerializer(
            qc,
            data=request.data,
            partial=True
        )

        if serializer.is_valid():
            serializer.save()
            return Response({
                "message": "QC Updated Successfully",
                "data": serializer.data
            })

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    # DELETE record
    def delete(self, request, pk):
        qc = get_object_or_404(SubconJobworkQCInfo, pk=pk)
        qc.delete()

        return Response({
            "message": "QC Deleted Successfully"
        }, status=status.HTTP_204_NO_CONTENT)
    





class SalesReturnQcInfoAPI(APIView):

    def get(self, request):

        data = SalesReturnQcInfo.objects.all().order_by('-id')

        serializer = SalesReturnQcInfoSerializer(data, many=True)

        return Response(serializer.data)


    def post(self, request):

        serializer = SalesReturnQcInfoSerializer(data=request.data)

        if serializer.is_valid():

            serializer.save()

            return Response(
                {"message": "Sales Return QC Created Successfully"},
                status=status.HTTP_201_CREATED
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)