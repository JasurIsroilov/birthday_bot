from celery import Celery
from celery.schedules import crontab


app = Celery('mycelery', include=['mycelery.tasks'])


app.conf.beat_schedule = {
    'run-every-morning': {
        'task': 'mycelery.tasks.mailing.congrat',
        'schedule': crontab(hour='14', minute='5'),
    },
}
app.config_from_object('mycelery.celeryconfig')
