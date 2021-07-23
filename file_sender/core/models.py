from django.db import models
from django.utils.translation import gettext_lazy as _

class ImageSender(models.Model):
    img = models.ImageField(_('foto'))
    nome = models.CharField(_('nome completo'), max_length=75)
    email = models.EmailField(_('endereço de email'))
    # whatsapp = models.IntegerField(_('Whatsapp'))

    def __str__(self):
        return self.nome

    def get_primeiro_nome(self):
        nome_split = self.nome.split(' ')
        return nome_split[0]