"""tool to download and process COVID-19 data"""
import argparse
import logging
from covid19_graphs.covid19_processing import Covid19Processing

CONFIRMED = {'Url': 'https://raw.githubusercontent.com/CSSEGISandData/'
                    'COVID-19/master/csse_covid_19_data/'
                    'csse_covid_19_time_series/'
                    'time_series_19-covid-Confirmed.csv',
             'Title': 'Covid-19 confirmed cases - data from John Hopkins CSSE',
             'Ylabel': 'ConfirmedCases'}

DEATH = {'Url': 'https://raw.githubusercontent.com/CSSEGISandData/'
                'COVID-19/master/csse_covid_19_data/'
                'csse_covid_19_time_series/'
                'time_series_19-covid-Deaths.csv',
         'Title': 'Covid-19 deaths - data from John Hopkins CSSE',
         'Ylabel': 'Deaths'}


RECOVERED = {'Url': 'https://raw.githubusercontent.com/CSSEGISandData/'
                    'COVID-19/master/csse_covid_19_data/'
                    'csse_covid_19_time_series/'
                    'time_series_19-covid-Recovered.csv',
             'Title': 'Covid-19 recovered - data from John Hopkins CSSE',
             'Ylabel': 'Recovered'}

CONTINENTS = {
    'A': ['Afghanistan', 'Armenia', 'Azerbaijan',
          'Bahrain', 'Bangladesh', 'Bhutan',
          'Brunei', 'Cambodia', 'Cyprus',
          'Georgia', 'India', 'Indonesia',
          'Iran', 'Iraq', 'Israel', 'Japan',
          'Jordan', 'Kazakhstan', 'Kuwait',
          'Kyrgyzstan', 'Laos', 'Lebanon',
          'Malaysia', 'Maldives', 'Mongolia',
          'Myanmar', 'Nepal', 'North Korea',
          'Oman', 'Pakistan', 'Palestine',
          'Philippines', 'Qatar', 'Russia',
          'Saudi Arabia', 'Singapore',
          'South Korea', 'Korea, South', 'Sri Lanka',
          'Syria', 'Taiwan', 'Taiwan*', 'Tajikistan',
          'Thailand', 'Timor-Leste', 'Turkey',
          'Turkmenistan', 'United Arab Emirates',
          'Uzbekistan', 'Vietnam', 'Yemen'],
    'E': ['Albania', 'Andorra', 'Armenia', 'Austria', 'Azerbaijan',
          'Belarus', 'Belgium', 'Bosnia and Herzegovina', 'Bulgaria',
          'Croatia', 'Cyprus', 'Czechia', 'Denmark', 'Estonia',
          'Finland', 'France', 'Georgia', 'Germany', 'Greece',
          'Hungary', 'Iceland', 'Ireland', 'Italy', 'Kazakhstan',
          'Kosovo', 'Latvia', 'Liechtenstein', 'Lithuania',
          'Luxembourg', 'Malta', 'Moldova', 'Monaco', 'Montenegro',
          'Netherlands', 'North Macedonia', 'Norway', 'Poland',
          'Portugal', 'Romania', 'San Marino', 'Serbia', 'Slovakia',
          'Slovenia', 'Spain', 'Sweden', 'Switzerland', 'Turkey',
          'Ukraine', 'United Kingdom', 'Vatican City'],
    'Am': ['Antigua and Barbuda', 'Argentina', 'Bahamas',
           'Barbados', 'Belize', 'Bolivia', 'Brazil',
           'Canada', 'Chile', 'Colombia', 'Costa Rica',
           'Cuba', 'Dominica', 'Dominican Republic',
           'Ecuador', 'El Salvador', 'Grenada', 'Guatemala',
           'Guyana', 'Haiti', 'Honduras', 'Jamaica',
           'Mexico', 'Nicaragua', 'Panama', 'Paraguay', 'Peru',
           'Saint Kitts and Nevis', 'Saint Lucia',
           'Saint Vincent and the Grenadines', 'Suriname',
           'Trinidad and Tobago', 'Uruguay', 'US', 'Venezuela']
}


def parse_command_line_args(test_override=None):
    """Parse options returning the args namespace

    Sets up the command line using argparse including the help message.
    Here a single sequence string is required for output directory is
    required.

    test_override is an optional list of arguments (this is for testing).

    returns the args namespace that can be used for control
    """
    parser = argparse.ArgumentParser(description=__doc__)
    help_ = 'directory for output files '
    parser.add_argument('out_dir', metavar='OUT_DIR', help=help_)
    help_ = 'turn on debug message logging output'
    parser.add_argument('-d', '--debug', action='store_true', help=help_)
    if test_override is not None:
        args = parser.parse_args(test_override)
    else:
        args = parser.parse_args()
    return args


def main():
    """ main function invoked by covid19 script"""
    args = parse_command_line_args()
    # turn on debug level logging if user specifies --debug
    if args.debug:
        logging.basicConfig(level=logging.DEBUG,
                            format='debug %(message)s')
    print(__doc__)
    out_dir = args.out_dir
    logging.debug('args namespace: %args')
    logging.debug('will output to directory: %out_dir')
    confirm = Covid19Processing(CONFIRMED, CONTINENTS, out_dir)
    deaths = Covid19Processing(DEATH, CONTINENTS, out_dir)
    recover = Covid19Processing(RECOVERED, CONTINENTS, out_dir)
    confirm.runclass()
    deaths.runclass()
    recover.runclass()
