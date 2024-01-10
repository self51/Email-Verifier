"""EmailVerifier's view."""
import os

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import DeleteView, ListView, View

from .models import History
from .service import APIRequestManager


class EmailVerifier(View):

    def get(self, *args):
        if self.request.GET.get('email'):
            params_data = {
                'email': self.request.GET.get('email'),
                'api_key': os.getenv('API_KEY'),
            }

            request_builder = APIRequestManager('email-verifier', params_data)
            status_code, verification_response = request_builder.make_request()

            if 'errors' in verification_response:
                context_data = {'status_code': status_code}
            else:
                context_data = {
                    'email': verification_response['data']['email'],
                    'status': verification_response['data']['status'],
                    'score': verification_response['data']['score'],
                    'sources': verification_response['data']['sources'],
                }
                self.request.session['context_data'] = context_data

            return render(
                self.request,
                'email_verifier/email_verifier_result.html',
                {'context_data': context_data},
            )

        return render(self.request, 'email_verifier/email_verifier.html')

    def post(self, *args):
        context_data = self.request.session['context_data']

        try:
            History.objects.create(
                email=context_data['email'],
                status=context_data['status'],
                score=context_data['score'],
            ).save()
        finally:
            return HttpResponseRedirect(reverse('verification_service:history'))


class Account(View):
    def get(self, *args: object) -> object:
        request_builder = APIRequestManager(
            'account',
            {'api_key': os.getenv('API_KEY')},
        )
        status_code, verification_response = request_builder.make_request()

        if 'errors' in verification_response:
            context_data = {'status_code': status_code}
        else:
            verification_data = verification_response['data']
            context_data = {
                'first_name': verification_data['first_name'],
                'last_name': verification_data['last_name'],
                'email': verification_data['email'],
                'plan_name': verification_data['plan_name'],
                'used': verification_data['calls']['used'],
                'available': verification_data['calls']['available'],
            }

        return render(
            self.request,
            'email_verifier/account.html',
            {'context_data': context_data},
        )


class HistoryListView(ListView):
    context_object_name = 'entries'
    model = History
    template_name = 'email_verifier/history.html'


class HistoryDeleteView(DeleteView):
    model = History
    success_url = reverse_lazy('verification_service:history')
