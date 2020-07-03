from controller.console_controller import ConsoleController
from controller.clipboard_controller import ClipboardData
class ConsoleView:
    def __init__(self):
        pass

    def show_welcome_message(self):
        ConsoleController().welcome_message()

    def rich_text(self, text):
        ConsoleController().print_rich_text(text=text)

    def print_clipboard_content(self):#TODO This has to be moved to View
     #   RichConsole().print_rich_text(ClipboardData().clipboard_content())
        ConsoleController().print_rich_text(ClipboardData().clipboard_content())