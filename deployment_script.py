'''
This module sets up the github pages repository read for deployment
'''

import os
TEST_PNG = ('/Users/sm42/University/2019.20/'
            'SoftwareDev/coursework/'
            'SimonDMurray.github.io/data/test_file.png')
TEST_CSV = ('/Users/sm42/University/2019.20/'
            'SoftwareDev/coursework/'
            'SimonDMurray.github.io/data/test_file.csv')
TEST_DAILY_PNG = ('/Users/sm42/University/2019.20/'
                  'SoftwareDev/coursework/'
                  'SimonDMurray.github.io/data/'
                  'test_file_daily_new_cases.png')
TEST_DAILY_CSV = ('/Users/sm42/University/2019.20/'
                  'SoftwareDev/coursework/'
                  'SimonDMurray.github.io/data/'
                  'test_file_daily_new_cases.csv')
if os.path.exists(TEST_DAILY_PNG):
    os.remove(TEST_DAILY_PNG)
if os.path.exists(TEST_DAILY_CSV):
    os.remove(TEST_DAILY_CSV)
if os.path.exists(TEST_CSV):
    os.remove(TEST_CSV)
if os.path.exists(TEST_PNG):
    os.remove(TEST_PNG)
