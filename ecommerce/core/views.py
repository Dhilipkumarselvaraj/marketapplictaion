from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.views import password_reset, password_reset_confirm
from django.core.urlresolvers import reverse
from core.forms import SignUpForm


@login_required
def home(request):
    return render(request, 'home.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def reset(request):
    # Wrap the built-in password reset view and pass it the arguments
    # like the template name, email template name, subject template name
    # and the url to redirect after the password reset is initiated.
    return password_reset(request, template_name='registration/password_reset_confirm.html',
        email_template_name='registration/password_reset_email.html',
        subject_template_name='registration/password_reset_subject.txt',
        post_reset_redirect=reverse('success'))

def reset_confirm(request, uidb64=None, token=None):
    # Wrap the built-in reset confirmation view and pass to it all the captured parameters like uidb64, token
    # and template name, url to redirect after password reset is confirmed.
    return password_reset_confirm(request, template_name='registration/password_reset_confirm.html',
        uidb36=uidb36, token=token, post_reset_redirect=reverse('success'))

def success(request):
  return render(request, "registration/password_reset_done.html")

