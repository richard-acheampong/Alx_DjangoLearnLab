from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, Permission
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import Group
from django.dispatch import receiver
from django.db.models.signals import post_save

# Book Model with Custom Permissions
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    publication_year = models.IntegerField()
    
    class Meta:
        permissions = [
            ("can_view", "Can view book"),
            ("can_create", "Can create book"),
            ("can_edit", "Can edit book"),
            ("can_delete", "Can delete book"),
        ]

# Custom User Model
class CustomUser(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.username

# Custom User Manager
class CustomUserManager(BaseUserManager):
    def create_user(self, email, username, password=None, date_of_birth=None, profile_photo=None):
        if not email:
            raise ValueError('Users must have an email address')
        if not username:
            raise ValueError('The Username field must be set')

        email = self.normalize_email(email)
        user = self.model(email=email, username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None):
        user = self.create_user(email, username, password)
        user.is_admin = True
        user.is_staff = True
        user.save(using=self._db)
        return user

# User Profile Model
class UserProfile(models.Model):
    ROLE_CHOICES = [
        ('Admin', 'Admin'),
        ('Librarian', 'Librarian'),
        ('Member', 'Member'),
    ]
    
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='Member')

    def __str__(self):
        return f"{self.user.username} - {self.role}"
    
    @receiver(post_save, sender=CustomUser)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            UserProfile.objects.create(user=instance)
        else:
            instance.userprofile.save()

# Signal to Create Groups and Assign Permissions
@receiver(post_save, sender=Book)
def create_groups_and_permissions(sender, **kwargs):
    groups_permissions = {
        "Editors": ["can_create", "can_edit"],
        "Viewers": ["can_view"],
        "Admins": ["can_create", "can_edit", "can_delete", "can_view"],
    }

    content_type = ContentType.objects.get_for_model(Book)
    for group_name, perms in groups_permissions.items():
        group, created = Group.objects.get_or_create(name=group_name)
        for perm_code in perms:
            permission, _ = Permission.objects.get_or_create(codename=perm_code, name=f"Can {perm_code} book", content_type=content_type)
            group.permissions.add(permission)
