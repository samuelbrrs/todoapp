from django.shortcuts import render
from django.contrib import messages

from .forms import CategoryForm, TaskForm
from .forms import CategoryForm, TaskForm
from .models import Category, Task
from .models import Category, Task

# Create your views here.

def add_category(request):
    template_name = 'tasks/add_category.html'
    context = {}
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.owner = request.user
            f.save()
            messages.succes(request, 'Categoria adicionada com sucesso')
    form = CategoryForm()
    context['form'] = form
    return render(request, template_name, context)

def list_categories(request):
    template_name = 'tasks/list_categories.html'
    categories = Category.objects.filter(owner=request.user)
    context = {
        'categories': categories
    }
    return render(request, template_name, context)


