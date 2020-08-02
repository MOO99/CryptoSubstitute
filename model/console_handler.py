from rich.console import Console as Rich_console
from rich.panel import Panel as Rich_panel
from rich.text import Text as Rich_text
from rich.traceback import install as install_rich_traceback_handler


class RichConsole:
    def __init__(self):
        pass

    def install_rich_traceback_handler(self):
        """Installs Rich Traceback Handler"""
        install_rich_traceback_handler()

    def print_rich_text(self, text: str):
        Rich_console().print(Rich_text(text))

    def input_rich_text(self, text: str):
        return Rich_console().input(
            prompt=text
            + "\n[bold yellow]Crypto[/bold yellow][bold red]Substitute[/bold red] >>"
        )

    def print_btc_ascii_logo(self):
        """Prints welcome message with Bitcoin ASCII art, DON'T EDIT THIS!"""
        BTC_logo = Rich_text(
            """
                  ,.=ctE55ttt553tzs.,
             ,,c5;z==!!::::  .::7:==it3>.,
          ,xC;z!::::::    ::::::::::::!=c33x,
        ,czz!:::::  ::;;..===:..:::   ::::!ct3.
      ,C;/.:: :  ;=c!:::::::::::::::..      !tt3.                      __        __     _                                _
     /z/.:   :;z!:::::J  :E3.  E:::::::..     !ct3.                    \ \      / /___ | |  ___  ___   _ __ ___    ___  | |_  ___
   ,E;F   ::;t::::::::J  :E3.  E::.     ::.     \\ttL                    \ \ /\ / // _ \| | / __|/ _ \ | '_ ` _ \  / _ \ | __|/ _ \\
  ;E7.    :c::::F******   **.  *==c;..    ::     Jttk                    \ V  V /|  __/| || (__| (_) || | | | | ||  __/ | |_| (_) |
 .EJ.    ;::::::L                   "\:.   ::.    Jttl                    \_/\_/  \___||_| \___|\___/ |_| |_| |_| \___|  \__|\___/
 [:.    :::::::::773.    JE773zs.     I:. ::::.    It3L                            ____                      _
;:[     L:::::::::::L    |t::!::J     |::::::::    :Et3                           / ___| _ __  _   _  _ __  | |_  ___
[:L    !::::::::::::L    |t::;z2F    .Et:::.:::.  ::[13                          | |    | '__|| | | || '_ \ | __|/ _ \\
E:.    !::::::::::::L               =Et::::::::!  ::|13                          | |___ | |   | |_| || |_) || |_| (_) |
E:.    (::::::::::::L    .......       \:::::::!  ::|i3                           \____||_|    \__, || .__/  \__|\___/
[:L    !::::      ::L    |3t::::!3.     ]::::::.  ::[13                                        |___/ |_|
!:(     .:::::    ::L    |t::::::3L     |:::::; ::::EE3                   ____          _           _    _  _           _
 E3.    :::::::::;z5.    Jz;;;z=F.     :E:::::.::::II3[                  / ___|  _   _ | |__   ___ | |_ (_)| |_  _   _ | |   ___
 Jt1.    :::::::[                    ;z5::::;.::::;3t3                   \___ \ | | | || '_ \ / __|| __|| || __|| | | || __|/ _ \\
  \z1.::::::::::l......   ..   ;.=ct5::::::/.::::;Et3L                    ___) || |_| || |_) |\__ \| |_ | || |_ | |_| || |_|  __/
   \\t3.:::::::::::::::J  :E3.  Et::::::::;!:::::;5E3L                    |____/  \__,_||_.__/ |___/ \__||_| \__| \__,_| \__|\___|
    "cz\.:::::::::::::J   E3.  E:::::::z!     ;Zz37`
      \z3.       ::;:::::::::::::::;='      ./355F
        \z3x.         ::~======='         ,c253F
          "tz3=.                      ..c5t32^
             "=zz3==...         ...=t3z13P^
                 `*=zjzczIIII3zzztE3>*^`
        """,
            style="#e2c000",
        )
        Rich_console().print(Rich_panel(BTC_logo))
