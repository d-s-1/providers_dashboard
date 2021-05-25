#!/bin/sh

# (ran "dos2unix.exe boot.sh" in Git Bash to convert this file to Unix style)

source venv/bin/activate

# run gunicorn with 4 workers & bind to the specified server socket;
# (on why "exec" and the "-" following the log files are used, see https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xix-deployment-on-docker-containers)
exec gunicorn -w 4 -b :5000 --access-logfile - --error-logfile - dashboard:server_flask
