# Try1: ローカル実行（platformなし）
Commit: 
```
$ ./pants run src/python/main/whisper:main

```

# Try2: ローカル実行（platforms=["linux-x86_64-cp-38-cp38"]）
Commit: 
```
$ ./pants run src/python/main/whisper:main
15:18:22.81 [WARN] Pants cannot infer owners for the following imports in the target src/python/main/whisper/main.py:lib:

  * whisper (line: 1)

If you do not expect an import to be inferrable, add `# pants: no-infer-dep` to the import line. Otherwise, see https://www.pantsbuild.org/v2.14/docs/troubleshooting#import-errors-and-missing-dependencies for common problems.
15:18:24.09 [INFO] Completed: Building 1 requirement for src.python.main.whisper/main.pex from the thirdparty/python/python-default.lock resolve: openai-whisper
15:18:24.10 [ERROR] 1 Exception encountered:

  ProcessExecutionFailure: Process 'Building 1 requirement for src.python.main.whisper/main.pex from the thirdparty/python/python-default.lock resolve: openai-whisper' failed with exit code 1.
stdout:

stderr:
Failed to resolve compatible artifacts from lock thirdparty/python/python-default.lock for 1 target:
1. cp38-cp38-linux_x86_64:
    Failed to resolve all requirements for abbreviated platform cp38-cp38-linux_x86_64 from thirdparty/python/python-default.lock:

Configured with:
    build: False
    use_wheel: True

Dependency on openai-whisper not satisfied, 1 incompatible candidate found:
1.) openai-whisper 20230314 (via: openai-whisper) does not have any compatible artifacts:
    https://files.pythonhosted.org/packages/80/8b/13b7bf32b83fce396a814678661afdb8839b6b4713b3f2f2bc1499888654/openai-whisper-20230314.tar.gz

Dependency on future not satisfied, 1 incompatible candidate found:
1.) future 0.18.3 (via: openai-whisper -> ffmpeg-python==0.2.0 -> future) does not have any compatible artifacts:
    https://files.pythonhosted.org/packages/8f/2e/cf6accf7415237d6faeeebdc7832023c90e0282aa16fd3263db0eb4715ec/future-0.18.3.tar.gz

Use `--keep-sandboxes=on_failure` to preserve the process chroot for inspection.
```

# Try3: ローカル実行（platforms=["linux-x86_64-cp-38-cp38"], download_wheels)
Commit: 
## Local(macos)
```
$ pip wheel -w thirdparty/python/wheels openai-whisper
$ ./pants run src/python/main/whisper:main
```

## EC2
```
$ ./pants run src/python/main/whisper:main
$ ./pants run src/python/main/whisper:docker_image