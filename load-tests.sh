#!/bin/sh
./manage.py loaddata api/fixtures/user.json && \
./manage.py loaddata api/fixtures/patient.js && \
./manage.py loaddata api/fixtures/doctor.json 