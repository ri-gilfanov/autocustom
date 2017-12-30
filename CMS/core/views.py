from django.shortcuts import render
from django.views.generic.base import ContextMixin, View, TemplateResponseMixin, TemplateView
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from store.views_mixins import StoreMenuMixin


def main_page(request):
    context = {}
    context['page_header'] = 'Главная страница'
    return render(request, 'core/main_page.html', {})


@method_decorator(csrf_exempt, name='dispatch')
class MainPage(StoreMenuMixin, TemplateView):
    template_name = 'core/main_page.html'

    def get_context_data(self, **kwargs):
        context = super(MainPage, self).get_context_data(**kwargs)
        return context
