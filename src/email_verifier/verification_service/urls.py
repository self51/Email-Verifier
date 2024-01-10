"""EmailVerifier's urls."""

from django.urls import path

from .views import Account, EmailVerifier, HistoryDeleteView, HistoryListView

app_name = 'verification_service'
urlpatterns = (
    path('', EmailVerifier.as_view(), name='email_verifier'),
    path('account', Account.as_view(), name='account'),
    path('history', HistoryListView.as_view(), name='history'),
    path('history/delete/<int:pk>', HistoryDeleteView.as_view(), name='history-delete'),
)
