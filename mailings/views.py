from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


from mailings.models import MailingSettings, Clients, Log


class MailingSettingsCreateView(LoginRequiredMixin, CreateView):
    model = MailingSettings
    fields = ('start_date', 'end_date', 'periodicity', 'message', 'clients')
    success_url = reverse_lazy('mailings:list')


class MailingSettingsUpdateView(LoginRequiredMixin, UpdateView):
    model = MailingSettings
    fields = ('start_date', 'end_date', 'periodicity', 'message', 'clients')
    success_url = reverse_lazy('mailings:list')


class MailingSettingsListView(LoginRequiredMixin, ListView):
    model = MailingSettings
    extra_context = {
        'title': 'Список рассылок'
    }


class MailingSettingsDetailView(LoginRequiredMixin, DetailView):
    model = MailingSettings

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(**kwargs)
        mailings_item = MailingSettings.objects.get(pk=self.kwargs.get('pk'))
        context_data['pk'] = mailings_item.pk
        context_data['title'] = 'Рассылка ID ' + str(mailings_item.pk)
        return context_data


class MailingSettingsDeleteView(LoginRequiredMixin, DeleteView):
    model = MailingSettings
    success_url = reverse_lazy('mailings:list')


class ClientsCreateView(LoginRequiredMixin, CreateView):
    model = Clients
    fields = ('email', 'fullname', 'comment')
    success_url = reverse_lazy('mailings:list_client')


class ClientsUpdateView(LoginRequiredMixin, UpdateView):
    model = Clients
    fields = ('email', 'fullname', 'comment')
    success_url = reverse_lazy('mailings:list_client')


class ClientsListView(LoginRequiredMixin, ListView):
    model = Clients
    extra_context = {
        'title': 'Список клиентов'
    }


class ClientsDetailView(LoginRequiredMixin, DetailView):
    model = Clients

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(**kwargs)
        mailings_item = Clients.objects.get(pk=self.kwargs.get('pk'))
        context_data['pk'] = mailings_item.pk
        context_data['title'] = 'Клиент:  ' + mailings_item.fullname
        return context_data


class ClientsDeleteView(LoginRequiredMixin, DeleteView):
    model = Clients
    success_url = reverse_lazy('mailings:list_client')


class LogListView(LoginRequiredMixin, ListView):
    model = Log
    extra_context = {
        'title': 'Отчет проведенных рассылок'
    }


@login_required
def get_mailing_logs(request, pk):
    mailing_pk = pk

    context = {
        'object_list': Log.objects.filter(mailing_id=mailing_pk),
        'title': 'Логи рассылки'
    }
    return render(request, 'mailings/mailing_logs.html', context)
