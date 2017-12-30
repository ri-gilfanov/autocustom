from django.views.generic.base import ContextMixin
from .models import Category


class StoreMenuMixin(ContextMixin):

    def get_context_data(self, **kwargs):
        context = super(StoreMenuMixin, self).get_context_data(**kwargs)
        context['category_tree'] = Category.objects.filter(parent=None).get_descendants(include_self=True)
        return context
