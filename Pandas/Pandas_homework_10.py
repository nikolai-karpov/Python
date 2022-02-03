import pandas as pd
import os


def concat_users_files(path):
    file_names = os.listdir(path)
    file_names.sort()
    concated_users_files = pd.DataFrame()
    for file in file_names:
        tmp_data = pd.read_csv(path + '/' + file)
        concated_users_files = pd.concat([concated_users_files, tmp_data], axis=0, ignore_index=True) #axis=0 иначе прирастит столбцы
    concated_users_files = concated_users_files.drop_duplicates()
    return(concated_users_files)


if __name__ == '__main__':
    data = concat_users_files('./Root/users/')