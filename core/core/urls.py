from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf import settings
from django.conf.urls.static import static


schema_view = get_schema_view(
    openapi.Info(
        title="Shop API",
        default_version="v1",
        description="The schema view for API",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="cactusinjast@gmail.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/products/", include('products.urls')),
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path(
        "redoc/",
        schema_view.with_ui("redoc", cache_timeout=0),
        name="schema-redoc",
    ),
    path(
        "slider/", include("slider.urls")
    ),
    path('auth/', include('account.urls')),
    path('comments/', include('comment.urls')),
    path('cart/', include('cart.urls')),
    path('order/', include('order.urls')),
    path('summernote/', include('django_summernote.urls')),
    path('blog/', include('blog.urls')),
]

if settings.DEBUG:
    urlpatterns = urlpatterns + \
        static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
