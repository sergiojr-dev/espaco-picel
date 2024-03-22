from django.shortcuts import HttpResponseRedirect
from apps.comentario.forms import ComentarioForms
from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from apps.galeria.models import Fotografia
from apps.comentario.models import Comentario

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




def lista_comentarios(request, foto_id):
    fotografia = Fotografia.objects.get(id=foto_id)  # Obtenha a fotografia com o ID fornecido
    return render(request, 'comentario/lista_comentarios.html', {'fotografia': fotografia})


from django.shortcuts import get_object_or_404

def editar_comentario(request, comentario_id):
    comentario = Comentario.objects.get(id=comentario_id)
    form = ComentarioForms(instance=comentario)

    if request.method == 'POST':
        form = ComentarioForms(request.POST, instance=comentario)
        if form.is_valid():
            form.save()
            messages.success(request, 'Comentário editado com sucesso')
            return redirect('lista_comentarios', foto_id=comentario.post1.id)
    return render(request, 'comentario/editar_comentario.html', {'form': form, 'comentario_id': comentario_id})

def deletar_comentario(request, comentario_id):
    comentario = Comentario.objects.get(id=comentario_id)
    fotografia_id = comentario.post1_id
    comentario.delete()
    messages.success(request, 'Comentário deletado!')
    return redirect('lista_comentarios', foto_id=fotografia_id)

