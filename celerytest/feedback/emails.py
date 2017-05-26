from django.conf import settings
from django.core.mail import EmailMessage,send_mail
from django.template.loader import render_to_string, get_template
from django.template import Context

# def send_feedback_email(email, message):
#     c = {'email': email, 'message': message}
#
#     email_subject = render_to_string(
#         'feedback/email/feedback_email_subject.txt', c).replace('\n', '')
#     email_body = render_to_string('feedback/email/feedback_create.html', c)
#
#     email = EmailMessage(subject=email_subject,
#                          body=email_body,
#                          from_email=settings.DEFAULT_FROM_EMAIL,
#                          to=[email,])
#     return email.send(fail_silently=False)
    # return send_mail(
    #     'celery测试邮件',
    #     message,
    #     '18051481300@163.com',
    #     [email],
    #     fail_silently=False,
    # )

def send_feedback_email(email, message):
    subject = "I am an HTML email"
    to = ['zhaonian.chen@ele.me']
    from_email = '18051481300@163.com'

    ctx = {
        'order_id': '1111',
        'order_title': '测试邮件工单',
        'creator':'znchen',
        'start_time':'2017-05-26 16:20:35',
        'end_time':'2017-05-27 16:20:35',
        'order_status':'工单完结'
    }

    message = get_template('feedback/email/feedback_create.html').render(ctx)
    msg = EmailMessage(subject, message, to=to, from_email=from_email)
    msg.content_subtype = 'html'
    msg.send()