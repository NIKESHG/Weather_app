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

## Prerequisites
To run this application, you'll need the following installed:

• Python 3.x

• Tkinter (Tkinter is installed included with Python by default.)

• PIL (Python Imaging Library)

• Geopy

• Timezonefinder

• Requests

### You can install these dependencies using pip:

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