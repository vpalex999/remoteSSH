""" Хранит конфигурацию объектов и команд выполнения."""
from typing import Any, Dict, List, Optional
import yaml


class Config:
    def __init__(self, data: Optional[Dict[str, Any]] = None) -> None:
        self.data = data

    @classmethod
    def from_file(cls, filename: str):
        with open(filename, 'r') as f:
            data = yaml.safe_load(f)
            return cls(data)

    @property
    def nodes(self) -> List[Dict[str, str]]:
        if self.data:
            try:
                return self.data["nodes"]
            except KeyError:
                print("No nodes list in config")

        return []

    @property
    def commands(self) -> List[str]:
        if self.data:
            try:
                return self.data["commands"]
            except KeyError:
                print("No commands key in config")

        return []

    def __str__(self) -> str:
        return str(self.data)
