from django.shortcuts import render, redirect

from .models import SampleModel
from .models import *

# Create your views here.
def index(request):
    return render(request, "index.html")

def main(request):
    users = Articles.object.all()
    return render(request, '2.html', {'user': users})

# class MyDetailView(DetailView):
#     model = Article
#     template_name = 'detail.html'
#     context_object_name = 'article'

from .forms import *


def index(request):
    if request.method == 'POST':
        form = SampleModelForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('main')

    else:
        form = SampleModelForm()
    return render(request, 'index.html', {'form':form})

def logout(request):
    if request.user.is_authenticated:
        visited_pages = []

        visited_cookies = request.COOKIES.get('visit_count')
        if visited_cookies:
            visited_pages = visited_cookies.split(',')

        for page in visited_pages:
            VisitedPage.objects.create(user=request.user, page_name=page)

        response = redirect('login')
        response.delete_cookie('visited_pages')
        return response
    else:

        return redirect('login')