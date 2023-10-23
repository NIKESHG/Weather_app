# Weather App

### Software and Tools Requirments

1. [Github Account](https://github.com)
2. [VS CODE IDE](https://code.visualstudio.com)
3. [Git CLI](https://git-scm.com/downloads)


Create a new environment

----------------------------------------------------------------

conda create -p venv python==3.10 -y

----------------------------------------------------------------

## Overview

#### This is a simple Weather App built using Python and the Tkinter library for the GUI. It provides weather information for a given city, including temperature, wind speed, humidity, and more. Additionally, it displays sunrise and sunset times along with the current time in the selected location.

## Screenshot

Outpt 1 [Weather_app.py]

![Capture1](https://github.com/NIKESHG/Weather_app/assets/106954184/106c6cfc-c77b-40d5-b2f2-69d7f17a5eb0)

Outpt 2 [Weatherapp.py]

![Capture](https://github.com/NIKESHG/Weather_app/assets/106954184/96966a19-a4b3-46c6-a6c0-fac1f2f842f5)

## Table of Contents

• Prerequisites

• How It Works

• How to Use

• Deployment on GitHub

• Explanation of the Code

• Closing the App

## Prerequisites

To run this application, you'll need the following installed:

• Python 3.x

• Tkinter (Tkinter is installed included with Python by default.)

• PIL (Python Imaging Library)

• Geopy

• Timezonefinder

• Requests

## How It Works

1. Location Search: Enter the name of a city in the search box and click the search button (or press Enter) to search for weather information.

2. Display: The app will display the following information:

        • Location name and coordinates.

        • Local time.

        • Weather condition, temperature, humidity, wind speed, and more.

        • Sunrise and sunset times.

3. Reset: Press the Backspace key to clear the displayed weather data.

## Usage

• Run the Python script.

• Enter the name of the city you want to get weather information for in the provided input box.

• Press Enter or click the search icon.

•The app will display the weather information for the specified city.

## How to Use

1. Clone the repository to your local machine:

   ![github](https://github.com/NIKESHG/Weather_app/assets/106954184/2a3b1837-d7a6-48e6-bc93-ea6943b6fcf8)
   
2. Install the required Python packages:
   
   ![github1](https://github.com/NIKESHG/Weather_app/assets/106954184/a33811bb-6f16-4b3a-8be4-680defb3be25)

3. Run the Weather App:
   
   ![github2](https://github.com/NIKESHG/Weather_app/assets/106954184/989f3e80-d92a-4441-8d5b-6cad0f7159a0)

4. Enter the city name in the search box and press Enter or click the search button to get weather information.

## Deployment on GitHub

To deploy this project on GitHub, follow these steps:

1. Create a GitHub repository for your project.

2. Commit your code to the repository:
   
   ![github3](https://github.com/NIKESHG/Weather_app/assets/106954184/d3212d4e-dadf-4386-8d3a-283ac6da9e77)

3. You can now access your Weather App on GitHub at https://github.com/yourusername/weather-app.



## Code Explanation

• The code is written in Python and uses Tkinter for the GUI, Geopy for geocoding, and OpenWeatherMap API for weather information.

• The app displays a window with an input box to enter the city name, a search button, and various labels to display weather information.

• It also fetches and displays the background image for aesthetics.


## Closing the App

To close the app, simply click the close button (X) on the top-right corner of the window.

## Contributing

If you'd like to contribute to this project, feel free to fork the repository and submit a pull request. You can also open an issue if you find any bugs or have suggestions for improvements.

## License

This project is licensed under the Apache License 2.0 - see the LICENSE file for details.