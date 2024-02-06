#!/bin/bash

echo start 600d script

# wechsel in dne Ordner des Skripts
SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )

cd ${SCRIPT_DIR}
echo aktueller Ordner  ${SCRIPT_DIR}
chmod -R 775 untis/static
echo activate venv
source venvlinux/bin/activate
echo venvlinux activated

echo collect static
cd D600
../venvlinux/bin/python3.11 ../D600/manage.py collectstatic --noinput
echo static collected
rsync -ar static_collected/. /var/www/html/600d.mes-zugang.de/

echo start tmux session D600
tmux new-session -d -s D600  'gunicorn D600.wsgi'
echo tmux session D600 started. Attach with tmux a
