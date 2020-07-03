from controller.clipboard_controller import ClipboardController
from view.console_view import ConsoleView


#TODO ENTER_YOUR_CRYPTOS
#TODO GET FEEDBACK FROM MVC

ConsoleView().rich_traceback_handler()
ClipboardController = ClipboardController()

if __name__ == "__main__":
    ConsoleView().welcome_message()
    ClipboardController.print_clipboard_content()                                               #FIXME -----------------------------
    print("======================================================")                             #FIXME          Added this
    print("Clipboard was printed above for debug purposes! Will be removed in next versions.")  #FIXME      for debug purposes
    print("======================================================")                             #FIXME -----------------------------

    print(ClipboardController.check_wallet_format("You_can_enter_any_wallet_here"))

    #TODO enter your addres, leave blank if you don't want to use this one
    #TODO repeat step from above X times, depending on currency(-ies) you want to use
    #TODO automatically check what type of address user entered and inform him about his choice
    #TODO automatically replace address in clipboard using corresponding replacement address, if available
    #TODO if there are addresses for same currency but of different type - use first available