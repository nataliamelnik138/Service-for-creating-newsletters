from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


from mailings.models import MailingSettings, Clients
from mailings.services import send_mailing


class MailingSettingsCreateView(CreateView):
    model = MailingSettings
    fields = ('start_date', 'end_date', 'periodicity', 'message', 'clients')
    success_url = reverse_lazy('mailings:list')

    def form_valid(self, form):
        obj = form.save()
        send_mailing(obj)
        return super().form_valid(form)


class MailingSettingsUpdateView(UpdateView):
    model = MailingSettings
    fields = ('start_date', 'end_date', 'periodicity', 'message', 'clients')
    success_url = reverse_lazy('mailings:list')


class MailingSettingsListView(ListView):
    model = MailingSettings
    extra_context = {
        'title': 'Список рассылок'
    }


class MailingSettingsDetailView(DetailView):
    model = MailingSettings

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(**kwargs)
        mailings_item = MailingSettings.objects.get(pk=self.kwargs.get('pk'))
        context_data['pk'] = mailings_item.pk
        context_data['title'] = 'Рассылка ID ' + str(mailings_item.pk)
        return context_data


class MailingSettingsDeleteView(DeleteView):
    model = MailingSettings
    success_url = reverse_lazy('mailings:list')


class ClientsCreateView(CreateView):
    model = Clients
    fields = ('email', 'fullname', 'comment')
    success_url = reverse_lazy('mailings:list_client')


class ClientsUpdateView(UpdateView):
    model = Clients
    fields = ('email', 'fullname', 'comment')
    success_url = reverse_lazy('mailings:list_client')


class ClientsListView(ListView):
    model = Clients
    extra_context = {
        'title': 'Список клиентов'
    }


class ClientsDetailView(DetailView):
    model = Clients

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(**kwargs)
        mailings_item = Clients.objects.get(pk=self.kwargs.get('pk'))
        context_data['pk'] = mailings_item.pk
        context_data['title'] = 'Клиент:  ' + mailings_item.fullname
        return context_data


class ClientsDeleteView(DeleteView):
    model = Clients
    success_url = reverse_lazy('mailings:list_client')
