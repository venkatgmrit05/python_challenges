from Data_cleaning.cars.data import __path__ as datapath
import os
import sys

import pandas as pd

if __name__ == '__main__':

    src_path = datapath._path[0]
    print(src_path)

    df = pd.read_csv(src_path)









    print(0)
