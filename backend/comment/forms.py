from django import forms
from comment.models import Comment


class CommentCreateForm(forms.FormModel):
    class Meta:
        model = Comment
        fields = ['user', 'video', 'updated']

class CommentUpdateForm(forms.FormModel):
    class Meta:
        model = Comment
        fields = ['user', 'video', 'created']

