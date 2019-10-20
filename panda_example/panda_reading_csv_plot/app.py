import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def read_csv_file():
    ds = pd.read_csv("./resources/AAPL.csv")
    """
     head() and tail() show
     top first and top last values respectivly

    """
   # print(ds.head())
    # max closing value
    return ds


def max_closing(ds):
    closing = ds.iloc[:, 4]
    max_closing = np.max(closing)
    print(f"max closing value is {max_closing}")

    # alternative to use .iloc and np
    max_close_pd = ds["Close"].max()
    print(f"max closing value is {max_close_pd}")


def mean_volume(ds):
    volume = ds.iloc[:, 6]
    mean_volume_iloc = np.mean(volume)
    print(f"mean_volume using iloc and np is {mean_volume_iloc}")
    mean_volume_pd = ds["Volume"].mean()
    print(f"mean volume using pd is {mean_volume_pd}")


def show_adj_close(ds):
    ds["Adj Close"].plot()
    plt.show()
def show_two_graph(ds,column1,column2):
     ds[[column1,column2]].plot()
     plt.show()


if __name__ == "__main__":
    ds = read_csv_file()
    max_closing(ds)
    mean_volume(ds)
    show_adj_close(ds)
    show_two_graph(ds,"Close","Adj Close")
