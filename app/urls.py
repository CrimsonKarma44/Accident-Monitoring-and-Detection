from django.urls import path
from .views import UploadView, RegularUploadView, RetrieveView, RetrieveRegionView, NewCameraView

urlpatterns = [
   path("upload/", UploadView.as_view()),
   path("camera/", NewCameraView.as_view()),
   path("rupload/", RegularUploadView.as_view()),
   path("ret/len=<int:pk>/", RetrieveView.as_view()),
   path("ret/region=<str:pk>/", RetrieveRegionView.as_view()),
   # path("dummy/", Dummy.as_view()),
]