# -*- coding: utf-8 -*-
"""
Created on Sun Mar  5 20:32:24 2023

@author: Caleb Vite Justice
"""

# Importing the library modules for this project
import pandas as pd
import matplotlib.pyplot as plt

# DATA PREPARATION
# Reading the excel file using pandas
df_imdb = pd.read_excel("IMDB Top 250 Movies.xlsx")

# Like every other dataframe, the index starts from 0
# In this case I decided to set the Rank column as the index of the dataframe
df_imdb = df_imdb.set_index('rank')

# Getting info about the dataframe
print(df_imdb.info())

# Notice not all columns have 250 enteries, so we'll be dropping them
df_imdb.isna().sum()  # to know how many rows we'll be dropping
df_imdb = df_imdb.dropna()  # Dropping rows with existing Nan values

# Steps before the line plot
"""
A for loop to go through every row in the genre column
and putting it into a list...
the second loop through that list, comparing it to
the items in the genre column and appending it
"""
genr = ""
for i in df_imdb['genre']:
    genr = genr + "," + i
all_genre = genr.split(',')[1:]
unique_genres = list(set(all_genre))

data = []
for i in unique_genres:
    c = 0
    for j in df_imdb['genre']:
        if i in j:
            c += 1
    data.append([i, c])

# Creating a sub-data frame to make every genre mentioned unique
gen_df = pd.DataFrame(data, columns=['Genre', 'Frequency'])
gen_df.sort_values(by='Frequency', ascending=False, inplace=True)
gen_df = gen_df.head(10)  # Only interested in the top 10 most popular genres

# Setting the figure style before plotting
plt.style.use('fivethirtyeight')


# Line Plot function for the top 10 genres
def ln_gnr(x, y, label):
    """
    Creates a variable line plot

    Conditions
    -----------------------
    x : List or array,
    contains indexed x-axis points.
    y : array or list Plot values for the y-axis are contained here.
    label: string The name of the specific plotted array or list.

    Returns
    ------------------------
    fig_ln: line 2D figures
    a collection of lines depicting the data plotted.
    """
    fig_ln = plt.figure(figsize=(15, 9))
    plt.plot(x, y, label=var1)
    plt.title('Top 10 Most Popular Genres')
    plt.xlabel("Genres")
    plt.ylabel("Frequency")
    plt.legend()
    plt.show()
    return fig_ln


var1 = "Frequency Difference"
ln_gnr(gen_df['Genre'], gen_df['Frequency'], label=var1)


# Bar Plot function for the top 10 Movie Certfications
def bar_crt(a):
    """
    Creates a bar plot chart of sorted values

    Conditions
    -----------------------
    a : List or array,
    contains indexed x-axis points.

    Returns
    ------------------------
    fig_bar: A bar chart
    a collection of bars depicting the data plotted.
    """
    fig_bar = plt.figure(figsize=(14, 7))
    a.size().sort_values(ascending=False).head(10).plot(kind='bar')
    plt.xlabel('Certificate')
    plt.ylabel('Frequency')
    plt.title("Top 10 Certificates")
    plt.show()
    return fig_bar


bar_crt(df_imdb.groupby('certificate'))


# Pie Plot function for Top Movies produced within 20 Years Time-frame
def pie_yr(u, labels):
    """
    Creates a pie chart of percentage values

    Conditions
    -----------------------
    u : List or array,
    contains indexed x-axis points.

    Returns
    ------------------------
    fig_bar: A bar chart
    a collection of bars depicting the data plotted.
    """
    fig_pie = plt.figure(figsize=(12, 6))
    plt.pie(u, labels=label, autopct='%.2f%%')
    plt.title("Percentage of Movies within 20 Years Time-Frame")
    plt.show()
    return fig_pie


# Creating an empty list in order to loop through the year column
# and fitting it into the list to create a pie chart.
a = 0
b = 0
c = 0
d = 0
e = 0

for i in df_imdb['year']:
    if i > 1920 and i <= 1940:
        a += 1
    elif i > 1940 and i <= 1960:
        b += 1
    elif i > 1960 and i <= 1980:
        c += 1
    elif i > 1980 and i <= 2000:
        d += 1
    else:
        e += 1

data = [a, b, c, d, e]
label = ['1920 - 1940', '1941- 1960',
         '1961 - 1980', '1981 - 2000', '2001 - 2022']
pie_yr(u=data, labels=label)


# The Scatter Plot function for multiple use
def sca_yr(par, title_lab, y_lab):
    """
    A set of dots plotted on a horizontal and vertical axis.
    Conditions
    -----------------------
    par : List or array,
    contains indexed y-axis points.
    title_lab : The title label
    The string given as the title
    y_lab : The y label
    The string given to the y-axis

    Returns
    ------------------------
    fig: A scatter plot
    """
    fig = plt.figure(figsize=(12, 6))
    plt.scatter(df_imdb['year'], par)

    # Add labels and title
    plt.title(title_lab)
    plt.xlabel("Year")
    plt.ylabel(y_lab)

    # Show the plot
    plt.show()
    return fig


# For the Movie Duration plot
title_lab = "Movie Duration by Release Year"
y_lab = "Duration(min)"
sca_yr(df_imdb['run_time(ms)'], title_lab, y_lab)


# For the Top Grossing movies plot
title_lab = "Top Grossing Movies"
y_lab = "Box Office Revenue (in billions of dollars)"
sca_yr(df_imdb['box_office'], title_lab, y_lab)
