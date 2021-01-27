#!/bin/sh
./manage.py loaddata api/fixtures/user.json && \
./manage.py loaddata api/fixtures/patient.json && \
./manage.py loaddata api/fixtures/doctor.json 