from django.views import generic

from .forms import ContactForm

class IndexView(generic.TemplateView):
    template_name = 'index.html'

class ContactView(generic.FormView):
    template_name = 'contact.html'
    form_class = ContactForm
