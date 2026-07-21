from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from cafes import views

    # Create an instance of the SIMPLE router.
router = DefaultRouter()
    
    # Register our CafeViewSet with the router.
    # This tells the router: "Create URLs for the CafeViewSet,
    # and use 'cafes' as the URL prefix."
router.register(r'cafes', views.CafeViewSet, basename="cafe")
router.register(r'barrios', views.BarrioViewSet, basename="barrio")
router.register(r'reviewers', views.ReviewerViewSet, basename="reviewer")



urlpatterns = [
    path('admin/', admin.site.urls),
        # This one line includes all the URLs the router generated for us.
    path('api/', include(router.urls))
]

