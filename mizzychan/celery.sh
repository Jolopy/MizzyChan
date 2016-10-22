#!/usr/bin/env bash
celery -A celeryworker  worker --loglevel=debug -B --concurrency=20
