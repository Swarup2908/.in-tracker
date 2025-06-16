from celery.schedules import crontab

beat_schedule = {
    'run-domain-scraper-monthly': {
        'task': 'tasks.run_domain_scraper',
        'schedule': crontab(day_of_month=3, hour=0, minute=0),  
    },
}

timezone = 'Asia/Kolkata'
