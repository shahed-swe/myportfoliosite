from django import forms
from .models import BlogPost

class BlogPostForm(forms.Form):
    slug = forms.SlugField()
    title = forms.CharField()
    content = forms.CharField(widget=forms.Textarea)
    about = forms.CharField()
    time = forms.TimeField()
    date = forms.DateField(widget=forms.SelectDateWidget)
    select = forms.CharField(max_length=256, widget=forms.Select(choices=[('Model Feed', 'Model Feed'),('News Feed', 'News Feed'),('Other Feed','Other Feed')]))

class BlogPostModelForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['slug','title','content','about','time','date','select']

    
    def clean_title(self, *args, **kwargs):
        instance = self.instance
        title = self.cleaned_data.get('title')
        qs = BlogPost.objects.filter(title__iexact=title)
        if instance is not None:
            qs = qs.exclude(pk=instance.pk)
        if qs.exists():
            raise forms.ValidationError("Title is already exists in the database")
        return title
    
    