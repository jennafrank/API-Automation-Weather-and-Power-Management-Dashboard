<h1>API Automation – Weather and Power Management Dashboard</h1>

<h2>Description</h2>
<b>This project is a journey into the world of automation, APIs, and data visualization. The core of the project is a Python script that connects to the OpenWeatherMap API to fetch live weather data for Oklahoma City. Based on this weather data, the script suggests power management strategies, such as recommending increased AC usage when it's hot or suggesting heating when it's cold.</b>
<br /><br />
This project integrates automation through <b>cron jobs</b> to regularly fetch and log the weather data at intervals. It also includes an optional feature where the data is visualized using <b>matplotlib</b>, creating a dashboard that provides insights into temperature trends and power management recommendations over time.
<br /><br />

<h2>Languages Used</h2>
- <b>Python 3.x:</b> The primary language used for fetching weather data and implementing power management suggestions.

<h2>Utilities Used</h2>
- <b>OpenWeatherMap API:</b> Used to fetch live weather data for Oklahoma City.<br />
- <b>matplotlib:</b> Used for visualizing weather trends and power management suggestions.

<h2>Automated Data Logging and Visualization</h2>
- <b>CSV Logging:</b> Data is appended to <code>weather_log.csv</code> for long-term analysis.<br />
- <b>Graph Generation:</b> Temperature trends are plotted and saved as images (<code>weather_trend.png</code>).

<h2>Key Features</h2>
- <b>Fetch live weather data</b><br />
- <b>Generate power management recommendations</b><br />
- <b>Automate the script execution every 6 hours using cron</b><br />
- <b>Visualize data trends and power suggestions using matplotlib (optional)</b><br />

<h2>Project Overview</h2>
- <b>Setup:</b> Install Python and the required libraries (<code>requests</code>, <code>matplotlib</code>). Set up the OpenWeatherMap API key and configure the Python script.<br />
- <b>Automation:</b> Use cron (macOS/Linux) to schedule the script to run every 6 hours, logging weather data and power management suggestions.<br />
- <b>Data Logging:</b> Save the fetched weather data and power suggestions to a CSV file for future analysis.<br />
- <b>Data Visualization:</b> Use matplotlib to generate and save graphs visualizing the temperature trends and power management decisions over time.<br />

<h2>Installation</h2>
- <b>Clone the Repository:</b><br />
<code>git clone https://github.com/yourusername/weather-power-dashboard.git</code><br />
<code>cd weather-power-dashboard</code><br /><br />
- <b>Install Requirements:</b><br />
<code>pip install requests matplotlib</code><br /><br />
- <b>Insert Your API Key:</b><br />
Open the script and replace <code>YOUR_API_KEY_HERE</code> with your actual OpenWeatherMap API key.<br /><br />
- <b>Schedule with cron:</b><br />
Use <code>crontab -e</code> and add:<br />
<code>0 */6 * * * /usr/bin/python3 /path/to/weather_power_dashboard.py</code><br />

<h2>Example Output</h2>
- <code>weather_log.csv</code> – Time-stamped log of temperature, weather description, and suggestions<br />
- <code>weather_trend.png</code> – Line chart showing temperature trends<br />

<h2>Contributors</h2>
- <b>Jenna Frank</b><br />

<h2>License</h2>
- MIT License

