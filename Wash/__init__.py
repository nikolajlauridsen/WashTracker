import datetime

DB_NAME = "washbase.db"

COLORS = {
    'azure': '#007fff',
    'green': '#00cc34',
    'red': '#e62020',
    'yellow': '#ffc40c',
    'd-green': '#177245',
    'grey': '#f0f0f0'
}


def format_time(time, t_format='%d/%m/%y %H:%M'):
    return datetime.datetime.fromtimestamp(int(time)).strftime(t_format)
