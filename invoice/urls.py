from django.urls import re_path
from .views import *

urlpatterns = [
    # buyer

    re_path(r'^InvoiceSeriesListJson/$', InvoiceSeriesListJson.as_view(), name='InvoiceSeriesListJson'),
    re_path(r'^InvoiceCreatedByCashListJson/$', InvoiceCreatedByCashListJson.as_view(),
        name='InvoiceCreatedByCashListJson'),
    re_path(r'^InvoiceCreatedByCardListJson/$', InvoiceCreatedByCardListJson.as_view(),
        name='InvoiceCreatedByCardListJson'),
    re_path(r'^InvoiceCreatedByMixListJson/$', InvoiceCreatedByMixListJson.as_view(), name='InvoiceCreatedByMixListJson'),
    re_path(r'^InvoiceCreatedByCreditListJson/$', InvoiceCreatedByCreditListJson.as_view(),
        name='InvoiceCreatedByCreditListJson'),
    re_path(r'^CollectionListJson/$', CollectionListJson.as_view(), name='CollectionListJson'),
    re_path(r'^CashCollectionListJson/$', CashCollectionListJson.as_view(), name='CashCollectionListJson'),
    re_path(r'^StaffAdvanceListJson/$', StaffAdvanceListJson.as_view(), name='StaffAdvanceListJson'),
    re_path(r'^ReturnCollectionListJson/$', ReturnCollectionListJson.as_view(), name='ReturnCollectionListJson'),
    re_path(r'^CorrectCollectionListJson/$', CorrectCollectionListJson.as_view(), name='CorrectCollectionListJson'),
    re_path(r'^CommissionListJson/$', CommissionListJson.as_view(), name='CommissionListJson'),
    re_path(r'^ExpenseListJson/$', ExpenseListJson.as_view(), name='ExpenseListJson'),

    re_path(r'^$', index, name='index'),
    re_path(r'^get_invoice_series/$', get_invoice_series, name='get_invoice_series'),
    re_path(r'^create_invoice/$', create_invoice, name='create_invoice'),
    re_path(r'^edit_invoice/$', edit_invoice, name='edit_invoice'),
    re_path(r'^edit_invoice_mix/$', edit_invoice_mix, name='edit_invoice_mix'),
    re_path(r'^edit_collection/$', edit_collection, name='edit_collection'),
    re_path(r'^edit_collection_cash/$', edit_collection_cash, name='edit_collection_cash'),
    re_path(r'^delete_sale_api/$', delete_sale_api, name='delete_sale_api'),
    re_path(r'^delete_sale_api_mix/$', delete_sale_api_mix, name='delete_sale_api_mix'),
    re_path(r'^delete_collection_api/$', delete_collection_api, name='delete_collection_api'),
    re_path(r'^delete_cash_collection_api/$', delete_cash_collection_api, name='delete_cash_collection_api'),
    re_path(r'^generateInvoice/$', generate_serial_invoice_number, name='generate_serial_invoice_number'),

    re_path(r'^manage_invoice/$', invoice_list, name='manage_invoice'),
    re_path(r'^add_invoice_serial/$', add_invoice_serial, name='add_invoice_serial'),
    re_path(r'^edit_invoice_serial/$', edit_invoice_serial, name='edit_invoice_serial'),

    re_path(r'^invoice_report/$', invoice_report, name='invoice_report'),
    re_path(r'^generate_net_report/$', generate_net_report, name='generate_net_report'),
    re_path(r'^generate_net_report_admin/$', generate_net_report_admin, name='generate_net_report_admin'),
    re_path(r'^generate_net_report_accountant/$', generate_net_report_accountant, name='generate_net_report_accountant'),
    re_path(r'^generate_monthly_report_admin/$', generate_monthly_report_admin, name='generate_monthly_report_admin'),
    re_path(r'^generate_monthly_report_staff_advance_admin/$', generate_monthly_report_staff_advance_admin, name='generate_monthly_report_staff_advance_admin'),

    re_path(r'^search_invoice/$', search_invoice, name='search_invoice'),
    re_path(r'^skipped_invoice/$', skipped_invoice, name='skipped_invoice'),
    re_path(r'^take_collection/$', take_collection, name='take_collection'),
    re_path(r'^take_cash_collection/$', take_cash_collection, name='take_cash_collection'),

    re_path(r'^get_today_collection_by_company/$', get_today_collection_by_company, name='get_today_collection_by_company'),
    re_path(r'^get_today_cash_collection_by_company/$', get_today_cash_collection_by_company,
        name='get_today_cash_collection_by_company'),
    re_path(r'^add_party_from_sales/$', add_party_from_sales, name='add_party_from_sales'),
    re_path(r'^get_buyer_list/$', get_buyer_list, name='get_buyer_list'),

    re_path(r'^change_password_for_sales_user/$', change_password_for_sales_user, name='change_password_for_sales_user'),
    re_path(r'^get_last_three_invoices/$', get_last_three_invoices, name='get_last_three_invoices'),
    re_path(r'^generate_collection_report_admin/$', generate_collection_report_admin,
        name='generate_collection_report_admin'),
    re_path(r'^generate_collection_report_supplier/$', generate_collection_report_supplier,
        name='generate_collection_report_supplier'),
    re_path(r'^generate_collection_report/$', generate_collection_report, name='generate_collection_report'),

    # Accountant
    re_path(r'^collection_report_accountant/$', collection_report_accountant, name='collection_report_accountant'),

    # Return
    re_path(r'^return_collection_post/$', return_collection, name='return_collection'),
    re_path(r'^get_today_return_by_company/$', get_today_return_by_company, name='get_today_return_by_company'),
    re_path(r'^edit_return/$', edit_return, name='edit_return'),
    re_path(r'^delete_return_api/$', delete_return_api, name='delete_return_api'),

    # Commission
    re_path(r'^commission_collection_post/$', commission_collection, name='commission_collection'),
    re_path(r'^get_today_commission_by_company/$', get_today_commission_by_company, name='get_today_commission_by_company'),
    re_path(r'^edit_commission/$', edit_commission, name='edit_commission'),
    re_path(r'^delete_commission_api/$', delete_commission_api, name='delete_commission_api'),

    # Correction
    re_path(r'^correction_collection_post/$', correct_collection, name='correct_collection'),
    re_path(r'^get_today_correction_by_company/$', get_today_correction_by_company, name='get_today_correction_by_company'),
    re_path(r'^edit_correction/$', edit_correction, name='edit_correction'),
    re_path(r'^delete_correction_api/$', delete_correction_api, name='delete_correction_api'),

    # expense
    re_path(r'^add_expense/$', add_expense, name='add_expense'),
    re_path(r'^get_today_expense_by_company/$', get_today_expense_by_company, name='get_today_expense_by_company'),
    re_path(r'^edit_expense/$', edit_expense, name='edit_expense'),
    re_path(r'^delete_expense_api/$', delete_expense_api, name='delete_expense_api'),

    re_path(r'^add_closing_balance_api/$', add_closing_balance_api, name='add_closing_balance_api'),

    # staffAdvance
    re_path(r'^staff_advance_post/$', staff_advance_post, name='staff_advance_post'),
    re_path(r'^get_today_staff_advance_by_company/$', get_today_staff_advance_by_company,
        name='get_today_staff_advance_by_company'),
    re_path(r'^edit_staff_advance/$', edit_staff_advance, name='edit_staff_advance'),
    re_path(r'^delete_staff_advance_api/$', delete_staff_advance_api, name='delete_staff_advance_api'),


    re_path(r'^edit_cash_invoice_report/$', edit_cash_invoice_report, name='edit_cash_invoice_report'),

]
