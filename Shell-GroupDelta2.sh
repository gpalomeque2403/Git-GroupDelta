#!/bin/bash
docker run -t -d --name groupdeltad tano2403/shell-groupdelta:latest
docker ps -a
echo "********************************** 2A **********************************"
docker exec -it groupdeltad python3 /Git-GroupDelta/2a-meraki.py
echo "********************************** 2B **********************************"
docker exec -it groupdeltad python3 /Git-GroupDelta/2b-dnacenter.py
echo "********************************** 2C **********************************"
docker exec -it groupdeltad python3 /Git-GroupDelta/2c-csr100v.py
echo "********************************** 2D **********************************"
docker exec -it groupdeltad python3 /Git-GroupDelta/2d-webex.py
