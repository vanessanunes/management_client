from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Person
from .forms import PersonForm


@login_required
def persons_list(requests):
    persons = Person.objects.all()
    print(persons)
    return render(requests, 'person.html', {'persons': persons})


@login_required
def persons_new(requests):
    form = PersonForm(requests.POST or None, requests.FILES or None)

    if form.is_valid():
        form.save()
        return redirect('person_list')
    return render(requests, 'person_form.html', {'form': form})


@login_required
def persons_update(requests, id):
    person = get_object_or_404(Person, pk=id)
    form = PersonForm(requests.POST or None,
                      requests.FILES or None, instance=person)

    if form.is_valid():
        form.save()
        return redirect('person_list')

    return render(requests, 'person_form.html', {'form': form})


@login_required
def persons_delete(requests, id):
    person = get_object_or_404(Person, pk=id)

    if requests.method == 'POST':
        person.delete()
        return redirect('person_list')

    return render(requests, 'person_delete_confirm.html', {'person': person})
