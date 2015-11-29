import csv
import os
import datetime
from beforeship.settings import SERVER_TMP_FOLDER


class CSVFile():

    def __init__(self, file_in_memory_obj, shop_name):
        self.datetime = datetime.datetime.strftime(datetime.datetime.now(),
                                                   '%Y_%m_%d_%H_%M_%S')
        self.file_in_memory_obj = file_in_memory_obj
        self.file_path = SERVER_TMP_FOLDER + shop_name + self.datetime +\
            ".csv"
        self.file_content_list = []
        self._save_file_on_server()

    def _save_file_on_server(self):
        with open(self.file_path, 'wb+') as destination:
            for chunk in self.file_in_memory_obj.chunks():
                destination.write(chunk)

    def process_csv_file(self):
        with open(self.file_path, "r") as f:
            self.csv_dict_reader = csv.DictReader(f)
            for order in self.csv_dict_reader:
                self.file_content_list.append(order)
        os.remove(self.file_path)
