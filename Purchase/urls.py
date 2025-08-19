from django.urls import path, include
from .views import *
from . import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'indents', IndentViewSet, basename='indent')
router.register(r'NewJobWorkPO', NewJobWorkPoInfoViewSet)
router.register(r'QuotationComparison',QuotationComparisonViewSet)
router.register(r'RFQ',RFQViewSet)

urlpatterns = router.urls + [ 
    path('api/', include(router.urls)),
    path('ItemDetail/', ItemDetailListCreate.as_view(), name='ItemDetail-retrieve-list-create'),
    path('ItemDetail/<int:pk>/', ItemDetailRetrieveUpdateDestroy.as_view(), name='ItemDetail-retrieve-update-destroy'),
    path('PO_Info/', PO_Info_ListCreate.as_view(), name='PO_Info-retrieve-list-create'),
    path('PO_Info/<int:pk>/', PO_Info_RetrieveUpdateDestroy.as_view(), name='PO_Info-retrieve-update-destroy'),
    path('Fetch_Supplier_Code/', Fetch_Supplier_Code_ListCreate.as_view(), name='Fetch_Supplier_Code'),
    path('Fetch_Item_fields/', Fetch_Item_fields_ListCreate.as_view(), name='Fetch_Supplier_Code'),
    path('JwPoInfo/', JwPoInfo_ListCreate.as_view(), name='JwPoInfo-retrieve-list-create'),
    path('JwPoInfo/<int:pk>/', JwPoInfo_RetrieveUpdateDestroy.as_view(), name='JwPoInfo-retrieve-update-destroy'),
    path('JwItem/', JwItem_ListCreate.as_view(), name='JwItem-retrieve-list-create'),
    path('JwItem/<int:pk>/', JwItem_RetrieveUpdateDestroy.as_view(), name='JwItem-retrieve-update-destroy'),
    path('JwShipAdd/', JwShipAdd_ListCreate.as_view(), name='JwShipAdd-retrieve-list-create'),
    path('JwShipAdd/<int:pk>/', JwShipAdd_RetrieveUpdateDestroy.as_view(), name='JwShipAdd-retrieve-update-destroy'),
    path('Fetch_PaymentTerm/', Fetch_PaymentTerm_ListCreate.as_view(), name='Fetch_PaymentTerm'),
    path('Quote_Comparison_Statement/', Quote_Comparison_Statement_ListCreate.as_view(), name='Quote_Comparison_Statement-retrieve-list-create'),
    path('Quote_Comparison_Statement/<int:pk>/', Quote_Comparison_Statement_RetrieveUpdateDestroy.as_view(), name='Quote_Comparison_Statement-retrieve-update-destroy'),
    path('generate_code/', GenerateCodeView.as_view(), name='generate_code'),
    # path('get_next_code/', GetNextCodeView.as_view(), name='get_next_code'),
    path('api/codegenerators/', CodeGeneratorListView.as_view(), name='codegenerator-list'),
    path('api/codegenerators/<int:pk>/', CodeGeneratorDetailView.as_view(), name='codegenerator-detail'),
    path('get_next_job_work_number/', views.get_next_job_work_number, name='get_next_job_work_number'),
    path('register_purchase_order/', views.register_purchase_order, name='register_purchase_order'),
    path('purchase_order_RUD/', views.RUDpurchase_order.as_view(), name='item-detail-list'),
    path('purchase_order_RUD/<int:pk>/', views.RUDpurchase_order_RetrieveUpdateDestroy.as_view(), name='item-detail-detail'),
    path('get_next_PurchaseNewIndent/', views.get_next_PurchaseNewIndent_number, name='get_next_PurchaseNewIndent_number'),
    path('register_PurchaseNewIndent/', views.register_PurchaseNewIndent, name='register_PurchaseNewIndent'),
    path('PurchaseNewIndent_RUD/', views.PurchaseNewIndent_RUD.as_view(), name='item-detail-list'),
    path('PurchaseNewIndent_RUD/<int:pk>/', views.PurchaseNewIndent_RUDeveUpdateDestroy.as_view(), name='item-detail-detail'),
    path('RegisterPO_All_Series/', RegisterPO.as_view(), name='RegisterPO_All_Series'),  # POST API
    path('RegisterPO_All_Series/<int:pk>/', PurchasePOView.as_view(), name='delete-purchasepo'),
    path('get_next_code/', PONextCode.as_view(), name='get_next_code'),    # GET A
    path('add-item-detail/', AddItemDetail.as_view(), name='add_item_detail'),
    # path('get-item-details/', GetItemDetails.as_view(), name='get_item_details'),
    # path('get-item-details/<int:id>/', GetItemDetails.as_view(), name='item_detail'),
    path('get-item-details/', GetItemDetails.as_view(), name='item_detail_list'),  # For all items
    path('get-item-details/<int:id>/', GetItemDetails.as_view(), name='item_detail'),  # For individual item
    path('get-next-indent-no/', GetNextIndentNo.as_view(), name='get_next_indent_no'),
    path('indent-list/', IndentDetailAPIView.as_view(), name='indent_list'),
    path('indent/pdf/<int:id>/', generate_indent_pdf, name='generate_indent_pdf'),
    path('api/indent/list/', FilteredIndentListAPIView.as_view(), name='filtered-indent-list'), 
    path('api/indent/auth/', ApproveRejectIndentAPIView.as_view(), name='approve-reject-indent'),
    path('api/indent/dropdown/', ApprovedIndentDropdownAPIView.as_view(), name='approved-indent-dropdown'),
    path('PurchaseOrderList/', ItemDetailAPIView.as_view(), name='item_summary'),
    path('PoOrder/pdf/<int:pk>/', generate_item_pdf, name='item_pdf'),
    path('api/transaction/create/', ItemTransactionCreateAPIView.as_view(), name='create-item-txn'),
    path('api/transaction/<int:pk>/', ItemTransactionDetailAPIView.as_view(), name='get-item-txn'),
    path('purchase-order/pdf/<int:pk>/', generate_po_pdf, name='generate_po_pdf'),
    path('JobWorkPOList/', NewJobWorkPoInfoAPIView.as_view(), name='new_job_work_po_info_api'),
    path('SuppilerJobWorkPoFetch/', JobWorkItemSearchView.as_view(), name='job-work-items'),
    path('purchase-orders/unverified/', views.get_unverified_purchase_orders, name='unverified_purchase_orders'),
    path('purchase-orders/all/', views.get_purchase_orders, name='purchase_orders_all'),
    path('purchase-orders/unverified/simple/', views.get_unverified_purchase_orders_simple, name='unverified_purchase_orders_simple'),
    path('purchase-po/<int:po_id>/update-status-fbv/', views.update_approved_status, name='update_approved_status_fbv'),
    path('all-indents/', views.get_indents, name='indents_all'),
    path('pending-indents/', views.get_pending_indents, name='pending_auth_indents_fbv'),
    path('indents/update-auth/', views.update_indent_auth_status, name='update_indent_auth'),
    path('QuotationComparison/delete/<int:pk>/', DeleteQuotationComparison.as_view(), name='quotationcomparison-delete'),
    path('QuotationComparison/edit/<int:pk>/', EditQuotationComparison.as_view(), name='quotationcomparison-edit'),
    path('GenrateRFQ/',generate_unique_rfq_no.as_view(),name='gererate_unique_rfq_no'),
    path('new-jobwork-item/', newjobworkitemdata.as_view(), name='new-jobwork-item'),
]