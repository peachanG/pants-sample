import whisper


if __name__ == "__main__":
    model = whisper.load_model("base")
    print(model)
