from django.contrib.auth.models import User


def run():
    user = User.objects.create_user(username='user', email='testuser@test.com',
                                    password='password')
    user.last_name = 'lastname'
    user.set_password('newpassword')
    user.save()

    print(f"Created user: {user.username} with email: {user.email} and "
          f"last name: {user.last_name}")
