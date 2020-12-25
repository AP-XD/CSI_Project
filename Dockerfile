FROM python:3.9

RUN apt -qq update
RUN apt -qq install -y --no-install-recommends \
    curl \
    git \
    gnupg2 \
    wget \

RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && apt install -y ./google-chrome-stable_current_amd64.deb && rm google-chrome-stable_current_amd64.deb
RUN wget https://chromedriver.storage.googleapis.com/86.0.4240.22/chromedriver_linux64.zip && unzip chromedriver_linux64.zip && chmod +x chromedriver && mv -f chromedriver /usr/bin/ && rm chromedriver_linux64.zip
RUN git clone https://github.com/APXD-git/CSI_Project /root/csi
WORKDIR /root/csi/
RUN chmod +x /usr/local/bin/*
RUN pip install -r requirements.txt
CMD [ "python3", "-m", "csi" ]
