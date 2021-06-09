from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.core.files.storage import FileSystemStorage
from django.conf import settings


def send_mail(template, context=None,
              from_email=settings.DEFAULT_FROM_EMAIL):

    subject, content = render_message(template, context)

    msg = EmailMessage('Proxima Resume', content, from_email, to=['koggi@mail.ru'])
    if context['resume']['file']:
        fs = FileSystemStorage()
        try:
            filename = fs.save(context['resume']['file'].name, context['resume']['file'])
            msg.attach(context['resume']['file'].name, fs.open(filename).read(), context['resume']['file'].content_type)
        except:
            pass
    msg.content_subtype = 'html'
    msg.send()


def render_message(template, context={}):
    context = context.copy()
    context.update({'BASE_URL': settings.BASE_URL})

    text = render_to_string(template, context)
    subject, message = text.split('---')

    return subject.strip(), message.strip()
