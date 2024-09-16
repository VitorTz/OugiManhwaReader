from pathlib import Path
from typing import Any
import json


def read_json(path: Path, default_ = None):
    if not isinstance(path, Path):
        path = Path(path)
    try:
        with open(path, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return default_
    

def save_json(obj: Any, path: Path) -> None:
    if not isinstance(path, Path):
        path = Path(path)
    with open(path, "w+") as file:
        json.dump(obj, path, indent=4, sort_keys=True, check_circular=True)