"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import  re_path
from base_app import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve

urlpatterns = [
    #re_path('admin/', admin.site.urls),
    re_path(r'^$', views.login,name='login'),
    re_path(r'^logout/$', views.logout,name='logout'),
    re_path(r'^internshipform/$', views.internshipform,name='internshipform'),
    re_path(r'^internship_save/$', views.internship_save,name='internship_save'),
    re_path(r'^leave/$', views.leave,name='leave'),
    re_path(r'^man_registration_form/$', views.man_registration_form,name='man_registration_form'),
    re_path(r'^man_registration_formsave/$', views.man_registration_formsave,name='man_registration_formsave'),
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),


    #Project manager
    #---------------------------------------------------------------------------------------------------------
    re_path(r'^pmanager_dash', views.pmanager_dash,name="pmanager_dash"),
    re_path(r'^projectmanager_projects', views.projectmanager_projects, name="projectmanager_projects"),

    #nirmal
    re_path(r'^projectmanager_assignproject', views.projectmanager_assignproject, name="projectmanager_assignproject"),

    #jensin
    re_path(r'^projectmanager_createproject', views.projectmanager_createproject, name="projectmanager_createproject"),

    #maneesh
    re_path(r'^projectmanager_description/(?P<id>\d+)/', views.projectmanager_description, name="projectmanager_description"),
    re_path(r'^projectmanager_table', views.projectmanager_table, name="projectmanager_table"),
    re_path(r'^projectmanager_upprojects', views.projectmanager_upprojects, name="projectmanager_upprojects"),

    #praveesh
    re_path(r'^projectmanager_accepted_projects', views.projectmanager_accepted_projects, name="projectmanager_accepted_projects"),
    re_path(r'^projectmanager_rejected_projects', views.projectmanager_rejected_projects, name="projectmanager_rejected_projects"),



    #amal#bibin#rohit#abin
    re_path(r'^manindex/$', views.manindex, name='manindex'),
    re_path(r'^projectmanEmp/$', views.projectmanEmp, name='projectmanEmp'),
    re_path(r'^projectmanDev/$', views.projectmanDev, name='projectmanDev'),
    re_path(r'^projectmanDevDashboard/(?P<id>\d+)/$', views.projectmanDevDashboard, name='projectmanDevDashboard'),
    re_path(r'^projectman_developer_attendance/(?P<id>\d+)/$', views.projectman_developer_attendance, name='projectman_developer_attendance'),

    re_path(r'^projectman_team/(?P<id>\d+)/$', views.projectman_team, name='projectman_team'),
    re_path(r'^projectman_team_profile/(?P<id>\d+)/$', views.projectman_team_profile, name='projectman_team_profile'),
    re_path(r'^projectman_team_attendance/(?P<id>\d+)/$', views.projectman_team_attendance, name='projectman_team_attendance'),
    re_path(r'^projectman_team_attandance/(?P<id>\d+)/$', views.projectman_team_attandance, name='projectman_team_attandance'),

    re_path(r'^projectMANattendance/$', views.projectMANattendance, name='projectMANattendance'),
    re_path(r'^projectMANattandance/$', views.projectMANattandance, name='projectMANattandance'),

    re_path(r'^projectMANreportedissues$', views.projectMANreportedissues, name='projectMANreportedissues'),
    re_path(r'^projectMANreportedissue$', views.projectMANreportedissue, name='projectMANreportedissue'),
    re_path(r'^projectMANreportissue$', views.projectMANreportissue, name='projectMANreportissue'),
    re_path(r'^projectmanagerreportedissue2/(?P<id>\d+)/$', views.projectmanagerreportedissue2, name='projectmanagerreportedissue2'),
    re_path(r'^projectmanagerreportedissue3/(?P<id>\d+)/$', views.projectmanagerreportedissue3, name='projectmanagerreportedissue3'),
    re_path(r'^MANreportsuccess$', views.MANreportsuccess, name='MANreportsuccess'),
    re_path(r'^projectreply/(?P<id>\d+)/$', views.projectreply, name='projectreply'), 
    

    re_path(r'^projectMANleave/$', views.projectMANleave, name='projectMANleave'),
    re_path(r'^projectMANleavereq/$', views.projectMANleavereq, name='projectMANleavereq'),
    re_path(r'^projectMANreqedleave/$', views.projectMANreqedleave, name='projectMANreqedleave'),

    re_path(r'^Manager_employees/$', views.Manager_employees, name='Manager_employees'),
    re_path(r'^projectManager_tl/$', views.projectManager_tl, name='projectManager_tl'),
    re_path(r'^projectManager_tl_dashboard/(?P<id>\d+)/$', views.projectManager_tl_dashboard, name='projectManager_tl_dashboard'),
    re_path(r'^man_tl_attendance/$', views.man_tl_attendance, name='man_tl_attendance'), 

    re_path(r'^projectmanager_currentproject/$', views.projectmanager_currentproject, name='projectmanager_currentproject'), 
    re_path(r'^projectmanager_currentdetail/(?P<id>\d+)/$', views.projectmanager_currentdetail, name='projectmanager_currentdetail'), 
    
    re_path(r'^projectmanager_completeproject/$', views.projectmanager_completeproject, name='projectmanager_completeproject'),
    re_path(r'^projectmanager_completedetail/(?P<id>\d+)/$', views.projectmanager_completedetail, name='projectmanager_completedetail'), 
    re_path(r'^projectmanager_completeteam/(?P<id>\d+)/$', views.projectmanager_completeteam, name='projectmanager_completeteam'),
    re_path(r'^projectmanager_teaminvolved/(?P<id>\d+)/$', views.projectmanager_teaminvolved, name='projectmanager_teaminvolved'),
    re_path(r'^projectmanager_devteam/(?P<id>\d+)/$', views.projectmanager_devteam, name='projectmanager_devteam'),

    re_path(r'^projectmanager_currentteam/(?P<id>\d+)/$', views.projectmanager_currentteam, name='projectmanager_currentteam'),
    re_path(r'^projectmanager_currenttl/(?P<id>\d+)/$', views.projectmanager_currenttl, name='projectmanager_currenttl'),
    re_path(r'^projectmanager_completetl/(?P<id>\d+)/$', views.projectmanager_completetl, name='projectmanager_completetl'),
    re_path(r'^projectmanager_tlreported/$', views.projectmanager_tlreported, name='projectmanager_tlreported'), 
    re_path(r'^TLlogout/$', views.TLlogout, name='TLlogout'),
    re_path(r'^ProMANlogout/$', views.ProMANlogout, name='ProMANlogout'),
 

    re_path(r'^projectmanager_accepted_projects', views.projectmanager_accepted_projects, name="projectmanager_accepted_projects"),    
    re_path(r'^projectmanager_rejected_projects', views.projectmanager_rejected_projects, name="projectmanager_rejected_projects"),


    re_path(r'^projectmanager_completeproject$', views.projectmanager_completeproject, name='projectmanager_completeproject'),
    re_path(r'^projectmanager_completedetail/(?P<id>\d+)/$', views.projectmanager_completedetail, name='projectmanager_completedetail'), 
    re_path(r'^projectmanager_completeteam/(?P<id>\d+)/$', views.projectmanager_completeteam, name='projectmanager_completeteam'),
    re_path(r'^projectmanager_completetl$', views.projectmanager_completetl, name='projectmanager_completetl'),

    re_path(r'^projectmanager_assignproject', views.projectmanager_assignproject, name="projectmanager_assignproject"),

    re_path(r'^projectmanager_createproject', views.projectmanager_createproject, name="projectmanager_createproject"),

