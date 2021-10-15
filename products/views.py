import logging

from django.contrib import messages
from django.urls import reverse_lazy
from django.views import generic

from .forms import ContactForm

logger = logging.getLogger(__name__)


class IndexView(generic.TemplateView):
    template_name = 'index.html'


class ContactView(generic.FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('products:contact')

    def form_valid(self, form):
        form.send_email()
        messages.success(self.request, 'メッセージを送信しました．')
        logger.info('Contact sent by {}'.format(form.cleaned_data['name']))
        return super().form_invalid(form)
