#!/bin/bash
mkdir Shell-GroupDelta

echo "FROM python" >> Shell-GroupDelta/Dockerfile
echo "RUN pip install requests" >> Shell-GroupDelta/Dockerfile
echo "RUN pip install simplejson" >> Shell-GroupDelta/Dockerfile
echo "RUN git clone https://github.com/gpalomeque2403/Git-GroupDelta.git" >> Shell-GroupDelta/Dockerfile

cd Shell-GroupDelta
docker build -t groupdelta .
docker run -t -d --name groupdeltad groupdelta
docker ps -a
echo "********************************** 2A **********************************"
docker exec -it groupdeltad python3 /Git-GroupDelta/2a-meraki.py
echo "********************************** 2B **********************************"
docker exec -it groupdeltad python3 /Git-GroupDelta/2b-dnacenter.py
echo "********************************** 2C **********************************"
docker exec -it groupdeltad python3 /Git-GroupDelta/2c-csr100v.py
echo "********************************** 2D **********************************"
docker exec -it groupdeltad python3 /Git-GroupDelta/2d-webex.py
