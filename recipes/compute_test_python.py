# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
train_prepared = dataiku.Dataset("train_prepared")
train_prepared_df = train_prepared.get_dataframe()


# Compute recipe outputs from inputs
# TODO: Replace this part by your actual code that computes the output, as a Pandas dataframe
# NB: DSS also supports other kinds of APIs for reading and writing data. Please see doc.

test_python_df = train_prepared_df # For this sample code, simply copy input to output


# Write recipe outputs
test_python = dataiku.Dataset("test_python")
test_python.write_with_schema(test_python_df)
