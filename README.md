# Evolution of Internet Users

Scripts to pre-process data for creating the
[Evolution of Internet Users](http://exploringdata.github.io/vis/evolution-internet-users/) visualization.
The data is downloaded from the [Worldbank Databank](http://databank.worldbank.org/data/views/reports/tableview.aspx).

## Required Indicators

* x-axis: NY.GDP.PCAP.CD - GDP per capita (current US$)
* y-axis: IT.NET.USER.P2 - Internet users (per 100 people)
* bubble size: SP.POP.TOTL - Population, total

## Enhancements

* Automate download, currently a manual process
* Assign values in worldbank.py based on column names rather than indexes to support different column orders.
