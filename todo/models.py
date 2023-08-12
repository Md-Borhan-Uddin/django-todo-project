from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
# Create your models here.


class TodoModel(models.Model):
    todoTitle = models.CharField(_("Title"), max_length=255)
    todoDescription = models.TextField(_("Description"))
    is_completed = models.BooleanField(_("is Complited"), default=False)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.todoTitle
    
    def get_absolute_url(self):
        return reverse("show_todo")
    