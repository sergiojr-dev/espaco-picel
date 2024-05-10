from typing import Any
from django import forms
from django.contrib.auth.models import User


 
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
        email = self.cleaned_data.get('email')

        if User.objects.filter(username=nome).exists() or User.objects.filter(email=email).exists():
             raise forms.ValidationError('Este usuário ou email já existem')
        
        else:
            nome = nome.strip()
            if ' ' in nome:
                raise forms.ValidationError('Espaços não são permitidos neste campo')
            else:
                return nome   
            
    def clean_senha_2 (self):
        senha_1 = self.cleaned_data.get('senha_1')
        senha_2 = self.cleaned_data.get('senha_2')

        if senha_1 and senha_2:
            if senha_1 != senha_2:
                raise forms.ValidationError('Senhas não são iguais')
            else:
                return senha_2
            

        
    

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




    

class EditarUsuarioForms(forms.ModelForm):
    password = forms.CharField(
        label='Senha',
        required=False,
        max_length=70,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Digite sua senha'}),
    )

    nova_senha = forms.CharField(
        label='Nova Senha',
        required=False,
        max_length=70,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Digite a nova senha'}),
    )

    confirmar_nova_senha = forms.CharField(
        label='Confirmar Nova Senha',
        required=False,
        max_length=70,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Digite novamente a nova senha'}),
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    def clean_username(self):
        nome = self.cleaned_data.get('username')
        email = self.cleaned_data.get('email')

        if User.objects.filter(username=nome).exists() and User.objects.get(username=nome).id != self.instance.id:
            raise forms.ValidationError('Este usuário já existe')

        if 'email' in self.changed_data:
            if User.objects.filter(email=email).exists() and User.objects.get(email=email).id != self.instance.id:
                raise forms.ValidationError('Este email já está em uso')

        nome = nome.strip()
        if ' ' in nome:
            raise forms.ValidationError('Espaços não são permitidos neste campo')
        return nome

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        nova_senha = cleaned_data.get('nova_senha')
        confirmar_nova_senha = cleaned_data.get('confirmar_nova_senha')

        if password and not self.instance.check_password(password):
            self.add_error('password', 'Senha atual incorreta')

        if nova_senha and nova_senha != confirmar_nova_senha:
            self.add_error('confirmar_nova_senha', 'As senhas não coincidem')

        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        nova_senha = self.cleaned_data.get('nova_senha')

        if nova_senha:
            user.set_password(nova_senha)

        if commit:
            user.save()
        return user
