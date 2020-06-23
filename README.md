# DGS Code Jam!
This repository holds the instructions and submissions for DGS Code Jam, an internal coding competition designed to improve Python fluency across the Department of General Services. 

## Fiscal Year Function  

### What your function should do
Here at DGS, the data usually comes to us with the calendar year. But for accounting and billing purposes, what we often really need is the fiscal year. Transforming the calendar year to the fiscal isn't too hard: if the date if after June 30, then we just add 1 to the year. 

The idea is to write a function that takes in as input a Pandas DataFrame where at least one column has date info. Your function should add a column to the Pandas dataframe that tells us what fiscal year the datetime column is in. 

A reasonable format for this kind of function would be 

	def add_fiscal_year(df, date_col):

Where `df` is the input dataframe and `date_col` is the name of the column in that dataframe that needs to get tranformed to a fiscal year. 

A couple of things to note: 

- __The new column should be called `fiscal_year` and its data type should be integer__. So just a number, like 2019.

- __Your function should be able to handle an input where the date column is a string__. You'll want to check the data type of that column and "cast" it to a `datetime` if it isn't already in that format. (You can find a few suggestions on how to do this [here](https://stackoverflow.com/questions/32204631/how-to-convert-string-to-datetime-format-in-pandas-python)).

- __Your function should throw a meaningful error if the input is bad__. What if the user passes in a `date_col` that just can't be converted to a date? Make sure your function provides the user a helpful error.

- __Your function contain a complete docstring__. You can see [this page](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html) for example docstrings. You'll want a sentence explaining what the docstring does, and then a description of the inputs (Args) and output (Returns). 

### How to get started
Since we haven't all installed Python locally on our machines, the easiest thing is to visit [Google Colab](https://colab.research.google.com/) and fire up a new notebook. So you'll be in the exact same browser-based Python environment that we use for the biweekly workshops. 
(If you would like, however, to install Python locally, hit me up on Teams and I'll walk you through it). 

Once you're in Google Colab, the following lines of code will get you started:

	import pandas as pd
	from datetime import datetime
	
	# define a URL where archibus data is stored
	url = 'https://github.com/james-trimarco/standard_datasets/raw/master/archibus.csv'
	
	# attempt to read the .csv from the URL
	archibus_raw = pd.read_csv(filepath_or_buffer=url, parse_dates=True)

Now you have the data. All you have to do is write a function. Remember that I've left you some clues in seventh exercises file, [which is here](https://colab.research.google.com/drive/1xrsjQJdQCTp7F27QNHLUx9WNVW6pHUym?usp=sharing).

### Judging criteria  
- __Clarity__. Is the code easy to read and follow, and properly documented?

- __Robustness__. How does the code perform given different-quality inputs? Does it throw helpful errors when the input is bad?

- __Concision__. If two functions both meet the first two criteria, we’ll choose the one with fewer lines of code.


- __Originality__. It's OK to look at the interet for parts of your solution. But please don’t copy a complete solution from the internet.

### How to submit your function
When you are satisfied that your function is robust, accurate, and well-documented, you'll need to push it to this repo! If you've never pushed code before, leave yourself 30 minutes or so to walk through it the first time. Eventually, if you keep at it, it will only take a moment to do this. 

Full instructions on pushing code with GitHub Desktop [are here](https://github.com/department-of-general-services/style_guides_and_trainings/blob/master/how_to_push_code_jam_submissions.md).
 

