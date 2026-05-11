from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    """form for our comment model """
    class Meta:
        model = Comment # to which the form is related
        exclude = ["post"] # all fields except post field - this should be the post under which the form appears
        labels = { #not the default inferred fields
            "user_name":"Your name",
            "user_email": "Your Email",
            "text": "Your Thoughts"
        }