from django.urls import re_path
from .views import *

urlpatterns = [
    # buyer
    re_path(r'^LoginSystemListJson/$', LoginSystemListJson.as_view(), name='LoginSystemListJson'),
    re_path(r'^EmployeeListJson/$', EmployeeListJson.as_view(), name='EmployeeListJson'),
    re_path(r'^EmployeeListForAttendanceJson/$', EmployeeListForAttendanceJson.as_view(), name='EmployeeListForAttendanceJson'),
    re_path(r'^EmployeeListForAttendanceAdminJson/$', EmployeeListForAttendanceAdminJson.as_view(), name='EmployeeListForAttendanceAdminJson'),
    re_path(r'^EmployeeListForAttendanceAdminBasicJson/$', EmployeeListForAttendanceAdminBasicJson.as_view(), name='EmployeeListForAttendanceAdminBasicJson'),

    re_path(r'^attendance/$', attendance, name='attendance'),
    re_path(r'^attendanceReport/$', attendanceReport, name='attendanceReport'),


    re_path(r'^ManageLoginSystem/$', loginSystem, name='loginSystem'),
    re_path(r'^add_login_system_api/$', add_login_system_api, name='add_login_system_api'),
    re_path(r'^edit_login_system_api/$', edit_login_system_api, name='edit_login_system_api'),


    re_path(r'^manageEmployee/$', manageEmployee, name='manageEmployee'),
    re_path(r'^addEmployee/$', addEmployee, name='addEmployee'),
    re_path(r'^employee/edit/(?P<id>\d+)/$', edit_employee, name='edit_employee'),

    re_path(r'^add_employee_api/$', add_employee_api, name='add_employee_api'),
    re_path(r'^edit_employee_api/$', edit_employee_api, name='edit_employee_api'),
    re_path(r'^edit_employee_photo_api/$', edit_employee_photo_api, name='edit_employee_photo_api'),
    re_path(r'^delete_employee_api/$', delete_employee_api, name='delete_employee_api'),



    re_path(r'^login_post_api/$', login_post_api, name='login_post_api'),
    re_path(r'^logout_post_api/$', logout_post_api, name='logout_post_api'),
    re_path(r'^genereate_attendence_report/$', genereate_attendence_report, name='genereate_attendence_report'),
    re_path(r'^demoReport/$', demoReport, name='demoReport'),

]
