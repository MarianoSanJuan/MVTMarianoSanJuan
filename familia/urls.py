from django.urls import path
from .views import familia, familia_db, familia_dburl, home

urlpatterns = [
    path("", home),
    path("mi-familia", familia),
    path("mi-familiadb", familia_db),
    path("mi-familiadburl/<integrante_nombre>/<integrante_edad>", familia_dburl)
    
]
