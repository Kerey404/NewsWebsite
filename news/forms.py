from .models import Articles
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea


class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['tittle', 'anons', 'content', 'pub_date']

        widgets = {
            "tittle":TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter Tittle",
            }),
            "anons":TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter Anons",
            }),
            "pub_date":DateTimeInput(attrs={
                "class": "form-control",
                "placeholder": "Enter Pub Date",
            }),
            "content":Textarea(attrs={
                "class": "form-control",
                "placeholder": "Enter Content",
            })
        }