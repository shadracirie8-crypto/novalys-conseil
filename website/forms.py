
from django import forms
from .models import ContactMessage


class ContactMessageForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ["nom", "email", "telephone", "sujet", "message"]

        widgets = {
            "nom": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Votre nom complet",
            }),
            "email": forms.EmailInput(attrs={
                "class": "form-control",
                "placeholder": "exemple@email.com",
            }),
            "telephone": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Votre numéro de téléphone",
            }),
            "sujet": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Objet de votre demande",
            }),
            "message": forms.Textarea(attrs={
                "class": "form-control",
                "placeholder": "Décrivez votre projet...",
                "rows": 5,
            }),
        }

    def clean_nom(self):
        nom = self.cleaned_data["nom"].strip()

        if len(nom) < 2:
            raise forms.ValidationError(
                "Votre nom doit contenir au moins 2 caractères."
            )

        return nom

    def clean_message(self):
        message = self.cleaned_data["message"].strip()

        if len(message) < 10:
            raise forms.ValidationError(
                "Votre message doit contenir au moins 10 caractères."
            )

        return message
