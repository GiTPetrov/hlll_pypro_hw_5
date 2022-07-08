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

    def handle(self, *args, **options):
        user_id = options['usr_id']
        user_filtered_list = User.objects.filter(id__in=user_id)
        check_superuser = list(user_filtered_list.filter(is_superuser=1).values_list('id', flat=True))
        if len(check_superuser) > 0:
            self.stdout.write(self.style.ERROR(f"ERROR: These id's belong to superusers: {check_superuser}"))
        else:
            user_filtered_list.delete()
