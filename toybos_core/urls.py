from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from toybos.views import HomeView, ProductList
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', HomeView.as_view(), name='home-url'),
    path('product-list/', ProductList.as_view(), name='product-list-url')
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)