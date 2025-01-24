from django.core.management.base import BaseCommand
from django.utils import timezone
from DHT.models import Dht11
class Command(BaseCommand):
    help = 'Update dt field to be timezone-aware'

    def handle(self, *args, **kwargs):
        for record in Dht11.objects.all():
            if timezone.is_naive(record.dt):
                record.dt = timezone.make_aware(record.dt, timezone.get_current_timezone())
                record.save()
        self.stdout.write(self.style.SUCCESS('Successfully updated dt fields to be timezone-aware'))