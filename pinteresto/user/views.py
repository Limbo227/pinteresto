from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views.generic import CreateView
from .models import News
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
# Create your views here.


def author(request, user_id):
    all_news = News.objects.filter(author=user_id)
    author_name = User.objects.get(pk=user_id)
    # return HttpResponse(author_name)
    return render(request, 'user/author.html', {'all_news': all_news, 'author_name': author_name})


def post(request):
    return render(request, 'user/post.html')


# def create_post(request):
#     return render(request, 'user/create_post.html', )

# class AddPostView(CreateView):
#     model = News
#     template_name = 'user/create_post.html'
#     # form_class =
#     fields = '__all__'


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()

    context = {'form': form}
    return render(request, 'registration/register.html', context)


@login_required()
def delety(request, pk):
    post = News.objects.get(id=pk)

    if post.author == request.user:
        post.delete()
        return redirect('/')
    else:
        return HttpResponse('<h1>Пошел нахуй Эрлан</h1>')
