from django.shortcuts import render, redirect
from .forms import SearchForm


def index(request):
    if request.method == "POST":
        form = SearchForm(request.POST)
        if form.is_valid():
            query = form.save(commit=False)
            query.user_id = request.user
            query.save()
            return redirect('search_result')
    else:
        form = SearchForm()
    return render(request, 'Website_0_1/Unauthenticated/index.html', {'form': form})


def search_result(request):
    print(request.GET)
    return render(request, 'Website_0_1/Unauthenticated/search_result.html')
