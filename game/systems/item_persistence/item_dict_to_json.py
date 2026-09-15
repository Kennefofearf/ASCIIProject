import json
from pathlib import Path


def item_dict_to_json(item_data):
    save_dir = Path(__file__).resolve().parents[3] / "item_saves"

    save_dir.mkdir(exist_ok=True)

    save_file = save_dir / f"{item_data['name']}.json"

    if not save_file.exists():
        with open(save_file, "x") as f:
            json.dump(item_data, f, indent=4)
    else:
        with open(save_file, "w") as f:
            json.dump(item_data, f, indent=4)

