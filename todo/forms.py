from django import forms

from todo.models import TodoModel


class TodoCreateForm(forms.ModelForm):

    class Meta:
        model = TodoModel
        fields = ('todoTitle','todoDescription')

        widgets = {
            'todoTitle':forms.TextInput(attrs={'placeholder':"Todo Title"}),
            'todoDescription':forms.Textarea(attrs={"placeholder":'Tod Description'})
        }
