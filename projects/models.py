import uuid

from django.db import models

from accounts.models import User


class Project(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField("имя", max_length=255)
    description = models.TextField("описание", blank=True, null=True)
    created_by = models.ForeignKey(User, related_name='projects', on_delete=models.CASCADE)

    def __str__(self):
        return f'Проект self.name'


class ProjectFile(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    project = models.ForeignKey(Project, related_name='files', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    attachment = models.FileField(upload_to='projectfiles')

    def __str__(self):
        return f'Файл для проекта {self.project}'


class ProjectNote(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    project = models.ForeignKey(Project, related_name='notes', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    body = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
