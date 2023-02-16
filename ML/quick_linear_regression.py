from sklearn.linear_model import LinearRegression


def qlr_predict(ax, ay, x_col=0, y_col=1):
    X = ax.iloc[:, x_col].values.reshape(-1, 1)
    Y = ay.iloc[:, y_col].values.reshape(-1, 1)
    linear_regressor = LinearRegression()
    linear_regressor.fit(X, Y)

    Y_pred = linear_regressor.predict(X)
    return X, Y, Y_pred

# hello world