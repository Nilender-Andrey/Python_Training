from api.models import CategoryResource, CourseResource
from django.urls import path, include
from tastypie.api import Api

# Для POST и DELETE необходимо добавить ключ в заголовок
# key: Authorization
# value: ApiKey admin:1234567890

api = Api(api_name="v1")
api.register(CategoryResource())
api.register(CourseResource())

urlpatterns = [
    path("", include(api.urls), name="index"),

]
