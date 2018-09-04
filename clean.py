import pandas as pd
import numpy as np
import re
import matplotlib.pyplot as plt

# dataFrame : dataframe from pd
def analysis(dataFrame):
	"""Function that takes dataframe,
	and retrieves info
	used as a reference
	"""
	# columns types and memory 
	print(dataFrame.info())
	# num of rows and columns
	print(dataFrame.shape)
	# count, mean, std, min, 25%, 50%, 75%, max  
	print(dataFrame.describe())
	# columns names and types
	print(dataFrame.columns)
	# print few rows
	print(dataFrame.head())


# dataFrame: dataframe from pd
# column1 : str
# column2 : str
# label : str to show on plot
def plot(dataFrame, ptype='scatter', column1='', column2='', label='', xlimMin=0, xlimMax=10, ylimMin=0, ylimMax=10):
	"""Function takes a dataFrame and 2 columns names,
	creates scatter plot,
	and displays plot with the labels
	"""
	# check if columns exist in dataFrame
	assert column1 in dataFrame.columns
	if column2 != '':
		assert column2 in dataFrame.columns
	# Create the scatter plot
	if ptype == 'hist' or ptype == 'line':
		dataFrame[column1].plot(kind=ptype)

	elif ptype == 'scatter':
		dataFrame.plot(kind=ptype, x=column1, y=column2)
		plt.ylabel(label + ' ' + column2)
		plt.ylim(ylimMin, ylimMax)

	plt.xlabel(label + ' ' + column1)
	plt.xlim(xlimMin, xlimMax)

	# Display the plot
	plt.show()


# ignore : list of indices (only numbers)
def checkNull(row_data, ignore=[]):
    """Function that takes a row of data,
    drops all missing values
    """
    assert all(isinstance(x, int) for x in ignore)
    no_na = row_data
    for i in row_data.size():
    	if i not in ignore:
    		no_na = no_na.dropna()[i]
    return no_na


# remember to drop NaN before this
def removeOutliners(dataFrame, columnName, low=.5, high=.95):
	"""Function that takes a dataframe,
    drops all outliers
    """
	quant_df = dataFrame.quantile([low, high], numeric_only=True)
	print(quant_df)
	dataFrame = dataFrame[dataFrame[columnName] > quant_df.loc[low, columnName]] 
	dataFrame = dataFrame[dataFrame[columnName] < quant_df.loc[high, columnName]]
	return dataFrame



# ignore : list of indices (only numbers)
def checkValidNumericNoNull(row_data, ignore=[]):
    """Function that takes a row of data,
    drops all missing values,
    check if all not in ignore is numeric (if they are strings)
    """
    no_na = check_null(no_na, ignore)
    numeric = pd.to_numeric(no_na)
    return numeric >= 0


# tidy data
# four principles :
# 	1. Each variable you measure should be in one column.
#   2. Each different observation of that variable should be in a different row.
#   3. There should be one table for each "kind" of variable.
#   4. If you have multiple tables, they should include a column in the table that allows them to be linked.
# melt or pivot
# melting turns columns into rows
# pivot will take unique values from a column and create new columns

# when melting with one column fixed
# id_vars = 'column name'
# with value_vars
# id_vars = ['column name', ....]
# column : str
# columns_names : list of str
def meltOneColumnFixed(dataFrame, column, columns_names=[]):
	"""Function that takes a dataFrame, a fixed column and new columns names,
    melts the dataFrame
    """
	data_melt = pd.melt(dataFrame, id_vars=column)
	# Rename the columns
	if columns_names.size() == data_melt.columns.size():
		data_melt.columns = columns_names
	return data_melt


def subObjectWithNumeric(dataFrame):
	for i in dataFrame.columns:
		if dataFrame[i].dtypes == np.object:
			dataFrame[i] = pd.to_numeric(dataFrame[i])


# columnName : str
# pattern : regex
def uniqueWithPattern(dataFrame, columnName, pattern):
	column = dataFrame[columnName]
	column = column.drop_duplicates()
	mask = column.str.contains(pattern)
	#mask_inverse = ~mask
	return column.loc[mask]


def notNull(dataFrame, columns):
	for i in dataFrame.columns:
		if ~(pd.notnull(dataFrame[i]).all()):
			return False
	return True