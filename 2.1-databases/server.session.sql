from django.core.management.base import BaseCommand
import csv



class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            phones1 = list(csv.DictReader(file, delimiter=';'))

            for phone in phones1:
                Phone.object.create(
                    id = phone['id'],
                    name = phone['name'],
                    price = phone['price'],
                    image = phone['image'],
                    release_date = phone['release_date'],
                    lte_exists = phone['lte_exists'],
                    slug = phone[bool])             
            phone.save()   
            pass

        class Command(BaseCommand):
            def add_arguments(self, parser):
                pass
        
            def handle(self, *args, **options):
                with open('phones.csv', 'r') as file:
                    phones1 = list(csv.DictReader(file, delimiter=';'))
        
                    for phone in phones1:
                        Phone.object.create(
                            id = phone['id'],
                            name = phone['name'],
                            price = phone['price'],
                            image = phone['image'],
                            release_date = phone['release_date'],
                            lte_exists = phone['lte_exists'],
                            slug = phone[bool])             
                    phone.save()   
                    pass
        
                from django.core.management.base import BaseCommand
                import csv
                
                
                
                class Command(BaseCommand):
                    def add_arguments(self, parser):
                        pass
                
                    def handle(self, *args, **options):
                        with open('phones.csv', 'r') as file:
                            phones1 = list(csv.DictReader(file, delimiter=';'))
                
                            for phone in phones1:
                                Phone.object.create(
                                    id = phone['id'],
                                    name = phone['name'],
                                    price = phone['price'],
                                    image = phone['image'],
                                    release_date = phone['release_date'],
                                    lte_exists = phone['lte_exists'],
                                    slug = phone[bool])             
                            phone.save()   
                            pass
                
                        class Command(BaseCommand):
                            def add_arguments(self, parser):
                                pass
                        
                            def handle(self, *args, **options):
                                with open('phones.csv', 'r') as file:
                                    phones1 = list(csv.DictReader(file, delimiter=';'))
                        
                                    for phone in phones1:
                                        Phone.object.create(
                                            id = phone['id'],
                                            name = phone['name'],
                                            price = phone['price'],
                                            image = phone['image'],
                                            release_date = phone['release_date'],
                                            lte_exists = phone['lte_exists'],
                                            slug = phone[bool])             
                                    phone.save()   
                                    pass
                        
                                from django.core.management.base import BaseCommand
                                import csv
                                
                                
                                
                                class Command(BaseCommand):
                                    def add_arguments(self, parser):
                                        pass
                                
                                    def handle(self, *args, **options):
                                        with open('phones.csv', 'r') as file:
                                            phones1 = list(csv.DictReader(file, delimiter=';'))
                                
                                            for phone in phones1:
                                                Phone.object.create(
                                                    id = phone['id'],
                                                    name = phone['name'],
                                                    price = phone['price'],
                                                    image = phone['image'],
                                                    release_date = phone['release_date'],
                                                    lte_exists = phone['lte_exists'],
                                                    slug = phone[bool])             
                                            phone.save()   
                                            pass
                                
                                        