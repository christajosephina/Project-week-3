# Project-week-3
NOTE: the story has not been updated regarding to last week.


In the Netherlands, the law regarding organ donation recently changed (July 2020). 
While it used to be: “you are not a donor, unless you register to be one”, it has 
now become “You are a donor, unless you register to not be one.” When registering 
for organ donation in the system, you can also choose to only donate certain organs 
or to let your relatives decide after you pass away.

I would like to see if there are certain people who are more likely to choose to not 
donate organs. A comparison over time could also be interesting in this sense, since 
the law recently changed.

The Dutch central office of statistics (CBS) keeps this data.

First, I downloaded the raw data from https://opendata.cbs.nl/#/CBS/nl/dataset/82814NED/table , 
importing the cvs into spreadsheets and converting it to columns. This dataset displays 
different demographics of Dutch civilians and how they are registered in the donor 
register (donor, non-donor, partly donor). It gives information such as age group, 
gender, migratory background. I cleaned the data by getting rid of excess white columns 
and by renaming them with English terms.

When I wrote the story last week, I made four graphs in excel focused on the comparison between
non-western migrants and Dutch natives. Because it was unclear how the amount of people who are 
part of this group over time had changed from just graphing the numbers I calculated the group 
size for each year and the percentages corresponding to these years. 

For this week's project, I opened up the excel file in a Jupyter Notebook. I noticed the data
was not being displayed correctly, so I went into the excel file to get rid of extra white
columns as well as information that was not needed (but was being read wrongly, such as a 
row with information on who is the source). I then tried to create the same graphs on percentages
as I did last week. 

I chose specifically to not show natives and non-western migrants in the same chart, because both 
charts already included three different variables (donor, non-donor, partly donor). I thought this 
would be too confusing if combined. This is also visible in the python file, were I tried to 
create the chart with all the lines included. Instead, I made a graph for only 'no permission'.
Next to this, I proceeded to create to graphs for 1st and 2nd generation immigrants. There's a 
limitationhere: it is not clear which share of these immigrants is western/non-western.
