"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
# import debug_toolbar

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('accounts.urls', namespace='accounts')),
    path('', include('address.urls', namespace='address')),
    path('', include('blog.urls', namespace='blog')),
    path('', include('contactus.urls', namespace='contactus')),
    path('', include('coupon.urls', namespace='coupon')),
    path('', include('orders.urls', namespace='orders')),
    path('', include('payments.urls', namespace='payments')),
    path('', include('products.urls', namespace='products')),
    path('', include('refound.urls', namespace='refounds')),
    path('', include('search.urls', namespace='search')),

    # path('__debug__/', include(debug_toolbar.urls)),


]  # + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    # urlpatterns += [path('__debug__/', include(debug_toolbar.urls))]

    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
