# This program analyses Ronald Fisher's Iris data set
# It reads in the data frame and outputs a summary to a text file
# Then plots the analysis using histograms and scatterplots
# Author: Sarah McNelis

import numpy as np 
import matplotlib.pyplot as plt
import pandas as pd 
import seaborn as sns 


# Adjust settings for output display - 1 decimal place
pd.set_option('display.precision', 1)


# open data set 
filename = pd.read_csv('iris.csv')
df = pd.DataFrame(filename)
#print(df) #debug


# SUMMARY TO TXT FILE 
with open ('summary.txt', 'wt') as f:
    f.write('The Iris Dataset: Statistics Summary of all Species\n')
    print(df.describe(), file=f)                                    # gives brief analysis of all 
    f.write('\n\nCount of Different Species:\n')
    print(df['Species'].value_counts(), file=f)                     # counts number of species
    f.write('\n\nShape of Iris Dataset:\n')
    print(df.shape, file=f)                                         # prints shape of data set
    f.write('\n\nStatistical Summary of Iris Setosa:\n',)
    print(df[df['Species'] == 'setosa'].describe(), file=f)         # prints summary of setosa
    f.write('\n\nStatistical Summary of Iris Versicolor:\n')
    print(df[df['Species'] == 'versicolor'].describe(), file=f)     # prints summary of versicolor      
    f.write('\n\nStatistical Summary of Iris Virginica:\n')
    print(df[df['Species'] == 'virginica'].describe(), file=f)      # prints summary of virginica
    f.write('\n\nFirst 5 rows of the Iris Dataset:\n')
    print(df.head(5), file=f)                                       # prints top 5 rows
    f.write('\n\nLast 7 rows of the Iris Dataset:\n')
    print(df.tail(7), file=f)                                       # prints last 7 rows
    f.write('\n\nLast 4 Rows of Iris Setosa Species:\n')
    print(df[df['Species'] == 'setosa'].tail(4), file=f)            # prints last 4 rows of setosa
    f.write('\n\nFirst 6 Rows of Iris Versicolor Species:\n')
    print(df[df['Species'] == 'versicolor'].head(), file=f)         # prints top 6 rows of versicolor
    f.write('\n\nFirst 3 Rows of the Iris Virginica Species:\n')
    print(df[df['Species'] == 'virginica'].head(3), file=f)         # prints top 3 rows of virginica


# HISTOGRAMS

# Petal Length
def histPetalLength():
    plt.figure()
    sns.histplot(data=df, x='Petal Length', hue='Species', multiple='stack')
    plt.title('Petal Length in cm', size=14)
    plt.xlabel('Petal Length', size=11)
    plt.ylabel('Frequency', size=11)
    plt.savefig('histogramPetalLength.png')
    #plt.show() #debug

# Petal Width
def histPetalWidth():
    plt.figure()
    sns.histplot(data=df, x='Petal Width', hue='Species', multiple='stack')
    plt.title('Petal Width in cm', size=14)
    plt.xlabel('Petal Width', size=11)
    plt.ylabel('Frequency', size=11)
    plt.savefig('histogramPetalWidth.png')
    #plt.show() #debug

# Sepal Length
def histSepalLength():
    plt.figure()
    sns.histplot(data=df, x='Sepal Length', hue='Species', multiple='stack')
    plt.title('Sepal Length in cm', size=14)
    plt.xlabel('Sepal Length', size=11)
    plt.ylabel('Frequency', size=11)
    plt.savefig('histogramSepalLength.png')
    #plt.show() #debug

# Sepal Width
def histSepalWidth():
    plt.figure()
    sns.histplot(data=df, x='Sepal Width', hue='Species', multiple='stack')
    plt.title('Sepal Width in cm', size=14)
    plt.xlabel('Sepal Width', size=11)
    plt.ylabel('Frequency', size=11)
    plt.savefig('histogramSepalWidth.png')  
    #plt.show() #debug

# Call histogram functions here
histPetalLength()
histPetalWidth()
histSepalLength()
histSepalWidth()


# SCATTERPLOTS

# Petal Length vs Petal Width
def scatterPetalLength_PetalWidth():
    plt.figure()
    sns.scatterplot(x='Petal Length', y='Petal Width', data=df, hue='Species')
    plt.title('Petal Length vs Petal Width', size=16)
    plt.xlabel('Petal Length', size=12)
    plt.ylabel('Petal Width', size=12)
    plt.legend(loc='best')
    plt.savefig('scatterPetalLength_PetalWidth.png')
    #plt.show() #debug
    
# Sepal Length vs Sepal Width
def scatterSepalLength_SepalWidth():
    plt.figure()
    sns.scatterplot(x='Sepal Length', y='Sepal Width', data=df, hue='Species')
    plt.title('Sepal Length vs Sepal Width', size=16)
    plt.xlabel('Sepal Length', size=12)
    plt.ylabel('Sepal Width', size=12)
    plt.legend(loc='best')
    plt.savefig('scatterSepalLength_SepalWidth.png')
    #plt.show() #debug

# Petal Length vs Sepal Length
def scatterPetalLength_SepalLength():
    plt.figure()
    sns.scatterplot(x='Petal Length', y='Sepal Length', data=df, hue='Species')
    plt.title('Petal Length vs Sepal Length', size=16)
    plt.xlabel('Petal Length', size=12)
    plt.ylabel('Sepal Length', size=12)
    plt.legend(loc='best')
    plt.savefig('scatterPetalLength_SepalLength.png')
    #plt.show() #debug

# Sepal Width vs Petal Width
def scatterSepalWidth_PetalWidth():
    plt.figure()
    sns.scatterplot(x='Sepal Width', y='Petal Width', data=df, hue='Species')
    plt.title('Sepal Width vs Petal Width', size=16)
    plt.xlabel('Sepal Width', size=12)
    plt.ylabel('Petal Width', size=12)
    plt.legend(loc='best')
    plt.savefig('scatterSepalWidth_PetalWidth.png')
    #plt.show() #debug

# Petal Length vs Sepal Width
def scatterPetalLength_SepalWidth():
    plt.figure()
    sns.scatterplot(x='Petal Length', y='Sepal Width', data=df, hue='Species')
    plt.title('Petal Length vs Sepal Width', size=16)
    plt.xlabel('Petal Length', size=12)
    plt.ylabel('Sepal Width', size=12)
    plt.legend(loc='best')
    plt.savefig('scatterPetalLength_SepalWidth.png')
    #plt.show() #debug

# Sepal Length vs Petal Width
def scatterSepalLength_PetalWidth():
    plt.figure()
    sns.scatterplot(x='Sepal Length', y='Petal Width', data=df, hue='Species')
    plt.title('Sepal Length vs Petal Width', size=16)
    plt.xlabel('Sepal Length', size=12)
    plt.ylabel('Petal Width', size=12)
    plt.legend(loc='best')
    plt.savefig('scatterSepalLength_PetalWidth.png')
    #plt.show() #debug

# Call scatter functions here
scatterPetalLength_PetalWidth()
scatterSepalLength_SepalWidth()
scatterPetalLength_SepalLength()
scatterSepalWidth_PetalWidth()
scatterPetalLength_SepalWidth()
scatterSepalLength_PetalWidth()


# PAIRPLOT OF DATA SET
def dfPairplot():
    plt.figure()
    sns.pairplot(df, hue='Species',diag_kind='hist', height=1.5) 
    plt.savefig('pairplot.png')
    #plt.show() #debug

# Call pairplot function here
dfPairplot()
