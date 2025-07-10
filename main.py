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

from weather_api.weather_connector import WeatherConnector
from data_manager.data_saver import DataSaver
from data_manager.data_getter import DataGetter
from utils.load_preferences import PreferencesLoader



def main():
    # Load user preferences
    preferences = PreferencesLoader().load_location_preferences()
    location = f"{preferences['city']}, {preferences['country']}"
    # Initialize the weather connector with user preferences
    weather_connector = WeatherConnector()
       

    # Fetch weather data
    weather_data = weather_connector.fetch_weather_data(location)

    # Save the fetched data
    data_saver = DataSaver('data/data.xlsx')
    data_saver.save_data(weather_data)
    
    
if __name__ == "__main__":
    main()