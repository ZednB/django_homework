from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.create(
            email='bibulatov.zubayr@mail.ru',
            first_name='zubayr',
            last_name='bibulatov',
            is_superuser=True,
            is_staff=True,
            is_active=True
        )
        user.set_password('Bz3d2yBz@')
        user.save()
