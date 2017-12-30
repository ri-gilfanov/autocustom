from django.views.generic.base import TemplateView, View, TemplateResponseMixin
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .views_mixins import StoreMenuMixin
from .models import Category, Product
from django.template.response import TemplateResponse

class CategoryPage(View, StoreMenuMixin, TemplateResponseMixin):
    category_template = 'store/category.html'
    products_template = 'store/products.html'
    category = None
    categories = None
    products = None

    def dispatch(self, request, *args, **kwargs):
        # определение и попытка вызова метода GET или POST
        handler = super(CategoryPage, self).dispatch(request, *args, **kwargs)
        return handler

    def get(self, request, *args, **kwargs):
        self.get_category()
        self.get_products()
        context = self.get_context_data(**kwargs)
        response = self.render_to_response(context)
        return response

    def get_category(self):
        queryset = Category.objects.filter()
        slug_4 = self.kwargs.get('slug_4')
        slug_3 = self.kwargs.get('slug_3')
        slug_2 = self.kwargs.get('slug_2')
        slug_1 = self.kwargs.get('slug_1')

        if slug_4:
            queryset = queryset.filter(parent__parent__parent__slug=slug_4)
        if slug_3:
            queryset = queryset.filter(parent__parent__slug=slug_3)
        if slug_2:
            queryset = queryset.filter(parent__slug=slug_2)
        if slug_1:
            queryset = queryset.filter(slug=slug_1)
            try:
                self.category = queryset.get()
            except queryset.model.DoesNotExist:
                raise Http404('Категория не найдена')

    def get_products(self):
        if self.category:
            queryset = Product.objects.filter(category__in=self.category.get_descendants(include_self=True))
            # тут добавить фильтрацию по аргументам из GET-запроса
        else:
            queryset = Product.objects.filter()
        queryset = queryset.prefetch_related(
            'category',
            'category__parent',
            'category__parent__parent',
            'category__parent__parent__parent',
        )
        self.products = queryset

    def get_context_data(self, **kwargs):
        context = super(CategoryPage, self).get_context_data(**kwargs)
        context['category'] = self.category
        if self.category:
            self.categories = self.category.get_children()
        else:
            self.categories = Category.objects.filter(parent=None)
        context['categories'] = self.categories
        context['products'] = self.products
        return context

    def render_to_response(self, context, **response_kwargs):
        response_kwargs.setdefault('content_type', self.content_type)
        if self.categories:
            template = self.category_template
        else:
            template = self.products_template
        return TemplateResponse(request=self.request, template=template, context=context, using=self.template_engine,
                                   **response_kwargs)
