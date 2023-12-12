from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Nome de usuário"}
        )
        self.fields["password"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Senha"}
        )


class RegistrarForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Nome de usuário"}
        )
        self.fields["password1"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Senha"}
        )
        self.fields["password2"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Confirme sua senha"}
        )
