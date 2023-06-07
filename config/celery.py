from __future__ import absolute_import, unicode_literals
import os
from celery import Celery, shared_task
from django.conf import settings
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

app = Celery('config')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')

app.conf.beat_schedule = {
    'add-every-5-seconds': {
        'task': 'vubon',
        'schedule': 5.0,
    },
    'add-every-minute-contrab': {
        'task': 'data_checking',
        'schedule': crontab(minute=1),
    },
}
