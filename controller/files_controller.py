from model.files_storage import FilesStorage, WalletsStorage

class WalletsController:
    def __init__(self):
        pass

    def confirm_or_create_default_wallets_dir(self):
        FilesStorage().new_directory()

    def confirm_or_create_default_wallets_csv(self):
        FilesStorage().new_directory(directory_name='wallets')
        FilesStorage().enter_directory('wallets')
        if FilesStorage().check_if_csv_exists('default.csv'):
            pass
        else:
            FilesStorage().new_file('default.csv')
        FilesStorage().return_to_root_directory()
    def divide_csv_content_into_smaller_ones(self): #TODO
        pass