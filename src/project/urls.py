from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from . import views
from accounts.views import SignUpView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('index.urls', namespace="index")),
    path('accounts/', include('django.contrib.auth.urls')),
    path('profile/', include('accounts.urls')),
    path('accounts/signup/', SignUpView.as_view(), name='signup'),
    path('products/', include('products.urls', namespace="proudcts")),
    path('cart/', include('cart.urls', namespace="cart")),
    path('checkout/', include('checkout.urls', namespace="checkout")),
    path('contact/', include('contact.urls', namespace="contact")),
    path('resume/', include('resume.urls', namespace="resume")),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
