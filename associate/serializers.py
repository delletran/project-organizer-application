from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import get_user_model
# from django.utils.text import slugify

from rest_framework import serializers
from rest_framework.fields import CurrentUserDefault
from rest_framework.validators import UniqueTogetherValidator

User = get_user_model()
from project.models import Project, ProjectMember

# class ChoicesSerializer(serializers.ChoiceField):
#   def to_representation(self, value):
#     if value in self.choices.keys():
#       return self.choices[value]

#     self.fail("invalid_choice", input=value)
#     return None

#   def to_internal_value(self, data):
#     for key, value in self.choices.items():
#       if value == data:
#         return key
#     self.fail("invalid_choice", input=data)
#     return None



class CreatedBySerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = [ 'id', 'username', 'job_title']


class MemberSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = [ 'id', 'username', 'first_name', 'last_name', 'job_title']


class ProjectSerializer(serializers.ModelSerializer):
  created_by = CreatedBySerializer(read_only=True)
  status = ChoicesSerializer(choices=Project.STATUS.choices)
  project_type = ChoicesSerializer(choices=Project.TYPE.choices)
  members = MemberSerializer(read_only=True, many=True)
  # schedule = ScheduleSerializer(read_only=True)

  class Meta:
    model = Project
    fields = "__all__"
    fields = ['id', 'name', 'slug', 'description', 'project_type', 'status', 'created_by', 'members']
  



class ProjectCreateSerializer(serializers.ModelSerializer):

  class Meta:
    model = Project
    fields = ["name", "description", "status", "project_type", "created_by"]
    # write_only_fields=['created_by']
    validators = [
      UniqueTogetherValidator(
        queryset=Project.objects.all(),
        fields=('name', 'created_by'),
        message=_("User has already created a project with this name.")
      )
    ]