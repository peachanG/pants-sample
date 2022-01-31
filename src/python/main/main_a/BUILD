pex_binary(
    name="main",
    entry_point="main.py",
    dependencies=[
        ":lib",
    ],
    platforms=["linux-x86_64-cp-38-cp38"]
)
python_sources(name="lib", dependencies=["src/python/lib/lib_a"])

docker_image(name="docker", dependencies=["src/python/main/main_a:main"])
