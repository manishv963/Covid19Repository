## happy path 1 (C:\Users\user\AppData\Local\Temp\tmpvo153xgj\8ea59ede179142b588d0d6b0495915d6_conversation_tests.md)
* greet: hello there!
    - utter_greet
* mood_great: amazing   <!-- predicted: greet: amazing -->
    - utter_happy   <!-- predicted: utter_greet -->


## happy path 2 (C:\Users\user\AppData\Local\Temp\tmpvo153xgj\8ea59ede179142b588d0d6b0495915d6_conversation_tests.md)
* greet: hello there!
    - utter_greet
* mood_great: amazing   <!-- predicted: greet: amazing -->
    - utter_happy   <!-- predicted: utter_greet -->
* goodbye: bye-bye!
    - utter_goodbye   <!-- predicted: utter_ask_country -->
    - action_listen   <!-- predicted: action_reset_slot -->


## sad path 1 (C:\Users\user\AppData\Local\Temp\tmpvo153xgj\8ea59ede179142b588d0d6b0495915d6_conversation_tests.md)
* greet: hello
    - utter_greet
* mood_unhappy: not good   <!-- predicted: negativeRepsone: not good -->
    - utter_cheer_up   <!-- predicted: utter_goodbye -->
    - utter_did_that_help   <!-- predicted: action_listen -->
    - action_listen   <!-- predicted: action_reset_slot -->
* affirm: yes
    - utter_happy   <!-- predicted: utter_greet -->


## sad path 2 (C:\Users\user\AppData\Local\Temp\tmpvo153xgj\8ea59ede179142b588d0d6b0495915d6_conversation_tests.md)
* greet: hello
    - utter_greet
* mood_unhappy: not good   <!-- predicted: negativeRepsone: not good -->
    - utter_cheer_up   <!-- predicted: utter_goodbye -->
    - utter_did_that_help   <!-- predicted: action_listen -->
    - action_listen   <!-- predicted: action_reset_slot -->
* deny: not really   <!-- predicted: showAll: not really -->
    - utter_goodbye   <!-- predicted: utter_ask_country -->
    - action_listen   <!-- predicted: action_reset_slot -->


## sad path 3 (C:\Users\user\AppData\Local\Temp\tmpvo153xgj\8ea59ede179142b588d0d6b0495915d6_conversation_tests.md)
* greet: hi
    - utter_greet
* mood_unhappy: very terrible   <!-- predicted: totalTest: very terrible -->
    - utter_cheer_up   <!-- predicted: utter_ask_country -->
    - utter_did_that_help   <!-- predicted: action_listen -->
    - action_listen   <!-- predicted: action_reset_slot -->
* deny: no   <!-- predicted: negativeRepsone: no -->
    - utter_goodbye
    - action_listen   <!-- predicted: action_reset_slot -->


## say goodbye (C:\Users\user\AppData\Local\Temp\tmpvo153xgj\8ea59ede179142b588d0d6b0495915d6_conversation_tests.md)
* goodbye: bye-bye!
    - utter_goodbye   <!-- predicted: utter_greet -->
    - action_listen   <!-- predicted: action_reset_slot -->


## bot challenge (C:\Users\user\AppData\Local\Temp\tmpvo153xgj\8ea59ede179142b588d0d6b0495915d6_conversation_tests.md)
* bot_challenge: are you a bot?   <!-- predicted: showAll: are you a bot? -->
    - utter_iamabot   <!-- predicted: utter_ask_country -->


