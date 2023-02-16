import data_prep.structure as struc
import internal.db_connect as db
import plotting.plotting as pl
import ML.quick_linear_regression as qlr
import external.weather as wt


# Plot items out over turnover
# Use all data for a certain store
# Drop values where items sold is zero (since there is somehow still turnover)
def plot_items_out_by_turnover():
    twd = db.execute_twd_ordered_turnover(db.dockerDB)
    df = db.sqlToPandas(twd, struc.twdColumns, struc.columnsNoTurnoverAndItemsOut)
    print(df.info)

    df = struc.drop_zero_turnover(df)
    print(df.info)

    pl.plot('Turnover', df['turnover'], 'Items out', df['items_out'], 'items out over turnover')

    # Predict items out by turnover
    X, Y, Y_pred = qlr.qlr_predict(df, df)
    pl.scatter_and_plot('Turnover', X, 'Items out', Y, Y_pred)


def plot_items_out_over_time():
    twd = dp.execute_twd(dp.dockerDB)
    df = dp.sqlToPandas(twd, dp.twdColumns, dp.columnsNoYearWeekDayAndItemsOut)

    # Return the rows belonging to 2021, change 7 to 0 for datetime objects
    df = dp.get_one_year(df, 2021)
    print(df)
    dp.add_column_ywd(df)  # add column with entries as 'YYYY-ww-dd', sunday becomes 0
    dp.convert_ywd_to_dt(df)  # add column with entries as 'YYYY-mm-dd', like '2021-01-04'
    pl.plot('Dates', df['dt'], 'Items out', df['items_out'])  # Plot Items out over time

# def plot_items_out_per_week():
#

# plot turnover over avg temperature
def plot_items_out_and_tavg_over_time():
    twd = dp.execute_twd(dp.dockerDB)
    df = dp.sqlToPandas(twd, dp.twdColumns, dp.columnsNoYearWeekDayAndItemsOut)

    # Return the rows belonging to 2021, change 7 to 0 for datetime objects
    df = dp.get_one_year(df, 2021)
    print(df)
    dp.add_column_ywd(df)           # add column with entries as 'YYYY-ww-dd', sunday becomes 0
    dp.convert_ywd_to_dt(df)        # add column with entries as 'YYYY-mm-dd', like '2021-01-04'


    # Get the daily stats for 2021, the same dates as used for the items out
    w_stats = wt.get_daily_data()

    cum_df = dp.create_df_from_dfs([df['dt'], df['items_out'], w_stats['tavg']], ['dt', 'items_out', 'tavg'])
    print(cum_df)

    dp.delete_nan(cum_df)


    # Plot AVG-Temp *10 and Items out over the Date
    pl.plot_twice('Date', cum_df['dt'], 'Average temperature &  Items out', cum_df['tavg'] * 10, cum_df['items_out'], 'items out over turnover')

    # Predict Items by temperature
    X, Y, Y_pred = qlr.qlr_predict(w_stats, df, 0, 3)
    print(X)
    print(Y)
    print(Y_pred)
    pl.plot_thrice('Dates', df['dt'], 'Average temperature, Items out, Prediction items out', X, Y, Y_pred)



plot_items_out_by_turnover()
# plot_items_out_over_time()
# plot_items_out_and_tavg_over_time()

