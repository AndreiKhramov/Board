from django.core.mail import send_mail, mail_managers, mail_admins
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Post


@receiver(post_save, sender=Post)
def notify_admins_post(sender, instance, **kwargs):
    subject = f'{instance.post_auth} {instance.title}'

    send_mail(
        subject=subject,
        message=instance.post_text,
        from_email='AndreySkillF2@yandex.ru',
        recipient_list=['ter_ah@mail.ru']
    )