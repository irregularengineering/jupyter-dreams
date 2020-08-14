FROM python:3.6
ENV PROJECT_DIR=/opt/pewpyter \
    TERM=XTERM
EXPOSE 8888
RUN mkdir -p $PROJECT_DIR
WORKDIR $PROJECT_DIR
ADD ./requirements.txt $PROJECT_DIR/requirements.txt
RUN pip3 install -r requirements.txt
ADD . $PROJECT_DIR

# setup extensions with nbextensions configurator etc...
RUN jupyter nbextensions_configurator enable --user
RUN jupyter contrib nbextension install --user

# install the actual extensions
RUN jupyter nbextension enable --py widgetsnbextension
RUN jupyter nbextension enable --py qgrid
RUN jupyter nbextension enable scroll_down/main
RUN jupyter nbextension enable snippets_menu/main

# generate a config file for later modification
RUN jupyter notebook --generate-config

# Add logo
COPY ./utils/content/images/gamma.png /usr/local/lib/python3.6/site-packages/jupyterlab/static/base/images/logo.png
COPY ./utils/content/images/gamma.png /usr/local/lib/python3.6/site-packages/notebook/static/base/images/logo.png
COPY ./utils/content/images/gamma.png /usr/local/lib/python3.6/site-packages/ipykernel/resources/logo-32x32.png

COPY ./utils/content/images/favicon.ico /usr/local/lib/python3.6/site-packages/notebook/static/favicon.ico
COPY ./utils/content/images/favicon.ico /usr/local/lib/python3.6/site-packages/notebook/static/base/images/favicon.ico
COPY ./utils/content/images/favicon.ico /usr/local/lib/python3.6/site-packages/notebook/static/base/images/favicon-busy-1.ico
COPY ./utils/content/images/favicon.ico /usr/local/lib/python3.6/site-packages/notebook/static/base/images/favicon-busy-2.ico
COPY ./utils/content/images/favicon.ico /usr/local/lib/python3.6/site-packages/notebook/static/base/images/favicon-busy-3.ico
COPY ./utils/content/images/favicon.ico /usr/local/lib/python3.6/site-packages/notebook/static/base/images/favicon-file.ico
COPY ./utils/content/images/favicon.ico /usr/local/lib/python3.6/site-packages/notebook/static/base/images/favicon-notebook.ico
COPY ./utils/content/images/favicon.ico /usr/local/lib/python3.6/site-packages/notebook/static/base/images/favicon-terminal.ico

# now, modify the custom js and css
RUN python3 utils/inject_customization.py
