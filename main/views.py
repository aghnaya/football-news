from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2406436410',
        'name': 'Aghnaya Kenarantanov',
        'class': 'PBP A'
    }

    return render(request, "main.html", context)
