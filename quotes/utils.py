# In quotes/utils.py
def send_quote_notification(quote):
    # Email to company
    company_subject = f'New Quote Request from {quote.name}'
    company_message = f'''
    New quote request details:
    Name: {quote.name}
    Email: {quote.email}
    Phone: {quote.phone}
    From: {quote.source_language} to {quote.target_language}
    Notes: {quote.notes}
    '''
    send_mail(company_subject, company_message, 'noreply@splendidtranslation.com', ['your-email@splendidtranslation.com'])
    
    # Confirmation email to client
    client_subject = 'Thank you for your quote request'
    client_message = f'''
    Dear {quote.name},
    Thank you for contacting Splendid Translation. We have received your request for a translation from {quote.source_language} to {quote.target_language}.
    Our team will review your documents and get back to you within 24 hours.
    '''
    send_mail(client_subject, client_message, 'noreply@splendidtranslation.com', [quote.email])