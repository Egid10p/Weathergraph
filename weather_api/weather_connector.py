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

from weather_api.api_client import APIParser, APIRequester
from utils.geo import CoordinatesGetter
from utils.url_builder import build_openmeteo_url

class WeatherConnector:
    """
    Coordinates the components required to perform a weather API request using Open-Meteo.

    This class serves as the orchestration layer for the full process:
    obtaining geographic coordinates, building the query URL, executing the HTTP request,
    and parsing the response data into a structured format.

    Attributes:
        coordinates_getter (CoordinatesGetter): Utility for retrieving latitude and longitude from a location name.
        url_builder (Callable[[float, float], str]): Function to construct the API query URL from coordinates.
    """

    def __init__(self) -> None:
        """
        Initializes the WeatherConnector with all required dependencies.

        Instantiates the components responsible for geolocation, URL construction,
        API requesting, and response parsing.
        """
        self.coordinates_getter = CoordinatesGetter()
        self.url_builder = build_openmeteo_url

    def fetch_weather_data(self, location: str) -> list:
        """
        Retrieves weather data for a given location name.

        This method handles the full request flow:
        - Geocoding the location to coordinates
        - Building the request URL
        - Fetching data from the Open-Meteo API
        - Parsing and returning the structured result

        Args:
            location (str): Name of the location (e.g., "Asunción", "Berlin", "New York").

        Returns:
            dict[str, float | str]: Parsed weather data including:
                - 'current_temperature' (float)
                - 'daily_min_temperature' (float)
                - 'daily_max_temperature' (float)
                - 'date' (str)

        Raises:
            ValueError: If the geolocation fails or the API request/response is invalid.
        """
        lat, lon = self.coordinates_getter.get_coordinates(location)
        url = self.url_builder(lat, lon)

        requester = APIRequester(url)
        raw_data = requester.get_data()

        parser = APIParser(raw_data)
        return parser.parse_weather()
