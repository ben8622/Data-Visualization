Created by Benjamin Knight
https://github.com/ben8622

DESC:
~~~~~~~~~~~~~~~~~~~~
IMPORTANT NOTE:
Require to have wkhtml downloaded to convert your DataFrames into .jpg files.
The excel files you use for this must be structured in the same way as the one provided
which is a single column of data, per sheet, with first cell of the column being the 
title of the data, an example would be:

Data Title
data[1]
data[2]
.
.
.
data[n]

This project was my introduction to data visualization with python. Here we use
python to create a visualization of data sets that we went out and collected on
our own. I saved some of my images as .jpg and others as .png. There's no rhyme or 
reason for it, I was just seeing the capabilties of these modules. Many things are 
hardcoded as because they will change on account of what your data is. 

Some examples of things that are hardcoded are:
-The names of the excel sheets holding data
-# of bins we want for each histogram
-histogram stylizing
-etc

The pandas module is used for its DataFrame data structure. This was an extreme overkill for these very simple sets
of data, however, I wanted to understand how they work, the functions that can
be used on them, and how they are structured. A pandas Series data structure would suit 
these data sets better, but they are simpler to understand and where's the fun in that?

The numpy module is used mainly for numpy arrays. These array have an amazing amount of 
complex methods that can be done on them. Here we use numpy to generate arrays
from our DataFrame objects. These arrays are then used as the values for our
histogram and its bin edges.

The matplotlib module is used for the creation of of our boxplots and histograms. I'd love
to explore the much more complicated visualizations you can do with it, but we were only using
univariate sets of data for this project. We also save these plots into our imgs files so we
can easily use them in our project report. Matplotlib makes the saving of plots EXTREMELY easy.

The imgkit module was used to export our dataframes as .jpg files so we can use them
in a practical manner. First we export the data into an html file with whatever css 
styling we want to be done on the table. Then imgkit will use wkhtmltoimg.exe to easily 
convert these files into .jpg. I followed this tutorial and used their css styling
for my tables we one or two tweaks of my own:
https://medium.com/@andy.lane/convert-pandas-dataframes-to-images-using-imgkit-5da7e5108d55

~~~~~~~~~~~~~~~~~~~~

ABSTRACT FLOW:
1.)Import .xlsx file with pd.ExcelFile()
2.)Parse each sheet of the excel file into a seperate DataFrame with .parse()

3.)Create a 2D numpy array using each of the data sets (this was because we wanted
both of our data sets on the same graph for boxplots)
4.)Use the numpy array to create boxplots with .boxplot()
5.)Stylize
6.)Save it as a .png

7.)Create 2 seperate numpy arrays with a single DataFrame
8.)Use these numpy arrays to create a bar graph with matplotlib.bar()
9.)Stylize
10.)Save it as a .png
11.)Repeat steps 7-10 for our other data set

12.)Create frequency tables from each data set with a pre-determined range size, for us we counted in 2s

13.)Convert a DataFrame you want as .jpg into .html files along with the CSS styling
14.)Convert these .html files into .jpgs with imgkit.from_file()
15.)Repeat 13-14 for all DataFrames you need


