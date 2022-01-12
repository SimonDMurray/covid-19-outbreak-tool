"""module for Covid19Processing class"""

import logging
import os
import getpass
import pandas as pd
import matplotlib.pyplot as plt


def daily_new_data(area):
    """
    Function generates daily new cases data
    """
    logging.debug('generating daily data has been written')
    difference = {}
    csv_rows = []
    for locations in area.keys():
        difference[locations] = []
        csv_rows.append(locations)
        for index_, value in enumerate(area[locations]):
            if index_ == area[locations][0]:
                difference[locations].append(value)
            else:
                diff = value - area[locations][index_ - 1]
                difference[locations].append(diff)
    return difference, csv_rows


class Covid19Processing:
    """
    This is the main class that runs
    to solve probelm stated in
    README_instructions
    """

    def __init__(self, data, cont, out_dir):
        logging.debug('Covid19Processing __init__ has been written')
        self.url = data['Url']
        self.title = data['Title']
        self.ylabel = data['Ylabel']
        self.cont = cont
        self.current = os.getcwd()
        self.outdir = out_dir

    def create_out_dir(self):
        """
        Creates a new output directory out_dir
        This will be used for all files to be written.
        """
        logging.debug('create_out_dir has been written, %self.outdir')
        outpath = self.current + '/' + self.outdir
        if not os.path.exists(outpath):
            os.makedirs(outpath)
        outcsv = os.path.join(outpath, self.ylabel + '.csv')
        outpng = os.path.join(outpath, self.ylabel + '.png')
        return outcsv, outpng, outpath

    def download_and_store_data(self, outcsv):
        """
        Downloads the dataset from the COVID19 github repo
        into a variable for storage and writes the data
        to a CSV file for user access.
        """
        logging.debug('download_and_store_data has been written'
                      '%outcsv')
        pdr = pd.read_csv(self.url)
        new_columns = {}
        for col in pdr.columns[:4]:
            new_columns[col] = col
        for col in pdr.columns[4:]:
            month, day, year = col.split('/')
            new_date = f'{day}/{month}/{year}'
            new_columns[col] = new_date
        pdr = pdr.rename(columns=new_columns)
        pdr.to_csv(outcsv)
        if str(getpass.getuser()) == 'sm42':
            pdr.to_csv('/Users/sm42/University/2019.20/SoftwareDev/'
                       'coursework/SimonDMurray.github.io/'
                       'data/' + self.ylabel + '.csv')
        return pdr

    def filter_data(self, pdr):
        """
        The data is filtered based on country or continent
        and summed into a list which is stored in a dictionary.
        """
        logging.debug('filter_data has been written')
        dates = list(pdr.columns.values[4:])
        china = pdr.loc[pdr['Country/Region'] == 'China']
        d_princess = pdr.loc[pdr['Country/Region'] == 'Cruise Ship']
        asia = pdr.loc[pdr['Country/Region'].isin(self.cont['A'])]
        euro = pdr.loc[pdr['Country/Region'].isin(self.cont['E'])]
        ukm = pdr.loc[pdr['Country/Region'] == 'United Kingdom']
        amer = pdr.loc[pdr['Country/Region'].isin(self.cont['Am'])]
        oth = pdr.loc[(~pdr['Country/Region'].isin(self.cont['Am']))
                      & (~pdr['Country/Region'].isin(self.cont['E']))
                      & (~pdr['Country/Region'].isin(self.cont['A']))
                      & (pdr['Country/Region'] != 'Cruise Ship')
                      & (pdr['Country/Region'] != 'China')]
        area = {'China': [china[date].sum() for date in dates],
                'DPrincess': [d_princess[date].sum() for date in dates],
                'Asia': [asia[date].sum() for date in dates],
                'Europe': [euro[date].sum() for date in dates],
                'UK': [ukm[date].sum() for date in dates],
                'Americas': [amer[date].sum() for date in dates],
                'Other': [oth[date].sum() for date in dates]}
        return dates, area

    def plot_data(self, dates, area, outpng):
        """
        Plots various graphs using data from the
        areas dictionary and dates list.
        """
        logging.debug('plot_data has been written')
        fig, axis = plt.subplots(figsize=(20, 10))
        axis.plot(dates, area['China'], label='Mainland China')
        axis.plot(dates, area['DPrincess'], label='Diamond Princess')
        axis.plot(dates, area['Asia'], label='Asia (not China')
        axis.plot(dates, area['Europe'], label='Europe')
        axis.plot(dates, area['UK'], label='UK')
        axis.plot(dates, area['Americas'], label='Americas')
        axis.plot(dates, area['Other'], label='Rest of the World')
        every_nth = 4
        for number, label in enumerate(axis.xaxis.get_ticklabels()):
            if number % every_nth != 0:
                label.set_visible(False)
        axis.set(xlabel='date', ylabel=self.ylabel,
                 title=self.title)
        axis.set_yscale('log')
        axis.grid()
        axis.legend()
        fig.savefig(outpng)
        if str(getpass.getuser()) == 'sm42':
            fig.savefig('/Users/sm42/University/2019.20/'
                        'SoftwareDev/coursework/'
                        'SimonDMurray.github.io/data/'
                        + self.ylabel)

    def daily_new_cases_graph(self, dates, difference, outpath):
        """
        Method plots and saves daily new cases data.
        """
        logging.debug('plotting daily data has been written')
        daily_png_path = outpath + '/' + self.ylabel + '_daily_new_cases'
        fig, axis = plt.subplots(figsize=(20, 10))
        axis.plot(dates, difference['China'], label='Mainland China')
        axis.plot(dates, difference['DPrincess'], label='Diamond Princess')
        axis.plot(dates, difference['Asia'], label='Asia (not China')
        axis.plot(dates, difference['Europe'], label='Europe')
        axis.plot(dates, difference['UK'], label='UK')
        axis.plot(dates, difference['Americas'], label='Americas')
        axis.plot(dates, difference['Other'], label='Rest of the World')
        every_nth = 4
        for number, label in enumerate(axis.xaxis.get_ticklabels()):
            if number % every_nth != 0:
                label.set_visible(False)
        axis.set(xlabel='date', ylabel=self.ylabel,
                 title=self.title + ' new daily')
        axis.set_yscale('log')
        axis.grid()
        axis.legend()
        fig.savefig(daily_png_path)
        if str(getpass.getuser()) == 'sm42':
            fig.savefig('/Users/sm42/University/2019.20/'
                        'SoftwareDev/coursework/'
                        'SimonDMurray.github.io/data/'
                        + self.ylabel + '_daily_new_cases')

    def daily_new_cases_csv(self, pdr, difference, csv_rows, outpath):
        """
        Method generates and saves csvs of daily new cases data
        """
        logging.debug('generating csvs of daily data has been written')
        daily_pd = pd.DataFrame(
            difference.values(), index=csv_rows, columns=pdr.columns[4:])
        daily_csv_path = outpath + '/' + self.ylabel + '_daily_new_cases.csv'
        daily_pd.to_csv(daily_csv_path)
        if str(getpass.getuser()) == 'sm42':
            daily_pd.to_csv('/Users/sm42/University/2019.20/SoftwareDev/'
                            'coursework/SimonDMurray.github.io/'
                            'data/' + self.ylabel + '_daily_new_cases.csv')

    def runclass(self):
        """
        Main method which runs
        all other methods
        """
        outcsv, outpng, outpath = self.create_out_dir()
        pdr = self.download_and_store_data(outcsv)
        dates, area = self.filter_data(pdr)
        self.plot_data(dates, area, outpng)
        difference, csv_rows = daily_new_data(area)
        self.daily_new_cases_graph(dates, difference, outpath)
        self.daily_new_cases_csv(pdr, difference, csv_rows, outpath)
