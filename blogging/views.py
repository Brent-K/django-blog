from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, redirect
from django import forms
from django.template import loader
from blogging.models import Post
from blogging.forms import MyCommentForm
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.utils import timezone


def add_model(request):
    if request.method == "POST":
        form = MyCommentForm(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.timestamp = timezone.now()
            model_instance.save()
            return redirect("/")
    else:
        form = MyCommentForm()
        return render(request, "add.html", {"form": form})


class PubPostListView(ListView):
    pub_posts = "blog_index"
    queryset = Post.objects.exclude(published_date__exact=None).order_by(
        "-published_date"
    )
    template_name = "blogging/list.html"


class PostDetailView(DetailView):
    detail_posts = "blog_detail"
    queryset = Post.objects.exclude(published_date__exact=None)
    template_name = "blogging/detail.html"


def stub_view(requests, *args, **kwargs):
    body = "Stub View\n\n"
    if args:
        body += "Args:\n"
        body += "\n".join(["\t%s" % a for a in args])
    if kwargs:
        body += "Kwargs:\n"
        body += "\n".join(["\t%s: %s" % i for i in kwargs.items()])
    return HttpResponse(body, content_type="text/plain")
