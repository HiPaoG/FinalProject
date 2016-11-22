from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .forms import CitaForm, PacienteForm, MedicoForm
from citas.models import Medico, Paciente, Cita

#Cita

def ListaCita(request):
    citas = Cita.objects.all
    return render(request, 'cita/ListaCita.html', {'citas':citas})

def DetalleCita(request, pk):
    citas = get_object_or_404(Cita, pk=pk)
    return render(request, 'cita/DetalleCita.html', {'citas':citas})

def NuevaCita(request):
    if request.method == "POST":
        formulario = CitaForm(request.POST)
        if formulario.is_valid():
            cita = formulario.save(commit=False)
            for medico_id in request.POST.getlist('medico'):
                for paciente_id in request.POST.getlist('paciente'):
                    cita = Cita(medico_id=medico_id,
                    paciente_id=paciente_id,
                    fecha=formulario.cleaned_data['fecha'],
                    hora=formulario.cleaned_data['hora'],
                    observaciones=formulario.cleaned_data['observaciones'])
                    cita.save()
                    messages.add_message(request, messages.SUCCESS, 'Datos guardados')
    else:
        formulario = CitaForm()
    return render(request, 'cita/NuevaCita.html', {'formulario':formulario})

def EditarCita(request, pk):
    cita = get_object_or_404(Cita, pk=pk)
    if request.method == "POST":
        formulario = CitaForm(request.POST, instance=cita)
        if formulario.is_valid():
            cita = formulario.save(commit=False)
            for medico_id in request.POST.getlist('medico'):
                for paciente_id in request.POST.getlist('paciente'):
                    cita = Cita(medico_id=medico_id,
                    paciente_id=paciente_id,
                    fecha=formulario.cleaned_data['fecha'],
                    hora=formulario.cleaned_data['hora'],
                    observaciones=formulario.cleaned_data['observaciones'])
                    cita.save()
                    messages.add_message(request, messages.SUCCESS, 'Datos guardados')
    else:
        formulario = CitaForm(instance=cita)
    return render(request, 'cita/EditarCita.html', {'formulario':formulario})

    def EliminarCita(request, pk):
        cita = get_object_or_404(Cita, pk=pk)
        cita.delete()
        return redirect('ListaCita')

#Paciente

def ListaPaciente(request):
    pacientes = Paciente.objects.all
    return render(request, 'paciente/ListaPaciente.html', {'pacientes':pacientes})

def DetallePaciente(request, pk):
    pacientes = get_object_or_404(Paciente, pk=pk)
    return render(request, 'paciente/DetallePaciente.html', {'pacientes':pacientes})

def NuevoPaciente(request):
    if request.method == "POST":
        formulario = PacienteForm(request.POST)
        if formulario.is_valid():
            paciente = formulario.save(commit=False)
            paciente = Paciente(nombre=formulario.cleaned_data['nombre'],
            apellido=formulario.cleaned_data['apellido'],
            edad=fomulario.cleaned_data['edad'],
            sexo=formulario.cleaned_data['sexo'])
            paciente.save()
            messages.add_message(request, messages.SUCCESS, 'Datos guardados')
    else:
        formulario = PacienteForm()
    return render(request, 'paciente/NuevoPaciente.html', {'formulario':formulario})

def EditarPaciente(request, pk):
    paciente = get_object_or_404(Paciente, pk=pk)
    if request.method == "POST":
        formulario = PacienteForm(request.POST, instance=paciente)
        if formulario.is_valid():
            paciente = formulario.save(commit=False)
            paciente = Paciente(nombre=formulario.cleaned_data['nombre'],
            apellido=formulario.cleaned_data['apellido'],
            edad=fomulario.cleaned_data['edad'],
            sexo=formulario.cleaned_data['sexo'])
            paciente.save()
            messages.add_message(request, messages.SUCCESS, 'Datos guardados')
    else:
        formulario = PacienteForm(instance=paciente)
    return render(request, 'paciente/EditarPaciente.html', {'formulario':formulario})

    def EliminarPaciente(request, pk):
        paciente = get_object_or_404(Paciente, pk=pk)
        paciente.delete()
        return redirect('ListaPaciente')

#Medico

def ListaMedico(request):
    medicos = Medico.objects.all
    return render(request, 'medico/ListaMedico.html', {'medicos':medicos})

def DetalleMedico(request, pk):
    medicos = get_object_or_404(Medico, pk=pk)
    return render(request, 'medico/DetalleMedico.html', {'medicos':medicos})

def NuevoMedico(request):
    if request.method == "POST":
        formulario = MedicoForm(request.POST)
        if formulario.is_valid():
            medico = formulario.save(commit=False)
            medico = Medico(nombre=formulario.cleaned_data['nombre'],
            apellido=formulario.cleaned_data['apellido'],
            especialidad=fomulario.cleaned_data['especialidad'],
            telefono=formulario.cleaned_data['telefono'],
            fecha_nacimiento=formulario.cleaned_data['fecha_nacimiento'])
            medico.save()
            messages.add_message(request, messages.SUCCESS, 'Datos guardados')
    else:
        formulario = MedicoForm()
    return render(request, 'medico/NuevoMedico.html', {'formulario':formulario})

def EditarMedico(request, pk):
    medico = get_object_or_404(Paciente, pk=pk)
    if request.method == "POST":
        formulario = medicoForm(request.POST, instance=medico)
        if formulario.is_valid():
            medico = formulario.save(commit=False)
            medico = Medico(nombre=formulario.cleaned_data['nombre'],
            apellido=formulario.cleaned_data['apellido'],
            especialidad=fomulario.cleaned_data['especialidad'],
            telefono=formulario.cleaned_data['telefono'],
            fecha_nacimiento=formulario.cleaned_data['fecha_nacimiento'])
            medico.save()
            messages.add_message(request, messages.SUCCESS, 'Datos guardados')
    else:
        formulario = MedicoForm(instance=medico)
    return render(request, 'medico/EditarMedico.html', {'formulario':formulario})

    def EliminarMedico(request, pk):
        medico = get_object_or_404(Medico, pk=pk)
        medico.delete()
        return redirect('ListaMedico')
