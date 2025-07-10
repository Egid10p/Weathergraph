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

from geopy.geocoders import Nominatim


class CoordinatesGetter:
    """
    Retrieve latitude and longitude for a given place name via Nominatim.

    This class wraps the Geopy Nominatim geocoder to convert free-form
    location strings (in any supported language or script) into precise
    geographic coordinates.

    Attributes:
        geolocator (Nominatim): Geopy Nominatim instance configured with a
                                 custom user_agent for rate-limit compliance.
    """

    def __init__(self) -> None:
        """
        Initialize the CoordinatesGetter with a Nominatim geolocator.

        The `user_agent` parameter is required by the Nominatim service
        to identify your application and must be unique per application.
        """
        self.geolocator = Nominatim(user_agent="weathergraph-geocoder")

    def get_coordinates(self, location: str) -> tuple[float, float]:
        """
        Geocode a location string into (latitude, longitude).

        Args:
            location (str): A place name or address. Can be in any language
                            or local script (e.g., "Москва", "Ciudad del Este").

        Returns:
            tuple[float, float]: A tuple containing (latitude, longitude)
                                 in decimal degrees.

        Raises:
            ValueError: If the geocoder cannot resolve the provided location.
        """
        result = self.geolocator.geocode(location)
        if result:
            return result.latitude, result.longitude # type: ignore
        raise ValueError(f"Location not found: {location}")
