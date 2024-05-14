import pandas as pd


def load_csv_file(filepath: str, default_separator: str = ','):
    if not filepath:
        return None
    # os.path.exists
    return pd.read_csv(filepath, sep=default_separator)


def split_column(current_df, target_column: str = 'Město'):
    new_columns = ['City', 'Street']
    current_df[new_columns] = current_df[target_column] \
            .str \
            .split(',', n=1, expand=True)

    new_order = new_columns + ['Max teplota (°C)', 'Min teplota (°C)', 'Srážky (mm)']

    return current_df[new_order]


cities_df = load_csv_file('cities.csv')
print(split_column(cities_df))
