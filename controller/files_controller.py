from model.files_storage import FilesStorage
from model.files_storage import WalletsStorage


class WalletsController:
    def __init__(self):
        pass

    @staticmethod
    def confirm_or_create_default_wallets_dir():
        if FilesStorage().check_if_folder_exists("wallets"):
            pass
        else:
            FilesStorage().new_directory("wallets")

    @staticmethod
    def confirm_or_create_default_wallets_csv():
        FilesStorage().enter_directory("wallets")
        if FilesStorage().check_if_csv_exists("default.csv"):
            pass
        else:
            FilesStorage().new_file("default.csv")
        FilesStorage().return_to_root_directory()

    def divide_csv_content_into_smaller_ones(self):  # TODO
        pass

    @staticmethod
    def add_wallet_to_default_csv(wallet_to_add: str):
        WalletsStorage().add_wallet_to_csv(csv_path="default.csv",
                                           wallet_to_add=wallet_to_add)
