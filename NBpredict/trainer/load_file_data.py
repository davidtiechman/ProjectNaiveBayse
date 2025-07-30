import pandas as pd
path_file = '/shared_data/buy_computer_data_full.csv'
def load_data():
    try:
        df = pd.read_csv(path_file)
        print("The file is loading")
        return df
    except FileNotFoundError:
        print(f"File not found: {path_file}")
        raise
    except Exception as e:
        print(f"Error loading file: {e}")
        raise
