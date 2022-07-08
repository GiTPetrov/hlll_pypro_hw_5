from django.contrib.auth.models import User
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Delete one or more of the specified users'  # noqa: A003

    def add_arguments(self, parser):
        parser.add_argument(
            'usr_id',
            nargs='+',
            type=int,
            help='Sets the list of user ids to be deleted without superusers'
        )

        parser.add_argument(
            '-s', '--super',
            action='store_true',
            help='The specified users will be deleted including superusers',
        )

    def handle(self, *args, **options):
        user_id = set(options['usr_id'])
        user_filtered_list = User.objects.filter(id__in=user_id)
        check_id = user_filtered_list.values_list('id', flat=True)
        if len(check_id) != len(user_id):
            lst_1 = list(user_id.difference(set(check_id)))
            lst_1.sort()
            return self.stdout.write(self.style.ERROR(f"ERROR: These id's do not exist: {lst_1}"))
        if options['super']:
            user_filtered_list.delete()
        else:
            check_superuser = list(User.objects.filter(id__in=user_id, is_superuser=1).values_list('id', flat=True))
            if len(check_superuser) > 0:
                return self.stdout.write(self.style.ERROR(f"ERROR: These id's belong to superusers: {check_superuser}"))
            else:
                user_filtered_list.delete()
