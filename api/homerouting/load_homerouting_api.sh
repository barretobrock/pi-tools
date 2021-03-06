#!/usr/bin/env bash
# LOADS HOSTS API SERVICE INTO SYSTEMD

SERVICEFILE=homerouting_api.service
API_FPATH=~/extras/pitools/api/homerouting/${SERVICEFILE}
LIB_FPATH=/lib/systemd/system/${SERVICEFILE}

# Copy the service file to lib
sudo cp ${API_FPATH} ${LIB_FPATH}
# Set permissions on it - owner has r/w perms, everyone else has read-only
sudo chmod 644 ${LIB_FPATH}
# Load service & allow boot on restart
sudo systemctl daemon-reload
sudo systemctl enable ${LIB_FPATH}

