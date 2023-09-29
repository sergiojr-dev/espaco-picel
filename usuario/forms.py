from django import forms


 
class CadastroForms(forms.Form):
    nome_cadastro=forms.CharField(
        label='Nome de Cadastro', 
        required=True, 
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ex.: Miguel Nicolelis',
            }
        )
    )

    email=forms.EmailField(
        label='Email',
        required=True,
        max_length=100,
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ex.: ciencia_sem_fim@xpto.com',
            }
        )
    )

    senha_1=forms.CharField(
        label='Senha', 
        required=True, 
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Digite sua senha',
            }
        ),
    )

    senha_2=forms.CharField(
            label='Confirmar Senha', 
            required=True, 
            max_length=70,
            widget=forms.PasswordInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Digite novamente',
                }
            ),
        )
    
    def clean_nome_cadastro(self):
        nome = self.cleaned_data.get('nome_cadastro')
        
        if nome:
            nome = nome.strip() # serve para remover espaços em branco (ou outros caracteres especificados) do início e do fim de uma string
            if ' ' in nome:
                    raise forms.ValidationError('Espaços não são permitidos nesse campo')
            else:
                    return nome      

class LoginForms(forms.Form):
    nome_login=forms.CharField(
        label='Nome de Login', 
        required=True, 
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ex.: Sergio Sacani',
            }
        )
    )
    senha=forms.CharField(
        label='Senha', 
        required=True, 
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Digite a sua senha',
            }
        ),
    )




    

