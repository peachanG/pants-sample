python_sources(
    name="lib",
    dependencies=[
        "thirdparty/python:whisper"
    ]
)

pex_binary(
    name="main",
    entry_point="main.py",
    dependencies=[
        ":lib",
    ],
)

docker_image(
    name="whisper_docker"
)