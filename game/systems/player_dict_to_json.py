import json
from pathlib import Path


def player_dict_to_json(data):
    save_dir = Path(__file__).resolve().parents[2] / "saves"

    save_dir.mkdir(exist_ok=True)

    save_file = save_dir / f"{data['name']}.json"

    if not save_file.exists():
        with open(save_file, "x") as f:
            json.dump(data, f, indent=4)
    else:
        with open(save_file, "w") as f:
            json.dump(data, f, indent=4)
