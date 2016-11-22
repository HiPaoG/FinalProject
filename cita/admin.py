from django.contrib import admin
from cita.models import Paciente, PacienteAdmin, Medico, MedicoAdmin

admin.site.register(Paciente, PacienteAdmin)
admin.site.register(Medico, MedicoAdmin)
