from django.shortcuts import render

# Create your views here.
# In quotes/views.py
def request_quote(request):
    if request.method == 'POST':
        form = QuoteRequestForm(request.POST, request.FILES)
        if form.is_valid():
            quote = form.save()
            # Send email notifications
            send_quote_notification(quote)
            return redirect('quote_success')
    else:
        form = QuoteRequestForm()
    return render(request, 'quotes/request_quote.html', {'form': form})
