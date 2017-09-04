#!/usr/bin/env python3
import sqlite3

connection = sqlite3.connect('trading.db')
cursor = connection.cursor()

cursor.execute(
    '''CREATE TABLE users (
        username VARCHAR(128),
        password VARCHAR(128),
        balance REAL
    );'''
)

cursor.execute(
    '''CREATE TABLE portfolio (
        username VARCHAR,
        stock_name VARCHAR(128),
        stock_symbol VARCHAR(128),
        last_price VARCHAR(128),
        volume VARCHAR(128),
        portfolio_value REAL,
        FOREIGN KEY(username) REFERENCES users(username)
    );'''
)