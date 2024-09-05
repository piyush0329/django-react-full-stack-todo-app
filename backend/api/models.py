from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.apps import apps

# CustomUserManager class
class CustomUserManager(BaseUserManager):
    def _create_user(self,username, password, **extra_fields):
        if not username:
            raise ValueError("UserName must be provided")
        if not password:
            raise ValueError('Password is not provided')


        GlobalUserModel = apps.get_model(
            self.model._meta.app_label, self.model._meta.object_name
        )
        username = GlobalUserModel.normalize_username(username)
        user = self.model(
            username=username,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user( username,password,  **extra_fields)

    def create_superuser(self,username, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_superuser', True)

        if username is None:
            raise ValueError("Superuser must have a username.")

        return self._create_user(username, password, **extra_fields)
    
    
# User Model class
class User(AbstractBaseUser, PermissionsMixin):
    def nameFile(instance,filename):
        return '/'.join(['images',str(instance.name),filename])
    username = models.CharField(db_index=True, unique=True,max_length=150)
    email = models.EmailField(max_length=254,null=True)
    first_name = models.CharField(max_length=240, default=None,null=True )
    last_name = models.CharField(max_length=255, default=None,null=True)
    mobile = models.CharField(max_length=50, default=None,null=True)
    address = models.CharField(max_length=250, default=None,null=True)
    pin_code = models.CharField(max_length=6, default=None,null=True)
    pan_card = models.CharField(max_length=10,default=None,null=True)
    aadhar_card= models.CharField(max_length= 12,default=None,null=True)
    profile_pic = models.ImageField(upload_to="nameFile",blank=True)

    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

# Note Model class
class Note(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notes')

    def __str__(self):
        return self.title
    

class Brother(models.Model):
    name = models.CharField(max_length=100)
    family_details = models.ForeignKey('FamilyDetails', related_name='brothers', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
class Sister(models.Model):
    name = models.CharField(max_length=100)
    family_details = models.ForeignKey('FamilyDetails', related_name='sisters', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class FamilyDetails(models.Model):
    total_members = models.CharField(max_length=10,null=True, default=None)
    father_name = models.CharField(max_length=100, null=True,default=None)
    mother_name = models.CharField(max_length=100,null=True,default=None)
    grandfather_name = models.CharField(max_length=100,null=True,default=None)
    grandmother_name = models.CharField(max_length=100,null=True,default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    user =  models.OneToOneField('User', on_delete=models.CASCADE, related_name='family_details')

    def __str__(self):
        return self.user.username



