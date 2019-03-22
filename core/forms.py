from django import forms

class CommentForm(forms.Form):
    user_comment = forms.CharField(max_length=200)
