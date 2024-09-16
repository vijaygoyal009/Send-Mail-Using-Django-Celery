from celery import shared_task
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils import timezone
from .models import Employee
from django.utils.html import strip_tags  # For plain text conversion



@shared_task
def send_birthday_wishes():
    # print("testing....................")
    today = timezone.now().date()
    today_month = today.month
    today_day = today.day
    employees = Employee.objects.filter(birthdate__month=today_month, birthdate__day=today_day)
    
    for employee in employees:
        subject = "Happy Birthday!"
        # message = render_to_string('birthday_template.html', {'employee': employee})
        html_message = render_to_string('birthday_template.html', {'employee': employee})
        
        # Create plain text version (as fallback) by stripping HTML tags
        plain_message = strip_tags(html_message)

        send_mail(
            subject,
            plain_message,
            'vijay.bridgefix@gamil.com',  
            [employee.email],
            fail_silently=False,
            html_message=html_message 
        )
    print("done ok tata bye bye")
