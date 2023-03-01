from  django.urls import path
from . import  views

from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('', views.inicio, name= 'inicio'),
    path('nosotros', views.nossotros, name='nosotros'),
    path('libros', views.libros, name='libros'),
    path('libros/crear_libros',views.crearLibro, name='crear_libros'),
    path('libros/editar_libro',views.editarLibro, name='editar_libro'),
    path('eliminar_libro/<int:pk>/',views.eliminarLIbro, name='eliminar_libro'),
    path('libros/editar_libro/<int:id>/',views.editarLibro, name='detalle_libros'),

]+ static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)