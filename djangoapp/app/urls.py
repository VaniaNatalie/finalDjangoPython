from django.urls import path
from . import views
from .views import DiaryLogs, IndividualDiaryLogs, NewDiaryLogs, EditDiaryLogs, DeleteDiaryLogs

# URL destination for each pages
urlpatterns = [
    path('', views.home, name="app-home"),
    path('yourdiary/', DiaryLogs.as_view(), name="app-diary"),
    path('yourdiary/<int:pk>/', IndividualDiaryLogs.as_view(), name="diary-log"),
    path('yourdiary/new/', NewDiaryLogs.as_view(), name="diary-new"),
    path('yourdiary/<int:pk>/edit/', EditDiaryLogs.as_view(), name="diary-edit"),
    path('yourdiary/<int:pk>/delete/', DeleteDiaryLogs.as_view(), name="diary-delete"),
    path('about/', views.about, name="app-about"),
    path('account/', views.account, name="app-account"),
    path('account/settings/', views.settings, name="app-settings"),
]