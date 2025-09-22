from .models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.core.mail import send_mail
from django.conf import settings

@receiver(post_save,sender=User,dispatch_uid='send_welcome_email')
def send_welcome_email(sender,instance,created,**kwargs):
    '''Send mail when user is register'''
    print('signal fired')
    if created:
            subject='Welcome to Ecommerce Site'
            message = f"""
                        Hi {instance.username},

                        Welcome to E-commerce Sitr! 🎉

                        Thank you for signing up. We're excited to have you on board. Explore our products, enjoy exclusive offers, and experience seamless shopping right at your fingertips.

                        Happy shopping! 🛍️

                        Best regards,
                        The Api Team
                        """
            from_email=settings.DEFAULT_FROM_EMAIL
            recipient_list=[instance.email]


            send_mail(
                   subject, 
                   message, 
                   from_email, 
                   recipient_list,
                   fail_silently=False,
            )

