from pathlib import Path
import os, csv
class FilesStorage:
    def __init__ (self):
        self.root_directory = os.getcwd()

    def check_if_csv_exists(self, csv_file: str):
        if Path(csv_file).is_file():
            return True
        return False

    def check_if_folder_exists(self, folder: str):
        if Path(folder).is_dir():
            return True
        return False

    def new_file(self, file_to_create: str):
        with open(file_to_create, 'x') as new_file:
            new_file.close()
        return new_file

    def new_directory(self, path: str = os.getcwd(), directory_name: str = 'NULL'):
        path_to_create = os.path.join(path, directory_name)
        try:
            os.mkdir(path_to_create, 0o777)
            return True
        except OSError:
            print(f"Creation of directory {path_to_create} failed, make sure it doesn't already exist!")
            pass
        return False

    def enter_directory(self, directory_to_enter: str):
        os.chdir(os.path.join(os.getcwd(), directory_to_enter))

    def merge_directory_path(self, first_part_or_path, second_part_of_path):
        return os.path.join(first_part_or_path, second_part_of_path)
    def return_to_root_directory(self):
        os.chdir(self.root_directory)

class WalletsStorage:
    def __init__(self):
        pass

    def add_wallet_to_csv(self, csv_path: str, wallet_to_add: str):
        splitted_wallet = wallet_to_add.split(':')
        with open(csv_path, 'a', newline='') as working_csv:
            fieldnames = ['wallet', 'format', 'currency']
            csv_writer = csv.DictWriter(working_csv, fieldnames=fieldnames)
            csv_writer.writerow({'wallet':splitted_wallet[0], 'format':splitted_wallet[1], 'currency':splitted_wallet[2]})
            working_csv.close()
