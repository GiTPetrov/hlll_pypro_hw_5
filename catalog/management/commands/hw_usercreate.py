from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string


class Command(BaseCommand):
    help = 'Create some random users'  # noqa: A003

    def add_arguments(self, parser):
        parser.add_argument(
            'num_usr',
            type=int,
            choices=range(1, 11),
            help='Sets the number of users to create')

    def handle(self, *args, **options):
        users_list = list()

        for i in range(options['num_usr']):
            usr_name = f'random_user_{get_random_string(length=10)}'
            usr_email = f'{usr_name}@ukr.net'
            passwrd = make_password(get_random_string(length=8))
            usr = User(
                username=usr_name,
                email=usr_email,
                password=passwrd,
            )
            users_list.append(usr)
        User.objects.bulk_create(users_list)
