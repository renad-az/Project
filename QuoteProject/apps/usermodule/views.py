from django.shortcuts import render
from .models import Quote

def home(request):
    quotes = Quote.objects.all().order_by('-created_at')
    return render(request, 'apps/templates/quotemodule/home.html', {'quotes': quotes})

def add_quote(request):
    if request.method == 'POST':
        text = request.POST.get('text')
        author = request.POST.get('author')
        Quote.objects.create(text=text, author=author)
        return redirect('home')
    return render(request, 'apps/templates/quotemodule/add_quote.html')

def quote_detail(request, quote_id):
    quote = Quote.objects.get(id=quote_id)
    return render(request, 'apps/templates/quotemodule/quote_detail.html', {'quote': quote})

def profile(request):
    # Assuming you have user authentication implemented
    user = request.user
    quotes = Quote.objects.filter(user=user)
    return render(request, 'apps/templates/quotemodule/profile.html', {'user': user, 'quotes': quotes})
