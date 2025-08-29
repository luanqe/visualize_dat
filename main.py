from csv import reader
from os import uname_result
import re


def open_file(filename):
    opened_file = open(filename, encoding = "utf8")
    read_file = reader(opened_file)

    return list(read_file)

applestore = open_file("C:\\Users\\Luan\\Desktop\\Dev\\visualize_data\\db\\AppleStore.csv")
googlestore = open_file("C:\\Users\\Luan\\Desktop\\Dev\\visualize_data\\db\\googleplaystore.csv")


def explore_data(dataset, start, end, rows_and_columns=False):
    dataset_slice = dataset[start:end]
    for row in dataset_slice:
        print(row)
        #print('\n')  # adds a new (empty) line after each row

    if rows_and_columns:
        print('Number of rows:', len(dataset))
        print('Number of columns:', len(dataset[0]))


def check_row_lengths(dataset):
    expected_length = len(dataset[0])  # Number of columns in first row

    for i, row in enumerate(dataset):
        if len(row) != expected_length:
            print(f"Row {i}: has {len(row)} columns instead of {expected_length}")
            print(f"Row {i}: {row}")
            del googlestore[i]


def check_duplicates(dataset):
    duplicate_apps = []
    unique_apps = []
    for app in dataset:
        name = app[0]
        if name in unique_apps:
            duplicate_apps.append(name)
        else:
            unique_apps.append(name)
    print('Number of duplicate apps:', len(duplicate_apps))
    print('Examples of duplicate apps', duplicate_apps[:10])


check_duplicates(googlestore)

reviews_max = {}

for app in googlestore[1:]:
    name = app[0]
    count = re.sub(r"[a-zA-Z]", "", app[3])
    # count = app[3]

    # if re.match(r'^[a-zA-Z]+$', app[3]):
    #     print(1)
    #     continue

    n_reviews = float(count)

    if not name in reviews_max:
        reviews_max[name] = n_reviews
    elif name in reviews_max and reviews_max[name] < n_reviews:
        reviews_max[name] = n_reviews

print(len(reviews_max.keys()))

android_clean = []
already_added = []

for app in googlestore[1:]:
    name = app[0]
    #n_reviews =










