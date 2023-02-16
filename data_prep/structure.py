import pandas as pd
import datetime as dt




twdColumns = ['store_id', 'subdepartment_id', 'year', 'week', 'day', 'turnover', 'nr_customers', 'items_out']
columnsNoTurnoverAndItemsOut = ['store_id', 'subdepartment_id', 'year', 'week', 'day', 'nr_customers']
columnsNoYearWeekDayAndItemsOut = ['store_id', 'subdepartment_id', 'turnover', 'nr_customers']



# drop rows where 0 items were sold (there is still turnover)
def drop_zero_turnover(df):
    return df[df.turnover != 0]
    # return df.drop(df[df.items_out % 1 != 0].index) # why does this even work


def get_one_year(df, year):
    return df[df.year == year]


def add_column_ywd(df):
    df['ywd'] = df['year'].astype(str) + '-' + df['week'].astype(str) + '-' + [str(0) if d == 7 else str(d) for d in
                                                                               df['day']]


# Convert dataframe with date always starting at week 1 day 1 to the correct datetime object
def convert_ywd_to_dt(df):
    df['dt'] = [dt.datetime.strptime(d, '%Y-%W-%w') for d in df['ywd']]


# Create a new dataframe from the given list of columns
def create_df_from_dfs(column_list, column_name_list):


    df_length = len(column_list[0])
    df = pd.DataFrame()
    for i in range(len(column_list)):
        if df_length != len(column_list[i]):
            print(str(df_length) + " notis " + str(len(column_list[i])))
            print("All columns must have the same length in order to maintain the size")
            exit()
        df.index = column_list[i].index             # reset index to ensure values are being added at the right index
        df[column_name_list[i]] = column_list[i]

    return df

# Delete rows where NaN values are present
def delete_nan(nanlist):
    nanlist.dropna(inplace=True)
