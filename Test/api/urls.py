from django.urls import path,re_path
from api import views
from api import loginview

urlpatterns=[
        path('login',loginview.user_login),
	path('api/v1/location/', views.MetadataList.as_view()),
        re_path(r'^api/v1/location/(?P<location_id>\w+)/department/$',views.Locationdept.as_view(),name= 'department'),
        re_path(r'^api/v1/location/(?P<location_id>\w+)/department/(?P<department_id>\w+)/category/$',views.Departments.as_view(), name='dapartments'),
        re_path(r'^api/v1/location/(?P<location_id>\w+)/department/(?P<department_id>[\w|\W]+)/category/(?P<category_id>[\w|\W]+)/subcategory/$',views.Category.as_view()),
        re_path(r'^api/v1/location/(?P<location_id>[\w|\W]+)/department/(?P<department_id>[\w|\W]+)/category/(?P<category_id>[\w|\W]+)/subcategory/(?P<subcategory_id>[\w|\W]+)/$',views.Subcategory.as_view()),

]
