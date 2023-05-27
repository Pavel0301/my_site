from django.shortcuts import render
from allauth.account.decorators import verified_email_required

from allauth.account.forms import LoginForm, SignupForm, AddEmailForm, SetPasswordForm, ResetPasswordForm, ResetPasswordKeyForm
from allauth.socialaccount.forms import DisconnectForm, SignupForm

