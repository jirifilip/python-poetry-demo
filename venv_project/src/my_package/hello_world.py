import pandas as pd


def my_hello_world():
    my_df = pd.DataFrame({
        "a": [1, 2],
        "b": [3, 4]
    })
    column_a_sum = my_df['a'].sum().item()

    return f"Hello world: {column_a_sum}!"
