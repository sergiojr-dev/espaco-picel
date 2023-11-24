from typing import Any
from django import forms
from apps.galeria.models import Fotografia

class FotografiaForms(forms.ModelForm): # porque é form que esta tendo um modelo para ser criada no caso Models de fotografia
    class Meta :                   #  essa classe refere-se aos metadados da classe. Metadados são dados que fazem referência à própria natureza daquela classe
        model = Fotografia        # conexão com model
        exclude = ['publicada',] # o que não quero de Model
        labels = {
            'descricao':'Descrição',
            'data_fotografia': 'Data de registro',
            'usuario': 'Usuário',
            'nome' : 'Título'

        }

        widgets = {         # os atributos que quero de fotografia
            'nome': forms.TextInput(attrs={'class':'form-control'}),
            'legenda': forms.TextInput(attrs={'class': 'form-control'}) ,
            'categoria': forms.Select(attrs={'class':'form-control'}), # forms.Selcet criar elementos de seleção (ou caixa de seleção) em um formulário HTML.
            'descricao': forms.Textarea(attrs={'class':'form-control'}), #forms.Textarea criar campos de texto multi-linha em formulários HTML
            'foto': forms.FileInput(attrs={'class':'form-control'}), #  forms.FileInput  criar campos de upload de arquivo em formulários HTML
            'data_fotografia': forms.DateInput(  # para formularios do tipo data
                format = '%d/%m/%Y',
                attrs={
                    'type':'date',
                    'class':'form-control'
                }
            ),
            'usuario': forms.Select(attrs={'class':'form-control'}), 
        }



    
