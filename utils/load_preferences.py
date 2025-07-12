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
from typing import Union, Optional


class PreferencesLoader:
    """Loads user preferences from a TOML configuration file."""

    def __init__(self, path: Optional[Union[str, Path]] = None) -> None:
        """Initializes the PreferencesLoader.

        If no path is provided, it defaults to:
        `<project_root>/user_settings/settings.toml`.

        Args:
            path (Optional[Union[str, Path]]): The path to the TOML configuration file.
                Can be a string or a Path object. If None, the default path is used.
        """
        self.path = Path(path) if path else Path(__file__).resolve().parent.parent / "user_settings" / "settings.toml"
        self.preferences = self.load_preferences()

    def load_preferences(self) -> dict:
        """Reads and parses the TOML configuration file.

        Returns:
            dict: A dictionary containing all user-defined preferences.

        Raises:
            FileNotFoundError: If the configuration file does not exist.
            RuntimeError: If the TOML file has a syntax error.
        """
        try:
            with self.path.open("rb") as f:
                return tomllib.load(f)
        except FileNotFoundError:
            raise FileNotFoundError(f"Configuration file does not exist: {self.path}")
        except tomllib.TOMLDecodeError as e:
            raise RuntimeError(f"Syntax error in TOML: {e}") from e

    def load_section(self, section: str) -> dict:
        """Retrieves a specific section from the loaded preferences.

        Args:
            section (str): The name of the section to retrieve.

        Returns:
            dict: The dictionary corresponding to the requested section.

        Raises:
            KeyError: If the specified section is not found in the preferences.
        """
        try:
            return self.preferences[section]
        except KeyError:
            raise KeyError(f"Section '{section}' not found in {self.path}")

    def load_location_preferences(self) -> dict:
        """Loads the 'location' preferences section.

        Returns:
            dict: The contents of the 'location' section.

        Raises:
            KeyError: If the 'location' section is missing from the preferences.
        """
        if "location" in self.preferences:
            return self.load_section("location")
        else:
            raise KeyError(f"Missing 'location' section in {self.path}")
