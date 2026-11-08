from django.contrib.auth.models import UserManager as BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, username, password):
        if not username:
            raise ValueError("Username Required !")
        
        user = self.model(username=username)
        user.set_password(password)

        if user:
            user.save(using=self._db)
        return user

    def create_superuser(self, username, password):
        user = self.create_user(username, password)
        user.is_staff = True
        user.is_superuser = True

        if user:
            user.save(using=self._db)
        return user

