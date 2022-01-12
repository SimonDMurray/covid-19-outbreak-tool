""" unit tests for Covid19Processing"""
import os
import shutil
from covid19_graphs.covid19_processing import Covid19Processing, daily_new_data
from covid19_graphs.command_line_script import CONFIRMED, CONTINENTS


def test_create_out_dir():
    out_dir = 'test_directory'
    test_run = Covid19Processing(CONFIRMED, CONTINENTS, out_dir)
    test_run.create_out_dir()
    test_path = os.path.join(os.getcwd(), out_dir)
    assert os.path.exists(test_path)
    if os.path.exists(test_path):
        shutil.rmtree(test_path)


def test_download_and_store_data():
    CONFIRMED['Ylabel'] = 'test_file'
    out_dir = 'test_directory'
    test_path = os.path.join(os.getcwd(), out_dir)
    test_file = os.path.join(test_path, 'test_file.csv')
    test_run = Covid19Processing(CONFIRMED, CONTINENTS, out_dir)
    test_run.create_out_dir()
    test_run.download_and_store_data(test_file)
    assert os.path.exists(test_file)
    if os.path.exists(test_file):
        shutil.rmtree(test_path)


def test_filter_data():
    CONFIRMED['Ylabel'] = 'test_file'
    out_dir = 'test_directory'
    test_path = os.path.join(os.getcwd(), out_dir)
    test_file = os.path.join(test_path, 'test_file.csv')
    test_run = Covid19Processing(CONFIRMED, CONTINENTS, out_dir)
    test_run.create_out_dir()
    pdr = test_run.download_and_store_data(test_file)
    dates, area = test_run.filter_data(pdr)
    assert len(dates) == len(pdr.columns.values[4:])
    assert len(area) == 7
    shutil.rmtree(test_path)


def test_plot_data():
    CONFIRMED['Ylabel'] = 'test_file'
    out_dir = 'test_directory'
    test_path = os.path.join(os.getcwd(), out_dir)
    test_csv = os.path.join(test_path, 'test_file.csv')
    test_png = os.path.join(test_path, 'test_file.png')
    test_run = Covid19Processing(CONFIRMED, CONTINENTS, out_dir)
    test_run.create_out_dir()
    pdr = test_run.download_and_store_data(test_csv)
    dates, area = test_run.filter_data(pdr)
    test_run.plot_data(dates, area, test_png)
    assert os.path.exists(test_png)
    assert os.path.exists(test_csv)
    if os.path.exists(test_path):
        shutil.rmtree(test_path)


def test_generate_daily_new_cases():
    out_dir = 'test_directory'
    test_path = os.path.join(os.getcwd(), out_dir)
    test_csv = os.path.join(test_path, 'test_file.csv')
    test_run = Covid19Processing(CONFIRMED, CONTINENTS, out_dir)
    test_run.create_out_dir()
    pdr = test_run.download_and_store_data(test_csv)
    _, area = test_run.filter_data(pdr)
    difference, csv_rows = daily_new_data(area)
    assert len(difference['China']) == len(pdr.columns[4:])
    assert csv_rows == list(area.keys())
    if os.path.exists(test_path):
        shutil.rmtree(test_path)


def test_plot_daily_new_cases():
    out_dir = 'test_directory'
    test_path = os.path.join(os.getcwd(), out_dir)
    test_csv = os.path.join(test_path, 'test_file.csv')
    test_daily_png = os.path.join(test_path, 'test_file_daily_new_cases.png')
    test_run = Covid19Processing(CONFIRMED, CONTINENTS, out_dir)
    test_run.create_out_dir()
    pdr = test_run.download_and_store_data(test_csv)
    dates, area = test_run.filter_data(pdr)
    difference, _ = daily_new_data(area)
    test_run.daily_new_cases_graph(dates, difference, test_path)
    assert os.path.exists(test_daily_png)
    assert os.path.exists(test_csv)
    if os.path.exists(test_path):
        shutil.rmtree(test_path)


def test_csv_daily_new_cases():
    out_dir = 'test_directory'
    test_path = os.path.join(os.getcwd(), out_dir)
    test_csv = os.path.join(test_path, 'test_file.csv')
    test_daily_csv = os.path.join(test_path, 'test_file_daily_new_cases.csv')
    test_run = Covid19Processing(CONFIRMED, CONTINENTS, out_dir)
    test_run.create_out_dir()
    pdr = test_run.download_and_store_data(test_csv)
    _, area = test_run.filter_data(pdr)
    difference, csv_rows = daily_new_data(area)
    test_run.daily_new_cases_csv(pdr, difference, csv_rows, test_path)
    assert os.path.exists(test_daily_csv)
    assert os.path.exists(test_csv)
    if os.path.exists(test_path):
        shutil.rmtree(test_path)
