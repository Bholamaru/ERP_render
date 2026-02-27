from django.urls import path,include
from . import views 
from .views import *
from rest_framework.routers import DefaultRouter
from Store.views import InwardChallanListCreate
from Production.views import ProductionEntryViewSet

router = DefaultRouter()
router.register(r'qcinfo', InwardtestQCinfoViewSet, basename='qcinfo')

urlpatterns = [
    # example
    path('test/', views.test_view, name='test'),
    path('api/', include(router.urls)),
    path('purchase-po-search/', PurchasePOforInwardtestlist.as_view(),name='Inward-test-certificate-list'),
    path('inward-qc-list/',InwardChallanListCreate.as_view(),name='Inward 57F4 QC List'),
    # path('inprocess/inspection',ProductionEntryViewSet.as_view() , name='Inprocess-Inspections'),
    path('subcon-jobwork-qc/', SubconJobworkQCInfoListCreateView.as_view(),name='subcon-jobwork-Qc'),
    path('subcon-jobwork-qc/<int:pk>/', SubconJobworkQCInfoDetailView.as_view(), name='subcon-jobwork-QC-delete'),    
    path('sales-return-qc/',SalesReturnQcInfoAPI.as_view(), name='sales-return-qc-post-api'),
    path('sales-qc-number/', GenerateUniqueQcNumber.as_view(), name='generate_qc_no-for-sales-return-qc'),    
    path('subcon-qc-number/',GenrateSubconQcNo.as_view(), name='subcon-jobwork-qc-no-genrate'),
    path('inwardtest-qc-number/',GenrateInwardTestqcno.as_view(),name='InwardTest-genrate-qc-no'),
]
