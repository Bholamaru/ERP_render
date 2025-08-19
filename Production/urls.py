from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'production-entries', ProductionEntryViewSet)
router.register(r'production-entries2', ProductionEntryViewSet2)
router.register(r'product-details', ProductDetailViewSet)
router.register(r'production-entriesAss', AssemblyProductionDetailsViewSet)
router.register(r'ProductionRecord', ProductionRecordViewSet)
router.register(r'FGScrapDetails',FGScrapDetailsViewSet)
router.register(r'ScrapLineRejectionNote',ScrapRejectionNoteViewSet)
router.register(r'work-order-entry', WorkOrderView)

urlpatterns = [
    path('api/', include(router.urls)),
    path('scrap_rejection/', ScrapRejectionListAPIView.as_view(), name='scrap_rejection_list'),  # List all and create
    path('scrap_rejection/<int:pk>/', ScrapRejectionDetailAPIView.as_view(), name='scrap_rejection_detail'),  # Get, Update, Delete a specific ScrapRejection
    path('scrap_rejection_no/', NextScrapRejectionAPIView.as_view(), name='next_scrap_rejection_no'),  # Get next rejection no
    path('Production_shift/', ProductionEntryShiftDetail.as_view(), name="Production-shift"),
    path('Production_contractor/',ProductionEntryContractorListView.as_view(), name = "Contractor-list"),
    path('Production_operators/', ProductionOperatorListView.as_view(), name="Operator-list"),
    path('Production_supervisor/', ProductionSupervisorListView.as_view(), name="Supervisor-list"),
    path('Production_Helper/', ProductionHelperListView.as_view(), name="Supervisor-list"),
    path('Production_unitmachine/', ProductionEntryUnitMachineListView.as_view(), name="UnitMachine-list"),
    # path('ProductDetail/', ProductDetailViewSet.as_view(), name="UnitMachine-list"),
    path('production-entries5/get_prod_no/', GetNextReworkNo.as_view(), name='get_next_heat_code'),
    path('api/get-next-dp-no/', GetNextDpNo.as_view(), name='get-next-dp-no'),
    path('ReworkReason2/', ReworkReason2ListCreate.as_view(), name='GeneralDetails-retrieve-list-create'),
    path('ReworkReason2/<int:pk>/', ReworkReason2RetrieveUpdateDestroy.as_view(), name='GeneralDetails-retrieve-update-destroy'),
    path('RejectReason2/', RejectReason2ListCreate.as_view(), name='GeneralDetails-retrieve-list-create'),
    path('RejectReason2/<int:pk>/', RejectReason2RetrieveUpdateDestroy.as_view(), name='GeneralDetails-retrieve-update-destroy'),
    path('GetNextNoteNo/', GetNextNoteNo.as_view(), name='get-next-Note-No'),
    path('GetNextNote/', GetNextNote.as_view(), name='get-next-Note'),
    path('api/work_order_entry/', WOGetNextDpNo.as_view(), name="create-work-order-entry"),
    path('Work_Order_Search_Customer/',Work_Order_Customer_Search.as_view(), name="Search-Customer"),
    path('ProductionEntry/pdf/<int:pk>/', generate_production_pdf, name='generate_production_pdf'),
    path('ProductionEntryList/', ProductionSummaryAPIView.as_view(), name='production_summary_api'),
    path('ProductionEntryAssembly/pdf/<int:pk>/', generate_assembly_pdf, name='generate_assembly_pdf'),
    path('ProductionEntryAssemblyList/', AssemblyProductionSummaryAPIView.as_view(), name='assembly_summary_api'),
    path('FGScrap/pdf/<int:pk>/', generate_FGScrap_pdf, name='fgscrap-pdf'),
    path('FGScrapRejectionReport/', FGScrapDetailsAPIView.as_view(), name='fgscrap-api'),
    path('scrap-line-rejection/pdf/<int:pk>/', generate_scrap_line_rejection_pdf, name='scrap-line-rejection-pdf'),
    path('ScrapLineRejectionReport/', ScrapLineRejectionAPIView.as_view(), name='scrap-line-rejection-api'),
    path('product-details/bulk/', ProductDetailBulkCreateView.as_view(), name='product-detail-bulk'),
    path('api/get-product-details/', ProductDetailGetView.as_view(), name='get-product-details'),

    path('api/item-dropdown/', ItemdropdownAPIView.as_view(), name='item-dropdown-search'),
      # search this type -api/item-dropdown/?q=Steel part

    path('api/bom-by-partcode/', BOMItemByPartCodeAPIView.as_view(), name='bom-by-partcode'),
    #     #    Production/api/bom-by-partcode/?part_code=PC-001

    path("api/grn/heat-numbers/", HeatNoListAPIView.as_view(), name="RM-stock-grn-heat-numbers"),
    
   
]