from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from toybos.views import HomeView, ProductListView, ProductDetailView, PublicationListView, PublicationDetailView, RecipesListView, RecipesDetailView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', HomeView.as_view(), name='home-url'),
    path('products/', ProductListView.as_view(), name='products-url'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail-url'),
    path('publications/', PublicationListView.as_view(), name='publications-url'),
    path('publications/<int:pk>/', PublicationDetailView.as_view(), name='publication-detail-url'),
    path('recipes/', RecipesListView.as_view(), name='recipes-url'),
    path('recipes/1/', RecipesDetailView.as_view(), name='recipes-detail-url'),
    ]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)