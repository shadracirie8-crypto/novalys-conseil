
from django.db import models


class ContactMessage(models.Model):
    nom = models.CharField(max_length=100)
    email = models.EmailField()
    telephone = models.CharField(max_length=20, blank=True)
    sujet = models.CharField(max_length=150)
    message = models.TextField()
    date_envoi = models.DateTimeField(auto_now_add=True)
    lu = models.BooleanField(default=False)

    class Meta:
        ordering = ["-date_envoi"]
        verbose_name = "Message de contact"
        verbose_name_plural = "Messages de contact"

    def __str__(self):
        return f"{self.nom} - {self.sujet}"
