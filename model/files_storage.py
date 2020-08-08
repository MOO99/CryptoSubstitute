import csv
import os
from pathlib import Path


class FilesStorage:
    def __init__(self):
        self.root_directory = os.getcwd()

    @staticmethod
    def check_if_csv_exists(csv_file: str):
        if Path(csv_file).is_file():
            return True
        return False

    @staticmethod
    def check_if_folder_exists(folder: str):
        if Path(folder).is_dir():
            return True
        return False

    @staticmethod
    def new_file(file_to_create: str):
        with open(file_to_create, "x") as new_file:
            new_file.close()
        return new_file

    @staticmethod
    def new_directory(path: str = os.getcwd(),
                      directory_name: str = "NULL"):
        path_to_create = os.path.join(path, directory_name)
        try:
            os.mkdir(path_to_create, 0o777)
            return True
        except OSError:
            print(
                f"Creation of directory {path_to_create} failed, make sure it doesn't already exist!"
            )
            pass
        return False

    @staticmethod
    def enter_directory(directory_to_enter: str):
        os.chdir(os.path.join(os.getcwd(), directory_to_enter))

    @staticmethod
    def merge_directory_path(first_part_or_path, second_part_of_path):
        return os.path.join(first_part_or_path, second_part_of_path)

    def return_to_root_directory(self):
        os.chdir(self.root_directory)


class WalletsStorage:
    def __init__(self):
        pass

    @staticmethod
    def add_wallet_to_csv(csv_path: str, wallet_to_add: str):
        split_wallet = wallet_to_add.split(":")
        with open(csv_path, "a", newline="") as working_csv:
            fieldnames = ["wallet", "format", "currency"]
            csv_writer = csv.DictWriter(working_csv, fieldnames=fieldnames)
            csv_writer.writerow({
                "wallet": split_wallet[0],
                "format": split_wallet[1],
                "currency": split_wallet[2],
            })
            working_csv.close()
