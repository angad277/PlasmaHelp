from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.template.loader import render_to_string
from django.utils import six
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode


class TokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return (
            six.text_type(user.pk)
            + six.text_type(timestamp)
            + six.text_type(user.is_active)
        )


def send_mail(request, user):
    email_subject = "Activate Your Account"
    domain = request.get_host()
    print(domain)

    message = render_to_string(
        "activate_account.html",
        {
            "user": user,
            "domain": domain,
            "uid": urlsafe_base64_encode(force_bytes(user.pk)),
            "token": TokenGenerator().make_token(user),
        },
    )
    user.email_user(email_subject, message)
