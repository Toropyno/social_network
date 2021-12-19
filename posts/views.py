from django.shortcuts import render, redirect
from django.views import View

from posts.forms import PostForm, CommentForm
from posts.models import Post


class PostCommentCreateView(View):

    def post(self, request):
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

        return redirect(request.META['HTTP_REFERER'])
