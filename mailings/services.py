from django.core.mail import send_mail
from django.conf import settings

from mailings.models import MailingSettings


def send_mailing(mailing_item: MailingSettings):
    for client in mailing_item.clients.all():
        send_mail(
            mailing_item.message.subject,
            mailing_item.message.content,
            settings.EMAIL_HOST_USER,
            [client.email]
        )



