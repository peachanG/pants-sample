FROM python:3.8.17-slim-bullseye

COPY src.python.main.whisper/main.pex /tmp/main.pex
RUN \
    PEX_TOOLS=1 /usr/local/bin/python3.8 /tmp/main.pex venv \
        --remove all \
        --compile \
        --bin-path prepend \
        /bin/whisper

ENTRYPOINT ["/bin/whisper/pex"]