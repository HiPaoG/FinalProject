from django.conf.urls import include, url
from . import views

urlpatterns = [

    url(r'^$', views.ListaCita),
    url(r'^cita/(?P<pk>[0-9]+)/$', views.DetalleCita, name='DetalleCita'),
    url(r'^cita/nueva/$', views.NuevaCita, name='NuevaCita'),
    url(r'^cita/(?P<pk>[0-9]+)/editar/$', views.EditarCita, name='EditarCita'),
    url(r'^cita/(?P<pk>[0-9]+)/eliminar/$', views.EliminarCita, name='EliminarCita'),
    url(r'^pacientes/', views.ListaPaciente, name='ListaPaciente'),
    url(r'^paciente/(?P<pk>[0-9]+)/$', views.DetallePaciente, name='DetallePaciente'),
    url(r'^paciente/nuevo/$', views.NuevoPaciente, name='NuevoPaciente'),
    url(r'^paciente/(?P<pk>[0-9]+)/editar/$', views.EditarPaciente, name='EditarPaciente'),
    url(r'^paciente/(?P<pk>[0-9]+)/eliminar/$', views.EliminarPaciente, name='EliminarPaciente'),
    url(r'^medicos/', views.ListaMedico, name='ListaMedico'),
    url(r'^medico/(?P<pk>[0-9]+)/$', views.DetalleMedico, name='DetalleMedico'),
    url(r'^medico/nuevo/$', views.NuevoMedico, name='NuevoMedico'),
    url(r'^medico/(?P<pk>[0-9]+)/editar/$', views.EditarMedico, name='EditarMedico'),
    url(r'^medico/(?P<pk>[0-9]+)/eliminar/$', views.EliminarMedico, name='EliminarMedico'),
    #url(r'^accounts/login/$', django.contrib.auth.views.login, name'login'),
    #url(r'^accounts/logout/$', views.logout, name='logout', kwargs={'next_page':'/'}),

]
