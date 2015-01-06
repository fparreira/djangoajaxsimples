from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'DjangoAjax.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'DjangoAjax.core.views.home', name='home'),
    url(r'^hello/$', 'DjangoAjax.core.views.hello', name='hello'),
    url(r'^mensagem/$', 'DjangoAjax.core.views.mensagem', name='mensagem'),

    url(r'^admin/', include(admin.site.urls)),
)
