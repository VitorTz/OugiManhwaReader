from constants import Constants
from dataclasses import dataclass
from pathlib import Path
from source import Source



@dataclass(frozen=True)
class Manhwa:

    name: str    
    source: Source
    link: str
    
    @property
    def path(self) -> Path:
        return Constants.root() / self.name.title()
            
    