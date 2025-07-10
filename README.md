# Weathergraph

Weathergraph is an ongoing project aimed at building a modular and scalable program to automate weather data retrieval, store data in `.xlsx` files, and generate charts from the historical data. Its architecture allows easy expansion towards a command-line interface (CLI), customizable configuration via `.toml` files, and scheduled execution through automation.

## Installation

### Prerequisites

#### System

- Python 3.11+
- Git

#### Python Dependencies

Install them with:

```bash
pip install -r requirements.txt
```

(It is recommended to use a virtual environment)

### Steps

1. Clone the repository:

   ```bash
   git clone https://github.com/Egid10p/Weathergraph.git
   cd Weathergraph
   ```

2. Configure preferences. Create the file `settings.toml` in `user_settings/settings.toml` with at least:

   ```toml
   [location]
   city    = "Asunción"
   country = "Paraguay"
   ```

3. Run the program:
   ```bash
   python main.py
   ```

## Basic Usage

Once installed and configured (see Installation section), using WeatherGrapher is as simple as running the main script:

```bash
python main.py
```

When executed:

- The location is loaded from `user_settings/settings.toml`.

- The weather API is queried to obtain the current day's data.

- Results are saved `data/data.xlsx`.

### Customization

- Modify `user_settings/settings.toml`to change city or country.

- Edit the path or filename in `DataSaver('data/data.xlsx')`.

- Import and reuse modules in your own scripts:

  ```python
  from weather_api.weather_connector import WeatherConnector
  from data_manager.data_saver import DataSaver

  prefs = {"city": "Roma", "country": "Italia"}
  loc   = f"{prefs['city']}, {prefs['country']}"
  data  = WeatherConnector().fetch_weather_data(loc)
  DataSaver("datos_roma.xlsx").save_data(data)
  ```

This minimal workflow lets you start collecting weather data and saving it without writing additional code. As the project evolves, CLI options, chart generation, and more features will be added.

## Project Structure

```text
Weathergraph/
├── main.py                   # Main program entry point
├── data/
│   └── data.xlsx             # Automatically generated Excel file with historical weather data
├── data_manager/
│   ├── data_saver.py         # Saves data in .xlsx files
│   └── data_getter.py        # Retrieves historical data
├── user_settings/
│   └── settings.toml         # User preferences and settings
├── utils/
│   ├── file_initializer.py   # Ensure that the specified file exists, creating it if it does not
│   ├── geo.py                # Returns coordinates based on city names
│   ├── load_preferences.py   # Loads preferences from user_settings/settings.toml
│   └── url_builder.py        # Builds URL for OpenMeteo API
├── weather_api/
│   ├── api_client.py         # Performs requests to the weather API
│   └── weather_connector.py  # Handles the usage of weather_api/api_client.py, utils/geo.py, and utils/url_builder.py
├── README.md                 # Project documentation
├── requirements.txt          # Project dependencies
```

## License

Weathergraph is licensed under the Apache 2.0 License.
For more information, see the [LICENSE](LICENSE) file.
