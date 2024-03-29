from django.core.management.base import BaseCommand
from django_seed import Seed
from im.models import Role

class Command(BaseCommand):
    
    // TODO Сделать очистку служебной таблицы Role

    def handle(self, *args, **options):
        seeder = Seed.seeder()

        roles = [
            {
                'id':   1,
                'name': "Admin",
            },
            {
                'id':   2,
                'name': "User",
            }
        ]


        # money_types = [
        #     {
        #         'id':   1,
        #         'name': "Доллар",
        #     },
        #     {
        #         'id':   2,
        #         'name': "Рубль",
        #     }
        # ]


        for role in roles:
            seeder.add_entity(Role, 1, role)

        # for money in money_types:
        #     seeder.add_entity(Money, 1, money)


        inserted_pks = seeder.execute()