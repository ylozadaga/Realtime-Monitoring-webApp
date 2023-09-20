from django.core.management.base import BaseCommand
from receiver import mqtt


class Command(BaseCommand):
    help = 'Starts MQTT subscription'

    def handle(self, *args, **kwargs):
        mqtt.client.loop_forever()
