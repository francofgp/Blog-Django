from django import forms
from blog.models import Post, Comment

""" 
class PostForm(forms.ModelForm):

    class Meta():
        model = Post
        fields = ('author', 'title', 'text')

        # widgets para que tengan mas estilos
        # conectar widget con estilos de CSS

        widgets = {
            # para relacionarlo con una clase en CSS, que va a estar en
            # nuestro CSS.css
            'title': forms.TextInput(attrs={'class': 'textinputclass'}),
            'text': forms.Textarea(attrs={'class':
                                          'editable medium-editor-textarea postcontent'})
        } """


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('author', 'title', 'text',)

        widgets = {
            'title': forms.TextInput(attrs={'class': 'textinputclass'}),
            'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea postcontent'}),
        }


class CommentForm(forms.ModelForm):

    class Meta():
        model = Comment
        fields = ('author', 'text')

        widgets = {
            # para relacionarlo con una clase en CSS
            'author': forms.TextInput(attrs={'class': 'textinputclass'}),
            'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea'})
        }
