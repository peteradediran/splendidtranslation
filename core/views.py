from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages




def home(request):
    return render(request, 'core/home.html')

def services(request):
    return render(request, 'core/services.html')

def about(request):
    return render(request, 'core/about.html')

def contact(request):
    return render(request, 'core/contact.html')

def about(request):
    # Team members data
    team_members = [
        {
            'name': 'Sarah Johnson',
            'position': 'Founder & CEO',
            'bio': 'With over 15 years in the translation industry, Sarah founded Splendid Translation to bridge cultural gaps through precise language services.',
            'image': 'https://images.unsplash.com/photo-1494790108377-be9c29b29330?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=400&q=80',
            'languages': ['English', 'French', 'Spanish']
        },
        {
            'name': 'Michael Chen',
            'position': 'Technical Director',
            'bio': 'Michael specializes in technical translations and has worked with major tech companies to localize their products for global markets.',
            'image': 'https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=400&q=80',
            'languages': ['Chinese', 'English', 'Japanese']
        },
        {
            'name': 'Elena Rodriguez',
            'position': 'Head of Linguistics',
            'bio': 'Elena leads our team of linguists, ensuring every translation maintains cultural authenticity and linguistic precision.',
            'image': 'https://images.unsplash.com/photo-1551836022-d5d88e9218df?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=400&q=80',
            'languages': ['Spanish', 'Portuguese', 'Italian']
        },
        {
            'name': 'David Kim',
            'position': 'Quality Assurance Manager',
            'bio': 'David ensures all translations meet our rigorous quality standards through meticulous review processes.',
            'image': 'https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=400&q=80',
            'languages': ['Korean', 'English', 'Chinese']
        }
    ]
    
    # Company milestones
    milestones = [
        {'year': '2010', 'event': 'Company Founded', 'description': 'Splendid Translation was established with a vision to provide premium translation services.'},
        {'year': '2013', 'event': 'First Major Client', 'description': 'Secured our first Fortune 500 client, marking our entry into corporate translation services.'},
        {'year': '2016', 'event': 'Global Expansion', 'description': 'Opened offices in Europe and Asia to better serve our international clients.'},
        {'year': '2019', 'event': 'Tech Integration', 'description': 'Implemented AI-assisted translation tools to enhance efficiency while maintaining quality.'},
        {'year': '2022', 'event': 'Industry Recognition', 'description': 'Received the Global Translation Excellence Award for outstanding service quality.'},
        {'year': '2023', 'event': '75+ Languages', 'description': 'Expanded our services to support over 75 languages and dialects.'}
    ]
    
    context = {
        'team_members': team_members,
        'milestones': milestones
    }
    return render(request, 'core/about.html', context)


def contact(request):
    if request.method == 'POST':
        # Get form data
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        service = request.POST.get('service')
        message = request.POST.get('message')
        
        # Basic validation
        if not name or not email or not message:
            messages.error(request, 'Please fill in all required fields.')
        else:
            # Send email notification
            subject = f'New Contact Form Submission from {name}'
            email_message = f'''
            Name: {name}
            Email: {email}
            Phone: {phone}
            Service: {service}
            Message: {message}
            
            This message was sent from the contact form on Splendid Translation.
            '''
            
            try:
                send_mail(
                    subject,
                    email_message,
                    settings.DEFAULT_FROM_EMAIL,
                    [settings.CONTACT_EMAIL],
                    fail_silently=False,
                )
                
                # Send confirmation email to user
                confirmation_subject = 'Thank you for contacting Splendid Translation'
                confirmation_message = f'''
                Dear {name},
                
                Thank you for reaching out to Splendid Translation. We have received your message and will get back to you within 24 hours.
                
                Here's a summary of your inquiry:
                Service: {service or 'Not specified'}
                Message: {message}
                
                Best regards,
                The Splendid Translation Team
                '''
                
                send_mail(
                    confirmation_subject,
                    confirmation_message,
                    settings.DEFAULT_FROM_EMAIL,
                    [email],
                    fail_silently=False,
                )
                
                messages.success(request, 'Your message has been sent successfully! We will get back to you soon.')
                return redirect('contact')
                
            except Exception as e:
                messages.error(request, 'There was an error sending your message. Please try again later.')
    
    # Services for dropdown
    services = [
        'Document Translation',
        'Interpretation Services',
        'Subtitling & Captioning',
        'Proofreading & Editing',
        'Transcription Services',
        'Localization',
        'Other'
    ]
    
    return render(request, 'core/contact.html', {'services': services})