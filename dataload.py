import pandas as pd

location='C:/Oxford/Assignment 7/Data nationalgrid'


def dataload():
    twenty5to10 = pd.read_csv(location+'DemandData_2005-2010.csv')


def add(a, b):
    return a+b


def subtract(a, b):
    return a-b


def divide(a, b):
    return a/b
