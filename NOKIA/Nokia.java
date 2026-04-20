import java.util.Scanner;

public class Nokia{

    public static void main(String[] args) {

        Scanner inputCollector = new Scanner(System.in);

        String menu = """
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
                """;

        System.out.print(menu);

        int generalMenuChoice = inputCollector.nextInt();

        switch (generalMenuChoice) {

 //                                     PHONEBOOK 
            case 1 -> {
                System.out.println("PhoneBook");

                String phoneBookMenu = """
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
                        """;

                System.out.println(phoneBookMenu);

                int phoneBookMenuPick = inputCollector.nextInt();

                switch (phoneBookMenuPick) {
                    case 8 -> {
                        System.out.println("Options");
                        String phoneBookOptionMenu = """
                                1 - Type of view
                                2 - Memory status
                                """;
                        System.out.println(phoneBookOptionMenu);
                    }
                }
            }

            //                       MESSAGES 
            case 2 -> {
                System.out.println("Messages");

                String messagesMenu = """
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
                        """;

                System.out.println(messagesMenu);

                int messagesMenuPick = inputCollector.nextInt();

                switch (messagesMenuPick) {

                    case 7 -> {
                        System.out.println("Message Settings");

                        String messagesMessageSettingsMenu = """
                                1 - Set 1
                                2 - Common
                                """;

                        System.out.println(messagesMessageSettingsMenu);

                        int messagesMessageSettingsMenuPick = inputCollector.nextInt();

                        switch (messagesMessageSettingsMenuPick) {

                            case 1 -> {
                                System.out.println("Set 1");
                                String messageSettingsSet1Menu = """
                                        1 - Message centre number
                                        2 - Message sent as
                                        3 - Message validity
                                        """;
                                System.out.println(messageSettingsSet1Menu);
                            }

                            case 2 -> {
                                System.out.println("Common");
                                String messageSettingsCommonMenu = """
                                        1 - Delivery reports
                                        2 - Reply via same centre
                                        3 - Character support
                                        """;
                                System.out.println(messageSettingsCommonMenu);
                            }
                        }
                    }
                }
            }

//                                  CHAT
            case 3 -> System.out.println("Chat");

//                              CALL REGISTER
            case 4 -> {
                System.out.println("Call register");

                String callRegisterMenu = """
                        1 - Missed calls
                        2 - Received calls
                        3 - Dialled numbers
                        4 - Erase recent call lists
                        5 - Show call duration
                        6 - Show call costs
                        7 - Call cost settings
                        8 - Prepaid credit
                        """;

                System.out.println(callRegisterMenu);
                        int callRegisterMenuPick = inputCollector.nextInt();

                        switch (callRegisterMenuPick) {

                            case 5 -> {
                    System.out.println ("Show call duration");
                     String callRegisterShowCallDurationMenu = """
                        1 - Last call duration
                        2 - All calls duration
                        3 - Clear timers
                        4 - Dialled calls duration
                        5 - clear timers
                            """;
                  System.out.print(callRegisterShowCallDurationMenu);

                        switch (callRegisterMenuPick) {

                            case 6 -> {
                    System.out.println ("Show call costs");
                     String callRegisterShowCallCostsMenu = """
                        1 - Last call cost
                        2 - All calls cost
                        3 - Clear counters      
                            """;
                  System.out.print(callRegisterShowCallCostsMenu);
                        }
                    }
                }
            }
        }
    
//                                      TONES
            case 5 -> {
                System.out.println("Tones");

                String tonesMenu = """
                        1 - Ringing tone
                        2 - Ringing volume
                        3 - Incoming call alert
                        4 - Composer
                        5 - Message alert tone
                        6 - Keypad tones
                        7 - Warning and game tones
                        8 - Vibrating alert
                        9 - Screen saver
                        """;

                System.out.println(tonesMenu);
            }

//                                       SETTINGS 
            case 6 -> {
                System.out.println("Settings");

                String settingsMenu = """
                        1 - Call settings
                        2 - Phone settings
                        3 - Security settings
                        4 - Restore factory settings
                        """;

                System.out.println(settingsMenu);
            }

//                              CALL DIVERTS
            case 7 -> System.out.println("Call divert");

//                                  GAMES 
            case 8 -> System.out.println("Games");

//                                 CALCULATOR 
            case 9 -> System.out.println("Calculator");

//                                  REMINDERS 
            case 10 -> System.out.println("Reminders");

//                                     CLOCK 
            case 11 -> {
                System.out.println("Clock");

                String clockMenu = """
                        1 - Alarm clock
                        2 - Clock settings
                        3 - Date setting
                        4 - Stopwatch
                        5 - Countdown timer
                        6 - Auto update of time and date
                        """;

                System.out.println(clockMenu);
            }

//                                  PROFILES
            case 12 -> System.out.println("Profiles");

//                                 SIM SERVICES 
            case 13 -> System.out.println("SIM services");

            default -> System.out.println("Invalid option");
        }

        
    }
}

