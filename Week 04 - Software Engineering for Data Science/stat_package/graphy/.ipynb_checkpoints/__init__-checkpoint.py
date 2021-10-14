#Imports pandas package as pd
import pandas as pd

def plot_data(data):
    """This is a docstring"""
    # Stores data as DataFrame and returns the plot
    ax = pd.DataFrame(data).plot.hist()
    return ax
