from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register(r'general-details', GeneralDetailsViewSet)
router.register(r'New-MRN-Entry', NewMrnView)
router.register(r'PurchaseGRN', GrnGenralDetailViewSet) 
router.register(r'New-Material-Issue', MaterialChallanView)


urlpatterns = [
    path('api/', include(router.urls)),
    path('InwardChallan/', InwardChallanListCreate.as_view(), name='InwardChallan-retrieve-list-create'),
    path('InwardChallan/<int:pk>/', InwardChallanRetrieveUpdateDestroy.as_view(), name='InwardChallan-retrieve-update-destroy'),
    path('Job_Work/', Job_WorkListCreate.as_view(), name='Job_Work-retrieve-list-create'),
    path('Job_Work/<int:pk>/', Job_WorkRetrieveUpdateDestroy.as_view(), name='Job_Work-retrieve-update-destroy'),
    path('VendorScrap/', VendorScrap_ListCreate.as_view(), name='VendorScrap-retrieve-list-create'),
    path('VendorScrap/<int:pk>/', VendorScrap_RetrieveUpdateDestroy.as_view(), name='VendorScrap-retrieve-update-destroy'),
    path('MaterialIssue/', MaterialIssue_ListCreate.as_view(), name='MaterialIssue-retrieve-list-create'),
    path('MaterialIssue/<int:pk>/', MaterialIssue_RetrieveUpdateDestroy.as_view(), name='MaterialIssue-retrieve-update-destroy'),
    path('Material_Issue_General/', Material_Issue_General_ListCreate.as_view(), name='Material_Issue_General-retrieve-list-create'),
    path('Material_Issue_General/<int:pk>/', Material_Issue_General_RetrieveUpdateDestroy.as_view(), name='Material_Issue_General-retrieve-update-destroy'),
    path('DeliveryChallan/', DeliveryChallan_ListCreate.as_view(), name='DeliveryChallan-retrieve-list-create'),
    path('DeliveryChallan/<int:pk>/', DeliveryChallan_RetrieveUpdateDestroy.as_view(), name='DeliveryChallan-retrieve-update-destroy'),
    path('SecondDeliveryChallann/', SecondDeliveryChallann_ListCreate.as_view(), name='SecondDeliveryChallann-retrieve-list-create'),
    path('SecondDeliveryChallann/<int:pk>/', SecondDeliveryChallan_RetrieveUpdateDestroy.as_view(), name='SecondDeliveryChallann-retrieve-update-destroy'),
    path('DC_GRN/', DC_GRN_ListCreate.as_view(), name='DeliveryChallan-retrieve-list-create'),
    path('DC_GRN/<int:pk>/', DC_GRN_RetrieveUpdateDestroy.as_view(), name='DeliveryChallan-retrieve-update-destroy'),
    path('maingroup/', MainGroupListCreateAPIView.as_view(), name='main-group-list-create'),
    path('maingroup/<int:pk>/', MainGroupList_RetrieveUpdateDestroy.as_view(), name='main-group-list-create'),
    path('itemgroup/', ItemGroupListCreateAPIView.as_view(), name='item-group-list-create'),
    path('itemgroup/<int:pk>/', ItemGroup_RetrieveUpdateDestroy.as_view(), name='item-group-list-create'),
    path('items/', ItemListCreateAPIView.as_view(), name='item-list-create'),
    # path('next-part-no/<int:main_group_id>/<int:item_group_id>/', NextPartNoAPIView.as_view(), name='next-part-no'),
    path('itemgroup/next-part-no/', NextPartNoByTypeAPIView.as_view(), name='next-part-no-by-type'),
    path('items/<int:pk>/', ItemDetailAPIView.as_view(), name='item-detail'),
    path('items/next-part-no/', NextPartNoAPIView.as_view(), name='next-part-no'),
    path('api/get-next-ge-no/', GetNextGeneralDetails.as_view(), name='get-next-ge-no'),
    path('api/get-next-mrn-no/', GetNextMrnNo.as_view(), name='get-next-mrn-no'),
    path('NewMRN_Item_Search/', NewMRNItemSearchListView.as_view(), name='New-MRN-Item_Search'),
    path('NewMRN_EmployeeDept_Search/', NewMRNEmployeeDeptListView.as_view(), name='NewMRN-EmployeeDept-Search'),
    path('api/grn-details/', GrnDetailAPIView.as_view(), name='grn-detail-api'),
    path('pdf/<int:id>/', generate_pdf, name='generate_pdf'),
    path('GetNextGrnNo/', GetNextGrnNo.as_view(), name='get-next-GrnNo'),
    path('general-details/', get_general_details_limited, name='general-details-limited'),
    path('general-details/<int:id>/', get_general_details_limited, name='general-details-detail'),
    path('get-by-pono/<str:pono>/', PurchasePODetailByPoNo.as_view(), name='get_by_pono'),
    path('get-by-pono-item/', GetByPoNoAndItem.as_view(), name='get_by_pono_item'),
    path('search-item/', ItemSearchAPIView.as_view(), name='search-item'),
    # path('generate-item-pdf/<int:pk>/', generate_item_pdf, name='generate-item-pdf'),
    path('gate-inward/pdf/<int:pk>/', generate_gateinward_pdf, name='gate-inward-pdf'),
    path('api/gate-inward/', GateInwardSummaryAPIView.as_view(), name='gate-inward-api'),
    path('NewDCgrn/', NewDCgrnCreateView.as_view(), name="NewDCgrn-Create-View"),
    path('NewDCgrn/<int:pk>/', NewDCgrnDetailView.as_view(), name="NewDCgrn-Detail-View"),
    path('57F4_InwardChallan/', InwardChallanCreateView.as_view(), name="Inward-Challan"),
    path('57F4_InwardChallan/<int:pk>/', InwardChallanDetailView.as_view(), name="Inward-Challan-Detail"),
    path('JobworkInwardChallan/', JobworkInwardChallanCreateView.as_view(), name="Jobwork-InwardChallan-CreateView"),
    path('JobworkInwardChallan/<int:pk>/', JobworkInwardChallanDetailView.as_view(), name="JobworkInward-ChallanDetail-View"),
    path('newjobworkpodetails/',get_purchase_orders_by_supplier, name='purchase-orders-by-supplier'),
    path('mrns/pending/', views.PendingMrnListView.as_view(), name='pending-mrns'),
    path('mrns/pending_mrn', views.get_pending_mrns, name='get_pending_mrn'),
    path('InwardChallan/pdf/<int:pk>/', generate_inwardchallan_pdf, name='pdf'),
    path('grn/heat-numbers/', views.get_grn_heat_numbers, name='get_grn_heat_numbers'),
    path('fg-movement/create/', views.create_fg_movement, name='create-fg-movement'),
    path('fg-movement/list/', views.get_fg_movements, name='get-fg-movements'),
    path('fg-movement/<int:movement_id>/', views.get_fg_movement_by_id, name='get-fg-movement-by-id'),
    path('fg-movement/<int:movement_id>/update/', views.update_fg_movement, name='update-fg-movement'),
    path('fg-movement/<int:movement_id>/delete/', views.delete_fg_movement, name='delete-fg-movement'),
    path('grn-calculation/<str:pono>/', GRNQuantityCalculation.as_view()),
    path('grn-calculation/', GRNQuantityByMultiplePOs.as_view()),
    path('api/grn/items/', views.get_grn_data, name='get_grn_data'),
    path('api/grn/items/<int:grn_id>/', views.get_grn_data, name='get_grn_data_by_id'),
    path('api/grn/summary/<int:grn_id>/', views.get_grn_summary, name='get_grn_summary'),

    path('api/WIPstockreport/',WIPStockreport.as_view(),name='WIP-stock-report'),
         # Store/api/WIPstockreport/?q=PC-001
]
