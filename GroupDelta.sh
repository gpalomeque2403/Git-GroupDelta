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
docker exec -it groupdeltad python3 /Git-GroupDelta/2a-meraki.py
docker exec -it groupdeltad python3 /Git-GroupDelta/2b-dnacenter.py
docker exec -it groupdeltad python3 /Git-GroupDelta/2c-csr100v.py
docker exec -it groupdeltad python3 /Git-GroupDelta/2d-webex.py
