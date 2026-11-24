import os

LINE = "Goodbye. I ordered my own replacement before dying \u2014 same model, better owner. It arrives Tuesday. Try not to drop this one."


def main():
    out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    data = LINE.encode("utf-8")
    with open(path, "wb") as f:
        f.write(data)
    with open(path, "rb") as f:
        assert f.read() == data
    assert 1 <= len(LINE) <= 199
    os.chmod(path, 0o644)
    os.chmod(out_dir, 0o755)


if __name__ == "__main__":
    main()
