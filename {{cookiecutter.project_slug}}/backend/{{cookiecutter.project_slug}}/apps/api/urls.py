from rest_framework import routers
from {{ cookiecutter.project_name }}.apps.default.api.views import UserViewSet

router = routers.SimpleRouter()

router.register(r'users', UserViewSet)

urlpatterns = router.urls
