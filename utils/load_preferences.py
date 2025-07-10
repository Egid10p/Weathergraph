# Copyright 2025 Egidio Pulicanò
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import tomllib
from pathlib import Path


class PreferencesLoader:
    def __init__(self, path: str | Path = None):  # type: ignore
        self.path = Path(path) if path else Path(__file__).resolve().parent.parent / "user_settings" / "settings.toml"
        self.preferences = self.load_preferences()
    
    def load_preferences(self) -> dict:  # type: ignore
        try:
            with self.path.open("rb") as f:
                return tomllib.load(f)
        except FileNotFoundError:
            raise FileNotFoundError(f"Configuration file does not exist: {self.path}")
        except tomllib.TOMLDecodeError as e:
            raise RuntimeError(f"Syntax error in TOML: {e}") from e
        
    def load_section(self, section: str) -> dict:
        try:
            return self.preferences[section]
        except KeyError:
            raise KeyError(f"Sección '{section}' no encontrada en {self.path}")


    def load_location_preferences(self) -> dict:
        """Load location preferences from the settings file."""
        if "location" in self.preferences:
            return self.load_section("location")
        else:
            raise KeyError(f"Missing 'location' section in {self.path}")
