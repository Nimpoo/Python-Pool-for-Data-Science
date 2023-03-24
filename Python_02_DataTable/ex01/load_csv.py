import pandas as pd


def load(path: str) -> pd.core.frame.DataFrame:

    """
    /----------- Utility -----------/
    Load a DataFrame from a .csv file using Pandas.

    /---------- Arguments ----------/
    path : string

    /----------- Return ------------/
    Return a DataFrame .csv from the path in argument
    Return None when encounter an Error
    """

    try:
        data_frame = pd.read_csv(path)

        # if not path.endswith(".csv"):
        #     raise TypeError

    except FileNotFoundError:
        print("FileNotFoundError: pls use a valid file")
        return (None)
    except ValueError:
        print("ValueError: pls use a string type to set a valid path")
        return (None)
    except Exception as e:
        print(e)
        return (None)

    print(f"Loading dataset of dimensions {data_frame.shape}")
    return (data_frame)
