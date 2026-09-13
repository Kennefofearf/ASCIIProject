from pathlib import Path


def get_saved_characters():
    save_dir = Path(__file__).resolve().parents[2] / "saves"

    if not save_dir.exists():
        return []

    saved_characters = []

    for save_file in save_dir.glob("*.json"):
        saved_characters.append(save_file.stem)

    return saved_characters
