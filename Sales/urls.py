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

router = DefaultRouter()
router.register(r'onwardchallan', OnwardChallanViewSet)
router.register(r'transportdetails', transportdetailsview)
router.register(r'vehicaldetails', vehicaldetailsview)
router.register(r'outwardchallan',outwardchallanview)
router.register(r'onward-challans', OnwardChallanViewSet, basename='onward-challan')

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
]
