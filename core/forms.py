from django import forms

class CommentForm(forms.Form):
    user_comment = forms.TextField(max_length=2000)
