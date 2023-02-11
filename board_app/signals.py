from django.core.mail import send_mail, mail_managers, mail_admins
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.db.models.signals import post_init, post_save, m2m_changed
from django.dispatch import receiver
from .models import Post, Reply
from .views import confirmation
# from django_lifecycle import LifecycleModel, hook, AFTER_UPDATE

#
# @receiver(post_save, sender=Reply)
# def notify_auth_reply(sender, instance, **kwargs):
#     subject = f'User {instance.reply_auth} replies on {instance.reply_post}'
#     auth_mail = instance.reply_post.post_auth.email
#     send_mail(
#         subject=subject,
#         message=instance.reply_text,
#         from_email='AndreySkillF2@yandex.ru',
#         recipient_list=[str(auth_mail)]
#     )


# @receiver(post_save, sender=confirmation)
# @hook(AFTER_UPDATE, when='confirmation', was='False', is_now='True')
# def notify_auth_confirm(sender, instance, **kwargs):
#     subject = f'User {instance.reply_post.post_auth} confirms your {instance.reply_text} on {instance.reply_post}'
#     auth_mail = instance.reply_auth.email
#     send_mail(
#         subject='Confirmation',
#         message=subject,
#         from_email='AndreySkillF2@yandex.ru',
#         recipient_list=[str(auth_mail)]
#     )
