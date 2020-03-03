from django.shortcuts import render

def main_page(request):
    return render(request, 'game/main_page.html', {})

