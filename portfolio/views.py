# Class-based views
# Django imports
from django.views.generic import ListView
from .models import HomePage, About, Contact, Project
from .forms import ContactForm
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views.generic.edit import FormView
from django.contrib import messages

# Send email imports
from django.core.mail import send_mail
from django.conf import settings

class HomePageView(ListView):
    """
    Views for home.
    """
    template_name = 'portfolio/index.html'
    
    model = HomePage
    queryset = HomePage.objects.all()
    context_object_name = 'home_data'
        
class ProjectsListView(ListView):
    """
    View for projects page
    """
    template_name = 'portfolio/projects.html'
    
    model = Project
    queryset = Project.objects.all()
    context_object_name = 'projects_data'


class AboutView(ListView):
    """
    View for about_me page
    """
    template_name = 'portfolio/about.html'
    
    model = About
    queryset = About.objects.all()
    context_object_name = 'about_data'
        
        
class ContactFormView(FormView):
    """
    Views for users ContactForm
    """
    model = Contact
    form_class = ContactForm
    template_name = 'portfolio/contact.html'
    
    def form_valid(self, form):
        # Save the contact to the database
        contact = form.save()

        # Prepare email data
        subject = f"New Contact Form Submission: {contact.subject}"
        message = (
            f"Name: {contact.name}\n"
            f"Email: {contact.email}\n"
            f"Message:\n{contact.message}"
        )
        from_email = contact.email
        recipient_list = [settings.EMAIL_HOST_USER] 

        # Send email
        send_mail(subject, message, from_email, recipient_list, fail_silently=False)

        messages.success(
            self.request,
            'Thank you for contacting. Message received, I will get back to you shortly.'
        )
        
        return HttpResponseRedirect(reverse('index'))

    def form_invalid(self, form):
        messages.info(
            self.request,
            'Please correct the errors below.'
        )
        # return self.render_to_response(self.get_context_data(form=form))
        return super().form_invalid(form)
