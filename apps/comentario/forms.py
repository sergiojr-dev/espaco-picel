from django import forms
from apps.comentario.models import Comentario

class ComentarioForms(forms.ModelForm):
    class Meta :
        model = Comentario
        fields = ['comment', 'usuario',]
        labels = {
            'usuario' : 'Nome',
            'comment' : 'Comentario',
        }

        widgets = {
        'comment':  forms.Textarea(attrs={'class':'form-control'}),
        'usuario': forms.Select(attrs={"class": "form-control"}),
        'data_comentario': forms.DateInput(  # para formularios do tipo data
                format = '%d/%m/%Y',
                attrs={
                    'type':'date',
                    'class':'form-control'
                }
            ),
        }
        
