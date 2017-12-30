from django.conf.urls import url
from .views import (
    ServicePage,
)


urlpatterns = [
    url(
        r'^services/(?P<slug>[\w-]+)/$',
        ServicePage.as_view(),
        name='services__service',
    ),
]
