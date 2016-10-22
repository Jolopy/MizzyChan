#!/usr/bin/env bash

DEVENV_USER=ubuntu
DEVENV_HOST=dev.sonic.mashframe.com

# Add ssh key if not present
if [[ `ssh-add -l | grep paulkey1.pem | wc -l` != 1 ]]; then
    ssh-add /home/paul/rudraya/misc/paulkey1.pem
fi


ssh $DEVENV_USER@$DEVENV_HOST sudo supervisorctl stop sonic-gunicorn
ssh $DEVENV_USER@$DEVENV_HOST sudo supervisorctl stop sonic-celery

ssh $DEVENV_USER@$DEVENV_HOST sudo chown ubuntu:sonic /var/www/sonic -R
ssh $DEVENV_USER@$DEVENV_HOST sudo chmod 777 /var/www/sonic -R

echo "Copying new files..."
#scp -r  ~/rudraya/workspace/sonic/ $DEVENV_USER@$DEVENV_HOST:/var/www/sonic
#rsync -r -v --progress ~/rudraya/workspace/sonic/ -e ssh $DEVENV_USER@$DEVENV_HOST:/var/www/sonic/
rsync -r --info=progress2 ~/rudraya/workspace/sonic/ ssh $DEVENV_USER@$DEVENV_HOST:/var/www/sonic/

ssh $DEVENV_USER@$DEVENV_HOST sudo chown ubuntu:sonic /var/www/sonic -R
ssh $DEVENV_USER@$DEVENV_HOST sudo chmod 777 /var/www/sonic -R

#ssh $DEVENV_USER@$DEVENV_HOST sudo supervisorctl start sonic-gunicorn
#ssh $DEVENV_USER@$DEVENV_HOST sudo supervisorctl start sonic-celery

echo "Deploy Complete"