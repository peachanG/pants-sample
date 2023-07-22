python_sources(
    name="lib",
    dependencies=[
        "thirdparty/python:whisper"
    ]
)

pex_binary(
    name="main",
    entry_point="main.py",
    environment="python_bullseye",
    dependencies=[
        ":lib",
    ],
)

docker_image(
    name="docker",
)