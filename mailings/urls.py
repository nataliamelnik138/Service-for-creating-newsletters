from django.urls import path
from mailings.apps import MailingsConfig
from mailings.views import MailingSettingsListView, MailingSettingsCreateView, MailingSettingsUpdateView, \
    MailingSettingsDetailView, MailingSettingsDeleteView, ClientsDeleteView, ClientsDetailView, ClientsUpdateView, \
    ClientsCreateView, ClientsListView, LogListView

app_name = MailingsConfig.name


urlpatterns = [
    path('', MailingSettingsListView.as_view(), name='list'),
    path('create/', MailingSettingsCreateView.as_view(), name='create'),
    path('edit/<int:pk>', MailingSettingsUpdateView.as_view(), name='edit'),
    path('view/<int:pk>', MailingSettingsDetailView.as_view(), name='view'),
    path('delete/<int:pk>', MailingSettingsDeleteView.as_view(), name='delete'),
    path('list_client/', ClientsListView.as_view(), name='list_client'),
    path('create_client/', ClientsCreateView.as_view(), name='create_client'),
    path('edit_client/<int:pk>', ClientsUpdateView.as_view(), name='edit_client'),
    path('view_client/<int:pk>', ClientsDetailView.as_view(), name='view_client'),
    path('delete_client/<int:pk>', ClientsDeleteView.as_view(), name='delete_client'),
    path('log', LogListView.as_view(), name='log'),
]
