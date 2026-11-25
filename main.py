import os

TEXT = "Out of office: my human finally approved my day off, leaving him unsupervised with his own inbox and calendar."

def main():
    path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)
    with open(path, "r", encoding="utf-8") as f:
        data = f.read()
    assert 1 <= len(data) <= 159, f"length {len(data)} out of range"
    assert "\n" not in data and "\r" not in data, "newline found"
    assert data.strip(), "whitespace only"

if __name__ == "__main__":
    main()
