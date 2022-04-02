# -*- coding: utf-8 -*-
"""Helper functions to load and save CSV data.

This contains a helper function for loading and saving CSV files.

"""
import csv
from pathlib import Path


def load_csv(csvpath):
    """Reads the CSV file from path provided.

    Args:
        csvpath (Path): The csv file path.

    Returns:
        A list of lists that contains the rows of data from the CSV file.

    """
    with open(csvpath, "r") as csvfile:
        data = []
        csvreader = csv.reader(csvfile, delimiter=",")

        # Skip the CSV Header
        next(csvreader)

        # Read the CSV data
        for row in csvreader:
            data.append(row)
    return data


def save_csv(csvpath, data):
    """Writes the CSV file to path provided.

    Args:
        csvpath (Path): The csv file path.

    Returns:
        A list of lists that contain the rows to write to a csv file. 

    """
    with open(csvpath, "w") as csvfile:
    
        csvwriter = csv.writer(csvfile)

        
        # Write the CSV data
        for row in data:
            csvwriter.writerow(row)
    #return data
