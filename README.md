# Fika

*"A collection of tools for Data Scientists and ML Engineers to automate their workflow of performing analysis to deploying models and pipelines."*

Fika is a library/platform that automates your data science and analytical tasks at any stage in the pipeline. Fika is, at its core, a uniform API that helps automate analytical techniques from various libaries such as pandas, sci-kit learn, spacy, etc.

**Fika** in Swedish - *A moment to slow down and appreciate the good things in life*

## Analysis with Fika

```python
import fika as fk
import pandas as pd

x_train = pd.read_csv('https://raw.githubusercontent.com/karthikraja95/fika/master/examples/data/train.csv') # load data into pandas

# Initialize Data object with training data
# By default, if no test data (x_test) is provided, then the data is split with 20% going to the test set
# 
# Specify predictor field as 'Survived'
df = fk.Classification(x_train, target='Survived')

df.x_train # View your training data
df.x_test # View your testing data

df # Glance at your training data

df[df.Age > 25] # Filter the data

df.x_train['new_col'] = [1,2] # This is the exact same as the either of code above
df.x_test['new_col'] = [1,2]

df.data_report(title='Titanic Summary', output_file='titanic_summary.html') # Automate EDA with pandas profiling with an autogenerated report

df.describe() # Display a high level view of your data using an extended version of pandas describe

df.column_info() # Display info about each column in your data

df.describe_column('Fare') # Get indepth statistics about the 'Fare' column

df.mean() # Run pandas functions on the aethos objects

df.missing_values # View your missing data at anytime

df.correlation_matrix() # Generate a correlation matrix for your training data

df.predictive_power() # Calculates the predictive power of each variable

df.autoviz() # Runs autoviz on the data and runs EDA on your data

df.pairplot() # Generate pairplots for your training data features at any time

df.checklist() # Will provide an iteractive checklist to keep track of your cleaning tasks

```
**NOTE:** One of the benefits of using `fika` is that any method you apply on your train set, gets applied to your test dataset. For any method that requires fitting (replacing missing data with mean), the method is fit on the training data and then applied to the testing data to avoid data leakage.

```python
# Replace missing values in the 'Fare' and 'Embarked' column with the most common values in each of the respective columns.
df.replace_missing_mostcommon('Fare', 'Embarked')

# Replace missing values in the 'Age' column with a random value that follows the probability distribution of the 'Age' column in the training set. 
df.replace_missing_random_discrete('Age')

df.drop('Cabin') # Drop the cabin column
```


## Setup

**Python Requirements**: 3.6, 3.7

**Run**: `pip install fika`


## How to use Fika

Take a look at this [fika.ipynb](https://github.com/karthikraja95/fika/blob/master/examples/fika.ipynb) notebook
