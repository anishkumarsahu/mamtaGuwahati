
from django.urls import re_path, path
from .views import *



urlpatterns = [
    # buyer
    re_path(r'^InvoicePrintListJson/$', InvoicePrintListJson.as_view(), name='InvoicePrintListJson'),
    re_path(r'^LoginListJson/$', LoginListJson.as_view(), name='LoginListJson'),
    re_path(r'^LogoutListJson/$', LogoutListJson.as_view(), name='LogoutListJson'),
    re_path(r'^buyerList/$', BuyerListJson.as_view(), name='BuyerListJson'),
    re_path(r'^ManageCreditListJson/$', ManageCreditListJson.as_view(), name='ManageCreditListJson'),
    re_path(r'^CreditListJson/$', CreditListJson.as_view(), name='CreditListJson'),
    re_path(r'^DebitListJson/$', DebitListJson.as_view(), name='DebitListJson'),
    re_path(r'^CollectionListCashJson/$', CollectionListCashJson.as_view(), name='CollectionListCashJson'),
    re_path(r'^CollectionListChequeJson/$', CollectionListChequeJson.as_view(), name='CollectionListChequeJson'),
    re_path(r'^ManageCompanyListJson/$', ManageCompanyListJson.as_view(), name='ManageCompanyListJson'),
    re_path(r'^StaffListJson/$', StaffListJson.as_view(), name='StaffListJson'),
    re_path(r'^SupplierCollectionListJson/$', SupplierCollectionListJson.as_view(), name='SupplierCollectionListJson'),
    re_path(r'^SupplierInvoiceCollectionListJson/$', SupplierInvoiceCollectionListJson.as_view(), name='SupplierInvoiceCollectionListJson'),
    re_path(r'^SupplierCollectionListCashJson/$', SupplierCollectionListCashJson.as_view(), name='SupplierCollectionListCashJson'),
    re_path(r'^SupplierCollectionAdminListCashJson/$', SupplierCollectionAdminListCashJson.as_view(), name='SupplierCollectionAdminListCashJson'),
    re_path(r'^SupplierCollectionListChequeJson/$', SupplierCollectionListChequeJson.as_view(), name='SupplierCollectionListChequeJson'),
    re_path(r'^SupplierCollectionAdminListChequeJson/$', SupplierCollectionAdminListChequeJson.as_view(), name='SupplierCollectionAdminListChequeJson'),

    re_path(r'^$', home, name='home'),
    # staff
    re_path(r'^staff/$', staff, name='staff'),
    re_path(r'^staff/add/$', add_staff, name='add_staff'),
    re_path(r'^staff/detail/(?P<id>\d+)/$', detail_staff, name='detail_staff'),
    re_path(r'^staff/edit/(?P<id>\d+)/$', edit_staff, name='edit_staff'),

    # staff api
    re_path(r'^staff/add/api/$', add_staff_user_api, name='add_staff_user_api'),
    re_path(r'^staff/edit/api/$', edit_staff_user_api, name='edit_staff_user_api'),
    re_path(r'^staff/photo_edit/api/$', edit_staff_photo_api, name='edit_staff_photo_api'),
    re_path(r'^staff/idproof_edit/api/$', edit_staff_idproof_api, name='edit_staff_idproof_api'),
    re_path(r'^staff/delete/api/$', delete_staff_user_api, name='delete_staff_user_api'),

    # buyers
    re_path(r'^buyers/$', buyers, name='buyers'),
    re_path(r'^buyers/add/$', add_buyer, name='add_buyer'),
    re_path(r'^buyers/detail/(?P<id>\d+)/$', detail_buyer, name='detail_buyer'),
    re_path(r'^buyers/edit/(?P<id>\d+)/$', edit_buyer, name='edit_buyer'),

    # buyers api
    re_path(r'^buyers/add/api/$', add_buyer_api, name='add_buyer_api'),
    re_path(r'^buyers/edit/api/$', edit_buyer_api, name='edit_buyer_api'),
    re_path(r'^buyers/delete/api/$', delete_buyer_api, name='delete_buyer_api'),

    # credits
    re_path(r'^buyers/credit/add/api/$', add_money_to_be_collected_api, name='add_money_to_be_collected_api'),

    # report
    re_path(r'^report/$', report, name='report'),
    # report
    re_path(r'^manage_credits/$', manage_credits, name='manage_credits'),

    # login
    re_path(r'^login/$', loginApp, name='loginApp'),

    # logout
    re_path(r'^Logout/$', logout_user, name='logout'),

    # profile
    re_path(r'^profile/$', profile, name='profile'),
    re_path(r'^change_password/$', change_password_api, name='change_password_api'),


    re_path(r'^manage_company/$', manage_company, name='manage_company'),
    re_path(r'^add_company_api/$', add_company_api, name='add_company_api'),
    re_path(r'^edit_company_api/$', edit_company_api, name='edit_company_api'),


    #supply
    re_path(r'^supplyHome/$', supply_home, name='supply_home'),
    re_path(r'^supplier_collection_report/$', supplier_collection_report, name='supplier_collection_report'),
    re_path(r'^take_collection_supplier_api/$', take_collection_supplier_api, name='take_collection_supplier_api'),
    re_path(r'^take_collection_invoice_supplier_api/$', take_collection_invoice_supplier_api, name='take_collection_invoice_supplier_api'),
    re_path(r'^edit_collection_supplier_api/$', edit_collection_supplier_api, name='edit_collection_supplier_api'),
    re_path(r'^approve_collection_supplier_api/$', approve_collection_supplier_api, name='approve_collection_supplier_api'),
    re_path(r'^delete_collection_supplier_api/$', delete_collection_supplier_api, name='delete_collection_supplier_api'),

    # username exist?
    re_path(r'^user_name_exist/$', user_name_exist, name='user_name_exist'),

    # login logout report
    re_path(r'^login_and_logout_report/$', login_and_logout_report, name='login_and_logout_report'),

    #cashier
    re_path(r'^cashierHome/$', cashier_home, name='cashier_home'),

    #print Report
    re_path(r'^print_report/$', print_report, name='print_report'),
    re_path(r'^EditedCashInvoiceAdminListJson/$', EditedCashInvoiceAdminListJson.as_view(), name='EditedCashInvoiceAdminListJson'),

]
