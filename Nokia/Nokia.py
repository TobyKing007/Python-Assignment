def main():
    menu = """
WELCOME TO NOKIA 3310 - CONNECTING PEOPLE

Press 1     - Phonebook
Press 2     - Messages
Press 3     - Chat
Press 4     - Call Register
Press 5     - Tones
Press 6     - Settings
Press 7     - Call Diverts
Press 8     - Games
Press 9     - Calculator
Press 10    - Reminders
Press 11    - Clock
Press 12    - Profiles
Press 13    - SIM services
"""

    print(menu)

    general_menu_choice = int(input("Choose an option: "))

    match general_menu_choice:

        # ================= PHONEBOOK =================
        case 1:
            print("PhoneBook")
            phonebook_menu = """
1 - Search
2 - Service Nos.
3 - Add name
4 - Erase
5 - Edit
6 - Assign tone
7 - Send b'card
8 - Options
9 - Speed dials
10 - Voice tags
"""
            print(phonebook_menu)

            phonebook_pick = int(input("Choose: "))
            if phonebook_pick == 8:
                print("""
Options
1 - Type of view
2 - Memory status
""")

        # ================= MESSAGES =================
        case 2:
            print("Messages")
            messages_menu = """
1 - Write messages
2 - Inbox
3 - Outbox
4 - Picture Messages
5 - Templates
6 - Smileys
7 - Message settings
8 - Info service
9 - Voice mailbox number
10 - Service command editor
"""
            print(messages_menu)

            messages_pick = int(input("Choose: "))

            if messages_pick == 7:
                print("""
Message Settings
1 - Set 1
2 - Common
""")
                settings_pick = int(input("Choose: "))

                if settings_pick == 1:
                    print("""
Set 1
1 - Message centre number
2 - Message sent as
3 - Message validity
""")

                elif settings_pick == 2:
                    print("""
Common
1 - Delivery reports
2 - Reply via same centre
3 - Character support
""")

        # ================= CHAT =================
        case 3:
            print("Chat")

        # ================= CALL REGISTER =================
        case 4:
            print("Call register")
            call_register_menu = """
1 - Missed calls
2 - Received calls
3 - Dialled numbers
4 - Erase recent call lists
5 - Show call duration
6 - Show call costs
7 - Call cost settings
8 - Prepaid credit
"""
            print(call_register_menu)

            call_pick = int(input("Choose: "))

            if call_pick == 5:
                print("""
Show call duration
1 - Last call duration
2 - All calls duration
3 - Clear timers
4 - Dialled calls duration
5 - Clear timers
""")

            elif call_pick == 6:
                print("""
Show call costs
1 - Last call cost
2 - All calls cost
3 - Clear counters
""")

            elif call_pick == 7:
                print("""
Call cost settings
1 - Call cost limit
2 - Show costs in
""")

        # ================= TONES =================
        case 5:
            print("Tones")
            print("""
1 - Ringing tone
2 - Ringing volume
3 - Incoming call alert
4 - Composer
5 - Message alert tone
6 - Keypad tones
7 - Warning and game tones
8 - Vibrating alert
9 - Screen saver
""")

        # ================= SETTINGS =================
        case 6:
            print("Settings")
            settings_menu = """
1 - Call settings
2 - Phone settings
3 - Security settings
4 - Restore factory settings
"""
            print(settings_menu)

            settings_pick = int(input("Choose: "))

            if settings_pick == 1:
                print("""
Call settings
1 - Automatic redial
2 - Speed dialling
3 - Call waiting options
4 - Own number sending
5 - Phone line in use
6 - Automatic answer
""")

            elif settings_pick == 2:
                print("""
Phone settings
1 - Language
2 - Cell info display
3 - Welcome note
4 - Network selection
5 - Lights
6 - Confirm SIM service actions
""")

            elif settings_pick == 3:
                print("""
Security settings
1 - PIN code request
2 - Call barring service
3 - Fixed dialling
4 - Closed user group
5 - Phone security
6 - Change access codes
""")

        # ================= SIMPLE MENUS =================
        case 7:
            print("Call divert")
        case 8:
            print("Games")
        case 9:
            print("Calculator")
        case 10:
            print("Reminders")

        # ================= CLOCK =================
        case 11:
            print("Clock")
            print("""
1 - Alarm clock
2 - Clock settings
3 - Date setting
4 - Stopwatch
5 - Countdown timer
6 - Auto update of time and date
""")

        case 12:
            print("Profiles")
        case 13:
            print("SIM services")

        case _:
            print("Invalid option")




