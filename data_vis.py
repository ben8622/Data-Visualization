import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import imgkit

# paths where we are storing files
html_path = r"C:\Users\Ben Knight\Desktop\python\IE3301_project\html"
imgs_path = r"C:\Users\Ben Knight\Desktop\python\IE3301_project\imgs"


def find_freq(min_range, df):
    
    freq = 0
    
    for x in range(df.size):
        if(df.iloc[x][0] >= min_range) and (df.iloc[x][0] < (min_range + 2)):
            freq += 1

    return freq

def create_tbl(max_range, df):
        
    tbl = [[0 for x in range(2)] for x in range(int(max_range/2))]
        
    # initialize the ranges
    for x in range(0, int(max_range/2), +1):
        tbl[x][0] = x*2
        
    # find each range's frequencies
    for x in range(0, int(max_range/2), +1):
        tbl[x][1] = find_freq(tbl[x][0], df)
        
    return tbl

def df_to_hist(df, bins, color, xlabel, title, out_path):
    hist,bin_edges = np.histogram(df, bins = bins)
    fig = plt.figure(figsize=[10,8])
    plt.bar(bin_edges[:-1], hist, width = 1, color=color,alpha=0.7)
    plt.xlim(min(bin_edges), max(bin_edges))
    plt.grid(axis='y', alpha=0.75)
    
    # Stylizing
    plt.xlabel( xlabel ,fontsize=15)
    plt.ylabel( 'Frequency' ,fontsize=15)
    plt.xticks(fontsize=15)
    plt.yticks(fontsize=15)
    plt.title( title ,fontsize=15)
    plt.show()
    
    # Saving it to a .png file
    fig.savefig( imgs_path + out_path, bbox_inches = 'tight')

def df_to_img(input_name, df, output_name):
    
    # css used to stylized our HTML-ized dataframes
    css = """
        <style type=\"text/css\">
        table {
        color: #333;
        font-family: Helvetica, Arial, sans-serif;
        width: 640px;
        border-collapse:
        collapse; 
        border-spacing: 0;
        }
        td, th {
        border: 1px solid transparent; /* No more visible border */
        height: 30px;
        }
        th {
        background: #DFDFDF; /* Darken header a bit */
        text-align: center;
        font-weight: bold;
        }
        td {
        background: #FAFAFA;
        text-align: center;
        }
        table tr:nth-child(odd) td{
        background-color: white;
        }
        </style>
        """
        
    # Writing the dataframe with css to an html file
    text_file = open(input_name, "w")
    # write the CSS
    text_file.write(css)
    # write the HTML-ized Pandas DataFrame
    text_file.write(df.to_html())
    text_file.close()
    
    # Setting our path variable so imgkit can find wkhtmltoimg executable
    path_wkthmltoimage = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltoimage.exe'
    config = imgkit.config(wkhtmltoimage=path_wkthmltoimage)
    
    options = {
    'log-level': 'none'
    }
    
    imgkit.from_file(input_name, output_name, config = config, options = options)

# PARSING DATA           
##############################################################################
file = 'data.xlsx'

data = pd.ExcelFile(file)

# Parsing the data from each sheet within the excel file into a data frame
grape_df = data.parse('Grape_Weight')
time_df = data.parse('Time_Spent')

# BOXPLOTS
##############################################################################
# We put both of our sets of data into a 2D numpy array
both_numpy = [grape_df.to_numpy(), time_df.to_numpy()]

# Some stylizing of the graph
colors = ['#deb0ff', '#c9ffca']
labels = ['Grape Data (g)', 'Time Data(mins)']

# Creating the boxplots
fig1 = plt.figure(1, figsize=(5, 5))
ax_g = fig1.add_subplot(111)
bp = ax_g.boxplot(both_numpy,
                    notch = True,
                    vert = True,
                    patch_artist = True,
                    labels = labels)

# Giving each boxplot it's own pre-determined color
for box in bp:
    for patch, color in zip(bp['boxes'], colors):
        patch.set_facecolor(color)
        
ax_g.set_title('Box Plots of Both Data Sets')
ax_g.set_ylabel('Observed Values')

# Saving it to a .png file
fig1.savefig( imgs_path  + '\\box_plots.png', 
             bbox_inches = 'tight')

# FREQUENCY HISTOGRAMS
##############################################################################
# We are using numpy's .histogram() to create the data for the graphs and then
# plotting said data with matplotlib's .bar() method
df_to_hist(grape_df, 
           20, 
           '#c97dff', 
           'Mass (g)', 
           'Frequency Histogram of Grape\'s Mass', 
           '\\grape_hist.png' )
df_to_hist(time_df, 
           28, 
           '#6bff6e', 
           'Time (mins)', 
           'Frequency Histogram of the Length of People\'s Trips at QT', 
           '\\time_hist.png' )

# FREQ TABLES
##############################################################################
# We're hardcoding this for now due to lack of time, these are our upper limits
# of the frequency tables and is the same # as our bins for their respective
# histogram which we determine by looking for the closest even number that is 
# greater than our max.
max_g = 20
max_t = 28

freq_tbl_g = pd.DataFrame(create_tbl(max_g, grape_df), 
                          columns = ['Range, [x[i] - x[i+1])' , 'Frequency'])
freq_tbl_t = pd.DataFrame(create_tbl(max_t, time_df), 
                          columns = ['Range, [x[i] - x[i+1])' , 'Frequency'])

# CREATING IMGS FROM DATAFRAMES
##############################################################################
# creating .jpgs of main data sets
df_to_img(html_path + "\\grape_df.html", 
          grape_df, 
          imgs_path + "\\grape_df.jpg")
df_to_img(html_path + "\\time_df.html", 
          time_df, imgs_path + "\\time_df.jpg")

# creating .jpgs of frequency tables
df_to_img(html_path + "\\grape_freq.html", 
          freq_tbl_g, imgs_path + "\\grape_freq.jpg")
df_to_img(html_path + "\\time_freq.html", 
          freq_tbl_t, imgs_path + "\\time_freq.jpg")

# creating .jpgs of statistics on data sets
df_to_img(html_path + "\\grape_stats.html", 
          grape_df.describe().transpose(), imgs_path + "\\grape_stats.jpg")
df_to_img(html_path + "\\time_stats.html", 
          time_df.describe().transpose(), imgs_path + "\\time_stats.jpg")