#---------------------------------------------------------------------------------------------------------------------------

#  Teamleader
    re_path(r'^projectreplytl/(?P<id>\d+)/$', views.projectreplytl, name='projectreplytl'), 
    re_path(r'^TLdashboard/$', views.TLdashboard, name='TLdashboard'),
    re_path(r'^TLattendance/$', views.TLattendance, name='TLattendance'),
    re_path(r'^TLattendancesort/$', views.TLattendancesort, name='TLattendancesort'),
    re_path(r'^TLprojects/$', views.TLprojects, name='TLprojects'),
    re_path(r'^TLreportissues/$', views.TLreportissues, name='TLreportissues'),
    re_path(r'^TLtasks/$', views.TLtasks, name='TLtasks'),
    re_path(r'^TLleave/$', views.TLleave, name='TLleave'),
    re_path(r'^tlprojecttasks/(?P<id>\d+)/$', views.tlprojecttasks, name='tlprojecttasks'),
    re_path(r'^TLreportedissue1/$', views.TLreportedissue1, name='TLreportedissue1'),
    re_path(r'^TLreportedissue2/(?P<id>\d+)/$', views.TLreportedissue2, name='TLreportedissue2'),
    re_path(r'^TLreport1/$', views.TLreport1, name='TLreport1'),
    re_path(r'^tlgivetask/$', views.tlgivetask, name='tlgivetask'),
    re_path(r'^TLreportsuccess/$', views.TLreportsuccess, name='TLreportsuccess'),
    re_path(r'^tltaskstatus/(?P<id>\d+)/$', views.tltaskstatus, name='tltaskstatus'),
    re_path(r'^tlsplittask/(?P<id>\d+)/$', views.tlsplittask, name='tlsplittask'), 
    re_path(r'^TLgavetask/(?P<id>\d+)/$', views.TLgavetask, name='TLgavetask'),
    re_path(r'^TLgivetasks/(?P<id>\d+)/$', views.TLgivetasks, name='TLgivetasks'),
    re_path(r'^TLtaskformsubmit/(?P<id>\d+)/$', views.TLtaskformsubmit, name='TLtaskformsubmit'),
    re_path(r'^TLleavereq/$', views.TLleavereq, name='TLleavereq'),
    re_path(r'^TLreqedleave/$', views.TLreqedleave, name='TLreqedleave'),
    re_path(r'^tl_leave_form/$', views.tl_leave_form, name='tl_leave_form'),
    re_path(r'^extensionsave/(?P<id>\d+)/$', views.extensionsave, name='extensionsave'),
    re_path(r'^extensionapprove/(?P<id>\d+)/$', views.extensionapprove, name='extensionapprove'),
    re_path(r'^extensionreject/(?P<id>\d+)/$', views.extensionreject, name='extensionreject'),
    re_path(r'^tlprojectsave/(?P<id>\d+)/$', views.tlprojectsave, name='tlprojectsave'),
    re_path(r'^pdetailsave/(?P<id>\d+)/$', views.pdetailsave, name='pdetailsave'),
    re_path(r'^devtlreported/$', views.devtlreported, name='devtlreported'),
    re_path(r'^tldevview/(?P<id>\d+)/$', views.tldevview, name='tldevview'),
    # re_path(r'^TLleave$', views.TLleave, name='TLleave'),

    # re_path(r'^TLleavereq$', views.TLleavereq, name='TLleavereq'), 
    # re_path(r'^TLreqedleave$', views.TLreqedleave, name='TLreqedleave'),

