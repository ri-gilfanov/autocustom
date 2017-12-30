from django.conf.urls import url
from .views import (
    CategoryPage,
)


urlpatterns = [
    url(
        r'^categories/$',
        CategoryPage.as_view(),
        name='store__category__0',
    ),
    url(
        r'^categories/(?P<slug_4>[\w-]+)/(?P<slug_3>[\w-]+)/(?P<slug_2>[\w-]+)/(?P<slug_1>[\w-]+)/$',
        CategoryPage.as_view(),
        name='store__category__4',
    ),
    url(
        r'^categories/(?P<slug_3>[\w-]+)/(?P<slug_2>[\w-]+)/(?P<slug_1>[\w-]+)/$',
        CategoryPage.as_view(),
        name='store__category__3',
    ),
    url(
        r'^categories/(?P<slug_2>[\w-]+)/(?P<slug_1>[\w-]+)/$',
        CategoryPage.as_view(),
        name='store__category__2',
    ),
    url(
        r'^categories/(?P<slug_1>[\w-]+)/$',
        CategoryPage.as_view(),
        name='store__category__1',
    ),
    url(
        r'^products/(?P<slug>[\w-]+)/$',
        CategoryPage.as_view(),
        name='store__product',
    ),
]
