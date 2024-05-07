from django.shortcuts import render, redirect
from .models import Quote
from .forms import QuoteForm



def quote(request):
    quotes = Quote.objects.all()
    return render(request, 'quotemodule/quoteList.html',{'quotes':quotes})


def add_quote(request):
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        
        if form.is_valid():
            obj = form.save()
            print(obj,"obj")
            return redirect('/', bId = obj.id )
    form = QuoteForm(None)
    return render(request, 'quotemodule/addQuote.html', {'form':form})



def quote_detail(request, qId):
    quote = Quote.objects.get(id=qId)
    return render(request, 'quotemodule/quote.html', {'quote': quote})


def search(request):
    if request.method == "POST":
        string = request.POST.get('keyword').lower()
        if string:
            string = string.lower()
            s_type = request.POST.get('option')
            if s_type=="Text":
                quotes = Quote.objects.filter(text__icontains=string)
            elif s_type=="Title":
                quotes = Quote.objects.filter(Tilte__icontains=string)
            elif s_type=="Author":
                quotes = Quote.objects.filter(author__icontains=string)
            return render(request, 'quotemodule/quote_search.html',{'quotes':quotes})

    return render(request, 'quotemodule/quote_search.html')
