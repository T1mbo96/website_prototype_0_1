from django.shortcuts import render, redirect
from .forms import SearchForm
import ast
from .models import Contract, Price, Provider, Locations, Availability



def index(request):
    if request.method == "POST":
        form = SearchForm(request.POST)

        if form.is_valid():
            form_data = {}

            for data in form:
                form_data[data.name] = data.value()

            query = form.save(commit=False)
            query.user_id = request.user
            query.save()
            for data in form_data:
                print(data)
            return redirect('search_result', data=form_data)
    else:
        form = SearchForm()
    return render(request, 'Website_0_1/Unauthenticated/index.html', {'form': form})


def search_result(request, data):
    data_dict = ast.literal_eval(data)

    location_list = Locations.objects.filter(zip=data_dict.get('zip')).filter(street=data_dict.get('street')).filter(
        house_number=data_dict.get('house_number')).values()

    return render(request, 'Website_0_1/Unauthenticated/search_result.html')


def profile(request):
    return render(request, 'Website_0_1/Unauthenticated/profile.html')
