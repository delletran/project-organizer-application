from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.text import slugify
from django.contrib.auth import get_user_model
from django.conf import settings

from django.dispatch import receiver
from django.db.models.signals import post_save
from django.db.models.signals import pre_save
from django.db.models.signals import m2m_changed
from django.utils.crypto import get_random_string

from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode

MAX_LENGTH_NAME = settings.MAX_LENGTH_NAME
MAX_LENGTH_USERNAME = settings.MAX_LENGTH_USERNAME
MAX_LENGTH_JOB = settings.MAX_LENGTH_JOB
MAX_LENGTH_DESC = settings.MAX_LENGTH_DESC
MAX_LENGTH_TEXT = settings.MAX_LENGTH_TEXT
MAX_LENGTH_CHOICES = settings.MAX_LENGTH_CHOICES

USER = get_user_model()
PROJECT = 'project.Project'


class Collaborator(models.Model): 
  class POSITION(models.IntegerChoices):
    PAD = 1, _('Project Admin'),
    PMA = 2, _('Project Manager'),
    PLE = 3, _('Project Leader'), 
    MEM = 4, _('Member'),
    CUS = 5, _('Custom')

  class STATUS(models.TextChoices):
    ONHOLD = 'Invited', 
    JOINED = 'Joined',
    LEAVED = 'Leave',
    DECLINED = 'Declined'

  name = models.ForeignKey(USER, related_name='collaborator', on_delete=models.CASCADE)
  project = models.ForeignKey(PROJECT, on_delete=models.CASCADE)
  position = models.PositiveSmallIntegerField(choices=POSITION.choices, default=POSITION.MEM)
  inviter = models.ForeignKey(USER, related_name='group_invites', on_delete=models.CASCADE, blank=True, null=True)
  is_active = models.BooleanField(_("invite_active"), default=True)
  status = models.CharField(_("invite status"), max_length=MAX_LENGTH_NAME, choices=STATUS.choices, default=STATUS.ONHOLD)
  # permission_1 = models.BooleanField(_("manager_permission"), default=False)
  # permission_2 = models.BooleanField(_("accounting_permission"), default=False)
  # permission_3 = models.BooleanField(_("document_permission"), default=True)

  class Meta:
    unique_together = ['name', 'project']
    verbose_name = _("Collaborator")
    verbose_name_plural = _("Collaborators")

  def __str__(self):
    return f'{self.project} -- {self.name}'

@receiver(pre_save, sender=Collaborator)
def pre_save_project_group(sender, instance, *args, **kwargs):
  _status = instance.status
  if _status == 'Joined' or _status =='Leave' or _status =='Declined' :
    instance.is_active = False
  elif _status == 'Invited':
    instance.is_active = True




# @receiver(post_save, sender=Collaborator)
# def post_save_project_group(sender, instance, created, *args, **kwargs):
#   _sender = instance.inviter
#   _receiver = instance.collaborator
#   _status = instance.status
#   if not created:
#     if _status == 'Joined':

    # if _status =='Leave':
    #   if _status =='Declined' :
    #   if _status =='Invited' :
  



# @receiver(pre_save, sender=Project)
# def pre_save_project(sender, instance, *args, **kwargs): 
#   print('added: ', instance.admin.all())

# @receiver(post_save, sender=Project)
# def post_save_project(sender, instance, created, *args, **kwargs):
#   if not created:
#     instance.admin.set([instance.created_by])

# @receiver(m2m_changed, sender=Project.admin.through)
# def user_admin_change(sender, instance, action, *args, **kwargs):
#   if action == 'post_add':
#     if not (instance.admin.all().filter(pk=_created_by.pk).exists()):
#       instance.admin.add(_created_by)