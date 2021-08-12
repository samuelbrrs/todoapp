from django.shortcuts import render

from .forms import CategoryForm, TaskForm

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
    form = CategoryForm()
    context['form'] = form
    return render(request, template_name, context)