"""Creates beasts.csv from parsed data"""


import pandas as pd


def get_beast_csv(ru_beasts, lat_beasts):
    """Creates beasts.csv"""

    # Dict prepared for df
    ru_dct = {k: [v] for k, v in ru_beasts.items()}
    lat_dct = {k: [v] for k, v in lat_beasts.items()}
    # Data rotation 90, column creation
    ru_df = pd.DataFrame(ru_dct).T.rename_axis("ru_cat").reset_index()
    lat_df = pd.DataFrame(lat_dct).T.rename_axis("lat_cat").reset_index()
    # default column renamed
    ru_df.rename(columns={0: "ru_qty"}, inplace=True)
    lat_df.rename(columns={0: "lat_qty"}, inplace=True)
    # beasts.csv creation
    concatenated = pd.concat([ru_df, lat_df], axis=1)
    concatenated.to_csv("outputs/beasts.csv")
