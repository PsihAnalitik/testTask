from .models import Comment
from django.forms import ModelForm, TextInput

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['name']
        widgets = {'name': TextInput(attrs = {'class': 'form-control', 
                                              'name': 'comment',
                                              'id': 'comment',
                                              'placeholder': "Введите отзыв"
                                              })}