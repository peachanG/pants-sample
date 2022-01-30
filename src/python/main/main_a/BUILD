pex_binary(
    name="main",
    entry_point="main.py",
    dependencies=[
        ":lib",
    ]
)
python_sources(name="lib", dependencies=["src/python/lib/lib_a"])

docker_image(name="docker", dependencies=["src/python/main/main_a:main"])
