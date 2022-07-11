from django.shortcuts import render

from triangle.forms import TriangleForm


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
