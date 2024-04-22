from django.forms import ModelForm
from django import forms
from articleapp.models import Article
from projectapp.models import Project


class ArticleCreationForm(ModelForm):

    content = forms.CharField(widget=forms.Textarea(attrs={'class': 'editable text-left',
                                                           'style': 'height: auto;'}))
    project = forms.ModelChoiceField(queryset=Project.objects.all(), required=False)
    class Meta:
        model = Article
        fields = ['title', 'image', 'project', 'content'] # writer은 서버내에서 지정해줄것 이기때문에 생략


