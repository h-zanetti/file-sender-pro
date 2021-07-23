from django.shortcuts import redirect, render
from .forms import ImageSenderForm
from django.contrib import  messages
from django.core.mail import EmailMessage
from file_sender.settings.base import EMAIL_HOST_USER
# from django.contrib.auth.decorators import login_required

# @login_required
def index(request):
    if request.method == 'POST':
        form = ImageSenderForm(request.POST, request.FILES)
        if form.is_valid():
            model = form.save()
            email = EmailMessage(
                'Demo para evento da Mercedes',
                f'{model.get_primeiro_nome()},\nVocê está recebendo este e-mail porque enviou o formulário de teste da demostração do sistema para o evento da Mercedes.\nAnexado neste e-mail você encontra-rá a foto que foi enviada pelo formulário.\n\nObrigado pela preferência,\nTime de desenvolvimento AGAH Solutions.',
                EMAIL_HOST_USER,
                [model.email],
            )
            email.attach(model.img.name, model.img.file.read())
            email.send()
            messages.success(request, 'Mensagem enviada com sucesso!')
            return redirect('core:index')
    else:
        form = ImageSenderForm()
    return render(request, 'core/index.html', {'form': form})
