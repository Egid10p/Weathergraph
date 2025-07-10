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

import os
from openpyxl import Workbook
from typing import Any

def ensure_file_exists(file_path: str) -> None:
    """
    Ensure that the specified file exists, creating it if it does not.

    Args:
        file_path (str): The path to the file to check or create.
        
    Raises:
        OSError: If there is an issue creating the file.
    """
    headers = ["current_temp", "min_temp", "max_temp", "date"]
    
    if not os.path.exists(file_path):
        try:
            # Create a new workbook and save it to the specified path
            wb = Workbook()
            ws = wb.active
            if headers:
                ws.append(headers)
            wb.save(file_path)
        except OSError as e:
            raise OSError(f"Failed to create file at {file_path}: {e}")