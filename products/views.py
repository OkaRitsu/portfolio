import logging

from django.contrib import messages
from django.urls import reverse_lazy
from django.views import generic

from .forms import ContactForm
from .models import Product

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


class ProductListView(generic.ListView):
    model = Product
    template_name = 'product_list.html'
    paginate_by = 2

    def get_queryset(self):
        products = Product.objects.order_by('-created_at')
        return products
