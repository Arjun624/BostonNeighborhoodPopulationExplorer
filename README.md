# Arjun's 2023 Bostonography Final Project: **A Boston Neighborhood Population Explorer!**

---

## Project Overview:

For my final project, I endeavored to develop a comprehensive tool that empowers users to compare and analyze the
evolution of major neighborhoods in Boston over time. Beyond simply examining the overall population, my project delves
deeper by incorporating a wide range of comparison data that goes beyond total population. Specifically, users can
extract data on specific races, age groups, and education levels for a given year and neighborhood, allowing for more
nuanced and targeted analysis.

With my project, users can explore a wealth of data and answer a wide range of questions about the changing population
dynamics of Boston neighborhoods. For example, the tool can help to uncover the correlation between education rates and
race - a relationship that is heavily correlated. It can also reveal details such as how the Asian population in
Chinatown has evolved over time or the most popular age group living in a neighborhood during a specified year. The
possibilities for exploration and analysis are endless, as the project utilizes an abundance of data to empower users to
find critical insights and answers to a wide range of questions about Boston's neighborhoods.

---

## Project Data Information

All data is taken within the year range of ***1950 - 2000***.

The neighborhoods that are implemented are:

- Allston
- Back Bay
- Beacon Hill
- Downtown/Chinatown
- Fenway
- Mission Hill
- North End
- Roxbury

The population data categories that are implemented are:

- Total Population
- Population split by Age
- Population split by Race
- Population split by Education

For age, the specific age groups implemented are:

- Age 0-9
- Age 10-19
- Age 20-34
- Age 35-54
- Age 55-64
- Age 65+

For race, the specific race groups implemented are:

- White
- Black/African American
- Hispanic
- Asian
- Other

For education, the specific education groups implemented are:

- Less than High School
- High School/GED
- Some College
- Bachelor's Degree

All data was found
on: https://data.boston.gov/dataset/neighborhood-demographics/resource/7154cc09-55c4-4acd-99a5-3a233d11e699

I manually converted the Excel data into a JSON format, so I could easily use it for my program.

The JSON data file is over **1000** lines long, and there is so much useful and interesting data to
pick and compare from!

---

## Project Usage:

The usage of the program is pretty straightforward, but the user can choose two neighborhoods, their respective years,
the respective categories (and group if not total population) and the program will display the data for the chosen
options, and will also provide some additional information like the difference, the percent difference and the percent
change.

For example, if I want to compare how the population of Chinatown is changing over time I would pick:

    Neighborhood1: Chinatown | Year1: 1950 | Catagory: Total
    Neighborhood2: Chinatown | Year2: 2000 | Catagory: Total

And this would give me information about the Chinatown population in 1950 and the Chinatown population in 2000
and also tell me the difference between the two, the percent difference and the percent change.

Note that this is just one possibility of a usage case and there are thousands of different comparison possabilities to
pick and
try.

---

## Technical Details and Project difficulties

I used Python to code this project using the Pycharm IDE. I used the tkinter Python library for my user interface. I am
not really family with tkinter nor have I used it before, so part of my struggle with this project was just learning how
to use the library and learning the different syntax and how to use each method. The main struggle I had with this
program is the creation of my JSON file that my program uses to fetch data. The place where I found my data (linked
above)
only had the data in Excel format, so I was forced to manually create the json myself. This wasn't a very difficult
process,
but just was very tedious and time-consuming as there was so much data to convert for all the specific neighborhoods,
years, categories and groups. The JSON file is currently 1170 lines with 8 neighborhoods, but I might add more in the
future.
It took me a while, but was definably worth it as there is so much data to explore now!


    
    