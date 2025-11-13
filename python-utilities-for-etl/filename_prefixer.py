# filename_prefixer.py
from datetime import datetime

def build_filename(prefix, filecode):
    month = datetime.now().strftime('%B').upper()  # e.g., 'OCTOBER'
    return f"{prefix}_{filecode}_{month}.csv"

if __name__ == '__main__':
    print(build_filename('SPE','mcla'))