#-------------------------------------------------------------------------------------------------------
#tester module

    re_path(r'^TSassigned/(?P<id>\d+)/$', views.TSassigned, name='TSassigned'),
    re_path(r'^TSdashboard/$', views.TSdashboard, name='TSdashboard'),
    re_path(r'^TSproject/$', views.TSproject, name='TSproject'),
    re_path(r'^TSprojectdetails/(?P<pid>\d+)/$', views.TSprojectdetails, name='TSprojectdetails'),
    re_path(r'^TSsubmitted/(?P<id>\d+)/$', views.TSsubmitted, name='TSsubmitted'),
     re_path(r'^TSsubmittedsave/(?P<id>\d+)/$', views.TSsubmittedsave, name='TSsubmittedsave'),
    re_path(r'^TStask/$', views.TStask, name='TStask'),
    re_path(r'^TSsucess/$', views.TSsucess, name='TSsucess'),

    re_path(r'^testersave/(?P<uid>\d+)/(?P<pid>\d+)/$', views.testersave, name='testersave'),
    re_path(r'^projectdetailsave/(?P<uid>\d+)/(?P<pid>\d+)/$', views.projectdetailsave, name='projectdetailsave'),

#-------------------------------------------------------------------------------------------------------------------------------
#developer module
    re_path(r'^devindex/$', views.devindex, name='devindex'),
    re_path(r'^devdashboard/$', views.devdashboard, name='devdashboard'),
    re_path(r'^devReportedissues/$', views.devReportedissues, name='devReportedissues'),
    re_path(r'^devreportissue/$', views.devreportissue, name='devreportissue'),
    re_path(r'^devreportedissue/$', views.devreportedissue, name='devreportedissue'),
    re_path(r'^devsuccess/$', views.devsuccess, name='devsuccess'),
    re_path(r'^devissues/(?P<id>\d+)/$', views.devissues, name='devissues'),
    re_path(r'^dev_leave_form/$', views.dev_leave_form, name='dev_leave_form'),
    re_path(r'^dev_task_submit/$', views.dev_task_submit, name='dev_task_submit'),
    re_path(r'^DEVtaskformsubmit/(?P<id>\d+)/$', views.DEVtaskformsubmit, name='DEVtaskformsubmit'),
    re_path(r'^DEVtasksumitted/$', views.DEVtasksumitted, name='DEVtasksumitted'),
    re_path(r'^DEVtaskstatus/(?P<id>\d+)/$', views.DEVtaskstatus, name='DEVtaskstatus'),
    re_path(r'^DEVextension/(?P<id>\d+)/$', views.DEVextension, name='DEVextension'),
    re_path(r'^devprjsave/(?P<id>\d+)/$', views.devprjsave, name='devprjsave'),
    


    re_path(r'^Devapplyleav/$', views.Devapplyleav, name='Devapplyleav'),
    re_path(r'^Devapplyleav1/$', views.Devapplyleav1, name='Devapplyleav1'),
    re_path(r'^Devapplyleav2/$', views.Devapplyleav2, name='Devapplyleav2'),
    re_path(r'^Devleaverequiest/$', views.Devleaverequiest, name='Devleaverequiest'),
    re_path(r'^Devattendance/$', views.Devattendance, name='Devattendance'),
    re_path(r'^Devattendancesort/$', views.Devattendancesort, name='Devattendancesort'),
    re_path(r'^Devapplyleav3/$', views.Devapplyleav3, name='Devapplyleav3'),



    re_path(r'^DEVprojects/$', views.DEVprojects, name='DEVprojects'),
    re_path(r'^DEVsuccess/$', views.DEVsuccess, name='DEVsuccess'),
    re_path(r'^DEVtable/(?P<id>\d+)/$', views.DEVtable, name='DEVtable'),
    re_path(r'^DEVtask/(?P<id>\d+)/$', views.DEVtask, name='DEVtask'),
    re_path(r'^DEVtaskform/(?P<id>\d+)/$', views.DEVtaskform, name='DEVtaskform'),
    re_path(r'^DEVtaskmain/$', views.DEVtaskmain, name='DEVtaskmain'),
    re_path(r'^devlogout/$', views.devlogout, name='devlogout'),

]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
    urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)