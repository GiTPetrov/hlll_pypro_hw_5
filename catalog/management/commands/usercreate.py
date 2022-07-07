from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from faker import Faker
import random


fake = Faker()


class Command(BaseCommand):
    help = 'Create some random users'

    def add_arguments(self, parser):
        parser.add_argument(
            'num_usr',
            type=int,
            choices=range(1, 11),
            help='Sets the number of users to create')

        parser.add_argument(
            '-s', '--super',
            action='store_true',
            help='Will be create the random number of superusers from total users',
        )

    def handle(self, *args, **options):
        users_list = list()

        for i in range(options['num_usr']):
            frst_name = fake.unique.first_name()
            lst_name = fake.unique.last_name()
            usr_email = f'{frst_name.casefold()}.{lst_name.casefold()}@{fake.domain_name()}'

            while True:
                usr_name = f'{frst_name.casefold()}_{random.randrange(0, 2000)}'
                if User.objects.filter(username=usr_name).exists() is False:
                    break
            if options['super']:
                is_super = random.randrange(0, 2)
            else:
                is_super = 0
            passwrd = make_password(f'{frst_name[0:3]}{lst_name[0:3]}123')
            usr = User(
                username=usr_name,
                first_name=frst_name,
                last_name=lst_name,
                email=usr_email,
                is_superuser=is_super,
                password=passwrd,
            )
            users_list.append(usr)
        User.objects.bulk_create(users_list)
