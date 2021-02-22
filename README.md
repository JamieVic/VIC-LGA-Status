# VIC-LGA-Status
## About the Project
The Victorian government have introduced a travel permit system to coincide with the COVID-19 situation in Australia. Basically, everyone entering Victoria must have a permit otherwise they cannot enter the state. Eligibility is determined on which local government area you're coming from.
Some people may find systems like this rather confusing because of social media and the news sometimes providing conflicting information. Others may even find government jargon outright confusing. This project aims to eliminate the confusing details and give you the information you need, which is if you're allowed to enter Victoria or not, and what you may need to do upon entry.
## How to Use
The program can be initialised in any Python interpreter. Enter the name of the LGA you're coming from into the input field and hit Enter. The program will use the data in the CSV file, provided by the Victorian government, to determine the permit status of that LGA.
## How it Works
Combining the CSV and urllib libraries, the Excel spreadsheet available on the Coronavirus Victoria website is able to be read. The spreadsheet is stored in the url variable, which is then opened in the response variable using the urllib.request.urlopen() function. Once the CSV page is opened, the lines variable stores the data once the page is decoded to UTF-8 to ensure the data can be read. The zoneReader variable now holds what the program needs which is the entire CSV page opened, decoded to UTF-8 and each value in that CSV file seperated by a comma.

For user input, the lga variable asks the user to enter the name of a LGA. It is then stored in the lga variable and is converted to capitalize only the first letter of the string using the .capitalize() string method. A for loop is ran after the user hits Enter and the loop cycles through the CSV file to find the value of the lga variable and produce one of the four results provided in the if/else statements.
