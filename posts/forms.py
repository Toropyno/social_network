from django.forms import ModelForm

from posts.models import Post, Comment


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['post', 'author', 'text', 'photo']
