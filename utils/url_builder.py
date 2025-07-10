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

from urllib.parse import urlencode


def build_openmeteo_url(lat: float, lon: float) -> str:
    """
    Construct a fully parameterized Open-Meteo API endpoint URL.

    This utility function encodes the latitude, longitude, and fixed query
    parameters needed to retrieve current weather plus daily minimum and
    maximum temperatures, and returns the complete URL string.

    Args:
        lat (float): Geographic latitude in decimal degrees.
        lon (float): Geographic longitude in decimal degrees.

    Returns:
        str: A URL pointing to the Open-Meteo forecast endpoint with all
             query parameters properly URL-encoded.

    Example:
        >>> url = build_openmeteo_url( -25.5167, -54.6167 )
        >>> print(url)
        https://api.open-meteo.com/v1/forecast?latitude=-25.5167&longitude=-54.6167&current_weather=true&daily=temperature_2m_min%2Ctemperature_2m_max&timezone=auto
    """
    params = {
        'latitude': lat,
        'longitude': lon,
        'current_weather': 'true',
        'daily': 'temperature_2m_min,temperature_2m_max',
        'timezone': 'auto'
    }
    return f"https://api.open-meteo.com/v1/forecast?{urlencode(params)}"
