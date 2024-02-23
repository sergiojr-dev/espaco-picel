from django.shortcuts import HttpResponseRedirect
from apps.comentario.forms import ComentarioForms
from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from apps.galeria.models import Fotografia
from apps.galeria.forms import FotografiaForms

def criar_comentario(request, foto_id):
    fotografia = Fotografia.objects.get(id=foto_id)
    if request.method == "POST":
        form = ComentarioForms(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.post1 = fotografia
            comentario.usuario = request.user
            comentario.save()
            messages.success(request, "Comentado com sucesso")
            return redirect("imagem", foto_id=foto_id)
    else:
        form = ComentarioForms()
        form.fields['usuario'].queryset = User.objects.filter(pk=request.user.pk)
        
    return render(request, "comentario/criar_comentario.html", {'form': form, 'foto_id': foto_id})






