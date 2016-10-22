from datetime import timedelta

CELERYBEAT_SCHEDULE = {
    #'checker': {
    #    'task': 'app.aws.taskQueue.runChecker',
    #    'schedule': timedelta(minutes=600),
    #},
    #'updateSVNCache': {
    #    'task': 'app.sonicVC.ProjectCache.updateSVNCacheInterval',
    #    'schedule': timedelta(minutes=600),
    #},
}
