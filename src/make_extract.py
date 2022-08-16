
"Make sample data extract"

import sqlite3 as sqlite 
import pandas as pd

from src.helpers.utils import db_file
from src.helpers.queries import query_nsf, query_mag

if __name__ == "__main__":
    con = sqlite.connect(db_file)
    with con:
        d_mag = pd.read_sql(sql=query_mag, con=con)
        d_nsf = pd.read_sql(sql=query_nsf, con=con)

    d_mag.to_csv("data/input_mag.csv", index=False)
    d_nsf.to_csv("data/input_nsf.csv", index=False)

    con.close()


