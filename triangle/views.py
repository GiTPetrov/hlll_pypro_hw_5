from django.shortcuts import get_object_or_404, redirect, render

from triangle.forms import PersonForm, TriangleForm
from triangle.models import Person


def index(request):
    return render(request, 'triangle/index.html', {})


def trngl_form(request):
    hypo = None
    if 'calculate' in request.GET:
        form = TriangleForm(request.GET)
        if form.is_valid():
            leg_one = form.cleaned_data["leg_one"]
            leg_two = form.cleaned_data["leg_two"]
            hypo = (leg_one ** 2 + leg_two ** 2) ** 0.5
    else:
        form = TriangleForm()
    return render(
        request,
        'triangle/triangle_form.html',
        {
            'get_trngl_form': form,
            'hypothesis': hypo,
        }
    )


def person_form(request):
    if request.method == 'POST':
        pers_form = PersonForm(request.POST)
        if pers_form.is_valid():
            pers_form.save()
            return redirect('triangle:person-list')
    else:
        pers_form = PersonForm()
    return render(
        request,
        'triangle/person.html',
        {
            'formset': pers_form
        }
    )


def person_update_form(request, pk):
    person = get_object_or_404(Person, pk=pk)
    if request.method == 'POST':
        pers_form = PersonForm(request.POST, instance=person)
        if pers_form.is_valid():
            pers_form.save()
            return redirect('triangle:person-list')
    else:
        pers_form = PersonForm(instance=person)
    return render(
        request,
        "triangle/person_update.html",
        {
            'formset': pers_form,
            'person': person
        }
    )


def person_list(request):
    person_queryset = Person.objects.all()
    return render(request, 'triangle/person_list.html', {'persons': person_queryset})
