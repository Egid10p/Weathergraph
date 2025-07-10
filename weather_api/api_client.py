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

import requests

class APIRequester:
    """
    Simple HTTP client for performing GET requests to external APIs.

    This class encapsulates the logic for making a GET request to a specified URL
    and parsing the response as JSON.

    Attributes:
        url (str): The fully constructed URL to be queried, including parameters.
    """

    def __init__(self, url: str) -> None:
        """
        Initializes the APIRequester with a target URL.

        Args:
            url (str): The full API endpoint to query.
        """
        self.url = url

    def get_data(self) -> dict:
        """
        Executes a GET request to the specified URL and parses the response as JSON.

        Returns:
            dict: The response body parsed as a dictionary.

        Raises:
            Exception: If the request fails or returns a non-200 HTTP status code.
        """
        response = requests.get(self.url)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Error fetching data: {response.status_code}")


class APIParser:
    """
    Parses weather data returned by the Open-Meteo API.

    This class extracts key weather metrics such as current temperature, 
    minimum and maximum daily temperatures, and the associated date 
    from the raw API JSON response.

    Attributes:
        data (dict): The raw JSON response obtained from the API.
    """

    def __init__(self, data: dict) -> None:
        """
        Initializes the APIParser with the provided raw API response.

        Args:
            data (dict): Raw JSON dictionary containing weather data.
        """
        self.data = data

    def parse_weather(self) -> list:
        """
        Extracts relevant weather information from the API response.

        Returns:
            dict: A list containing:
                - (float | None): Current temperature reading.
                - (float | None): Forecasted minimum temperature for the day.
                - (float | None): Forecasted maximum temperature for the day.
                - (str | None): Reference date for the forecast (typically today).
        """
        current = self.data.get('current_weather', {})
        daily = self.data.get('daily', {})
        return [
            current.get("temperature"),
            daily.get("temperature_2m_min", [None])[0],
            daily.get("temperature_2m_max", [None])[0],
            daily.get("time", [None])[0],
        ]
