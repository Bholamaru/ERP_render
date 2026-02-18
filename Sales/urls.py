from rest_framework.routers import DefaultRouter
from .views import OnwardChallanViewSet
from django.urls import path
from .views import generate_unique_challan_number,generate_unique_rework_number
from .views import deletechallan 
from .views import transportdetailsview
from .views import deletetransportdetails
from .views import edittransportdetails
from .views import vehicaldetailsview 
from .views import deletevehicaldetails 
from .views import editvehicaldetails
from .views import purchaseview
from .views import inwardchallanview,InwardChallanRMView
from .views import outwardchallanview
from .views import supplierview 
from .views import ItemFullReport
from .import views 
from .views import *


router = DefaultRouter()
router.register(r'onwardchallan', OnwardChallanViewSet)
router.register(r'transportdetails', transportdetailsview)
router.register(r'vehicaldetails', vehicaldetailsview)
router.register(r'outwardchallan',outwardchallanview)
router.register(r'onward-challans', OnwardChallanViewSet, basename='onward-challan')
router.register(r'invoice', InvoiceViewSet, basename='invoice')
router.register(r'newsalesorder' ,NewsalesOrederViewSet, basename='NewSalesOreder')
router.register(r'debitnote',DebitNoteViewSet,basename='Debit-note')
router.register(r'Gstsalesretun', NewgstsalesreturnViewSet, basename='New-Gst-Sales-Return')


urlpatterns=router.urls+[
   path("generate-challan-no/", generate_unique_challan_number.as_view(), name='generate-challan-no'),
   path("deletechallan/<int:id>/",deletechallan.as_view(), name="deletechallan"),
   path("deletetransportdetails/<str:name>/",deletetransportdetails.as_view() , name="deletetransportdetails"),
   path("edittransportdetails/<str:name>/",edittransportdetails.as_view(), name='edittransportdetails'),
   path('deletevehicaldetails/<str:name>',deletevehicaldetails.as_view(),name='deletevehicaldetails'),
   path('editvehicaldetails/<str:vehical_no>', editvehicaldetails.as_view(), name='editvehicaldetails'),
   path('purchaseview/',purchaseview.as_view(),name='purchaseview'),
   path('inwardchallanview/',inwardchallanview.as_view(),name='inwardchallanview'),
#    /sales/inwardchallanview/?supplier=SUPPLIER_NAME
#    path('inward/', views.inward, name='inward'),
    path('supplierview/',supplierview.as_view(),name='onwardchallandetails-by-supplier'),
    path('onwardchallan/pdf/<int:pk>/', views.generate_onwardchallan_pdf,name='pdf'),

    path('inwardchallanrmview/',InwardChallanRMView.as_view(), name="inwardcahllan-rm-views"),
    path("genrate-rework-no",generate_unique_rework_number.as_view(),name='Genrate-Rework-number'),

    path('heatno/fg/',ItemFullReport.as_view() ,name="sales-fg-heat-no-stockwise" ),
    path('items/customers-list/', CustomerItemListView.as_view(),name="Custerm-view-for-newsales-order"),

    path('items-list/', ItemTableListView.as_view(), name='item-table-list'),

    path('create/invoice_no',generate_invoice_number.as_view(), name='create-invoice-no-for-gst-invoice'),
    
    path('wip/stock/get/',LastOperationProdQtyAPI.as_view(),name='wip-stcok-last-opno-stcok-get'),
    path('debit/no', GenerateDebitNoteNumber.as_view(), name='genrate-debit-note-no'),
    path("purchase-po/by-supplier/", PurchasePOBySupplierAPIView.as_view(), name='debit-note-purchase-grn-data'),

    path('sales/return-no/', GenerateSalesReturnNumber.as_view(), name='Gst-sales-return-no-genrate'),

    path('debit-note/<int:pk>/', DebitNotePDFAPIView.as_view(), name='purchase-debit-note-pdf-genrater'),

    path("customer/po/", NewSalesOrderListAPIView.as_view(), name="customer-po-for-gstinvoice"),

    path("salesreturn/gate-entry", SalesReturnListAPIView.as_view(), name="sales-return-list"),

    path("generate-so-no/", GenerateSalesOrderNumber.as_view(), name="generate-so-no-for-newsalesoreder"),

    path("finish-op-heat-wise/",FinishOpHeatWiseProd.as_view(),name="finish-op-heat-wise"),

]
