import pandas as pd
import matplotlib.pyplot as plt


def date_range_run():
    start_date = "10/22/2018"
    end_date = "11/2/2018"
    dates = pd.date_range(start_date, end_date)
   # print(dates)
    # create empty dataframe
    df1 = pd.DataFrame(index=dates)
    symbols = ["AAPL", "GLD", "IBM", "SPY"]
    for symbol in symbols:

        df_temp = pd.read_csv(f"./resources/{symbol}.csv", index_col="Date",
                              parse_dates=True, usecols=["Date", "Adj Close"], na_values=['nan'])
        # print(df_ibm)
        #df1 = df1.join(df_ibm, how='inner')
        df_temp = df_temp.rename(columns={"Adj Close": symbol})
        df1 = df1.join(df_temp, how="inner") 
    # remove NAN from column
    # df1.dropna()
    print(df1.loc["10/22/2018": "10/25/2018", ["IBM", "GLD"]])
    # normalizing data so we have same start point
    df1 = df1/df1.iloc[0, :]
    ax = df1.plot(title="Stock Price")
    ax.set_xlabel("Date")
    ax.set_ylabel("Price")
    plt.show()


if __name__ == "__main__":
    date_range_run()
