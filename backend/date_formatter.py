from datetime import datetime

class DateFormatter():
    def __init__(self, e_date, e_date_format):
        self.e_date = e_date
        self.e_date_format = e_date_format

    def _date(self):
        result = ''
        try:
            new_date = datetime.strptime(self.e_date, self.e_date_format)
            result = new_date.strftime('%Y-%m-%d')
        except ValueError:
            result = 'Error'
        return result