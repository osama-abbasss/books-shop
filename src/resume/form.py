from django import forms
from .models import Comment

class CommentForm(forms.Form):

    class Meta:
        models = Comment
        fields = ['comment','name','email',]
