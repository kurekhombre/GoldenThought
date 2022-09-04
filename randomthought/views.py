from django.shortcuts import render, redirect, get_object_or_404
from randomthought.models import RandomThought
from randomthought.forms import RandomThoughtForm, RandomThoughtFormDjango

import requests


# Create your views here.

def random_thought(request):
    thought = RandomThought.objects.order_by('?').first()
    return render(
        request,
        'randomthought/thought.html',
        context={
            'thought': thought
        }
    )


# Formularz django
def create_thought_django(request):

    if request.method == "POST":
        form = RandomThoughtFormDjango(request.POST)  # bound form

        if form.is_valid():
            data = form.cleaned_data

            RandomThought.objects.create(
                thought=data.get('thought'),
                author=data.get('author'),
            )

        return redirect('thought:thought-view')

    form = RandomThoughtFormDjango()  # unbound form

    return render(
        request,
        'randomthought/create_thought_django.html',
        context={
            'form': form
        }
    )


# Formularz modelu
def create_thought(request):

    if request.method == "POST":
        form = RandomThoughtForm(request.POST)

        if form.is_valid():
            form.save()

        return redirect('thought:thought-view')

    form = RandomThoughtForm()
    return render(
        request,
        'randomthought/create_thought.html',
        context={
            'form': form
        }
    )


def api(request):

    url = "https://quotes15.p.rapidapi.com/quotes/random/"
    headers = {
        "X-RapidAPI-Host": "quotes15.p.rapidapi.com",
        "X-RapidAPI-Key": "afe03997c9msh9b6b7f3c3e0a257p123913jsnba78a630c191"
    }
    response = requests.request("GET", url, headers=headers)

    randomthought = response.json()

    content = randomthought.get('content')

    try:
        originator = randomthought.get('originator')
        originator_name = originator.get('name')
        originator_url = originator.get('url')
    except:
        return render(
            request,
            'randomthought/api.html'
        )

    return render(
        request,
        'randomthought/api.html',
        context={
            'content': content,
            'originator_name': originator_name,
            'originator_url': originator_url,

        }
    )


def view_thoughts(request):
    thoughts = RandomThought.objects.all()
    return render(
        request,
        'randomthought/view_thoughts.html',
        context={
            'thoughts': thoughts
        }
    )


def detail_thought(request, pk):
    thought = get_object_or_404(RandomThought, pk=pk)
    return render(
        request,
        'randomthought/detail_thought.html',
        context={
            'thought': thought
        }
    )


def update_thought(request,pk):
    thought = get_object_or_404(RandomThought, pk=pk)

    if request.method == "POST":
        form = RandomThoughtForm(request.POST, instance=thought)

        if form.is_valid():
            form.save()
            return redirect('thought:view-thoughts')
    else:
        form = RandomThoughtForm(instance=thought)

    return render(
        request,
        'randomthought/create_thought.html',
        context={
            'form': form,
            'thought': thought
        }
    )


def delete_thought(request,pk):
    thought = get_object_or_404(RandomThought, pk=pk)

    if request.method == "POST":
        thought.delete()
        return redirect('thought:view-thoughts')

    return render(
        request,
        'randomthought/thought_confirm_delete.html',
        context={
            'thought': thought
        }
    )