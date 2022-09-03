## Sample Output

You can view the result as shown below when you execute the [main.py](main.py) file on your device.

```
Welcome to the CO2 Emission Data Analysis (1997-2010, 195 countries). There are four questions that print data, provide a summary of given year, visualize data for given countries (in Matplotlib), and save data in separate file for given countries.

--------------------------------------------------

Do you want to view the data? (y/n): n

--------------------------------------------------

Enter a year to view its summary (1997 to 2010): 2022
-> No data are available for 2022...

Enter a year to view its summary (1997 to 2010): two thousand eleven
-> Invalid year...

Enter a year to view its summary (1997 to 2010): 1997

=> In 1997, countries with minimum and maximum CO2 emission levels were, Chad and Qatar respectively. The average CO2 emissions in 1997 were 4.96.

--------------------------------------------------

Enter the 'comma-separated' countries for which you want to visualize data: ind, pak
-> Data for Ind is not available. Each name should be typed again...

Enter the 'comma-separated' countries for which you want to visualize data: india, pak
-> Data for Pak is not available. Each name should be typed again...

Enter the 'comma-separated' countries for which you want to visualize data: india, pakistan
```

![image](https://user-images.githubusercontent.com/108747654/188279759-6ec19f79-f711-4ca8-8d69-e23c20b94672.png)

```
--------------------------------------------------

Enter the 'comma-separated' coutries for which you want to extract data: ind, china
-> Data for Ind is not available. Each name should be typed again...

Enter the 'comma-separated' coutries for which you want to extract data: india, chin
-> Data for Chin is not available. Each name should be typed again...

Enter the 'comma-separated' coutries for which you want to extract data: india, china
Data added in file named, 'Emissions_subset.csv'

--------------------------------------------------

<"Thank You. Enjoy your day. :)"/>
```

Go to [Repository](https://github.com/chiragkumargohil/co2-emissions-data-analysis.git).
