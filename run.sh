#!/bin/bash
rm -rf __pycache__
rm trading.db
python3 Create_db_anitej_mock.py
python3 controller_mock.py