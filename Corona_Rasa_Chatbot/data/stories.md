
## interactive_story_2
* greet
    - utter_greet
* totalCases{"query": "Total"}
    - slot{"query": "Total"}
    - utter_ask_country
* active{"region": "usa"}
    - slot{"region": "usa"}
    - action_showTotalCases
    - slot{"region": "usa"}

## interactive_story_3
* greet
    - utter_greet
* totalCases{"query": "Total"}
    - slot{"query": "Total"}
    - utter_ask_country
* active{"region": "rusia"}
    - slot{"region": "rusia"}
    - action_validate_location
    - slot{"region": "russia"}
    - action_showTotalCases
    - slot{"region": "russia"}
    - utter_greet
* totalTest{"query": "totalTest"}
    - slot{"query": "totalTest"}
    - action_showTotalTest
    - slot{"region": "russia"}
    - utter_greet
* active{"query": "activeCases"}
    - slot{"query": "activeCases"}
    - action_showActive
    - slot{"region": "russia"}
    - utter_ask_more
* affirm
    - utter_greet
* totalCases{"query": "Recovered"}
    - slot{"query": "Recovered"}
    - action_showRecovered
    - slot{"region": "russia"}
    - utter_ask_more
* negativeRepsone
    - utter_goodbye
	- action_reset_slot

## interactive_story_4
* greet
    - utter_greet
* totalCases{"query": "Total"}
    - slot{"query": "Total"}
    - utter_ask_country
* specified_country_name{"region": "braazil"}
    - slot{"region": "braazil"}
    - action_validate_location
    - slot{"region": "brazil"}
    - action_showTotalCases
    - slot{"region": "brazil"}
    - utter_ask_more
* affirm
    - utter_greet
* active{"query": "activeCases"}
    - slot{"query": "activeCases"}
    - action_showActive
    - slot{"region": "brazil"}
    - utter_ask_more
* negativeRepsone
    - utter_goodbye
	- action_reset_slot

## interactive_story_5
* greet
    - utter_greet
* totalTest{"query": "totalTest"}
    - slot{"query": "totalTest"}
    - utter_ask_country
* active{"region": "india"}
    - slot{"region": "india"}
    - action_validate_location
    - slot{"region": "india"}
    - action_showTotalTest
    - slot{"region": "india"}
    - utter_ask_more
* negativeRepsone
    - utter_goodbye
	- action_reset_slot

## interactive_story_6
* greet
    - utter_greet
* totalCases{"query": "Recovered"}
    - slot{"query": "Recovered"}
    - utter_ask_country
* specifying_country_name{"region": "isrel"}
    - slot{"region": "isrel"}
    - action_validate_location
    - slot{"region": "israel"}
    - action_showRecovered
    - slot{"region": "israel"}
    - utter_ask_more
* affirm
    - utter_greet
* serious{"query": "Serious"}
    - slot{"query": "Serious"}
    - action_showSerious
    - slot{"region": "israel"}
    - utter_ask_more
* negativeRepsone
    - utter_goodbye
	- action_reset_slot

## interactive_story_7
* greet
    - utter_greet
* showAll{"query": "deaths"}
    - slot{"query": "deaths"}
    - utter_ask_country
* active{"region": "usa"}
    - slot{"region": "usa"}
    - action_validate_location
    - slot{"region": "usa"}
    - action_showDeaths
    - slot{"region": "usa"}
    - utter_ask_more
* affirm
    - utter_greet
* active{"query": "activeCases"}
    - slot{"query": "activeCases"}
    - action_showActive
    - slot{"region": "usa"}
    - utter_ask_more
* negativeRepsone
    - utter_goodbye
	- action_reset_slot

## interactive_story_8
* greet
    - utter_greet
* totalCases{"query": "Total"}
    - slot{"query": "Total"}
    - utter_ask_country
* active{"region": "india"}
    - slot{"region": "india"}
    - action_showTotalCases
    - slot{"region": "india"}
    - utter_ask_more
* affirm
    - utter_greet
* active{"query": "activeCases"}
    - slot{"query": "activeCases"}
    - action_showActive
    - slot{"region": "india"}
    - utter_ask_more
* negativeRepsone
    - utter_goodbye
	- action_reset_slot

## interactive_story_9
* greet
    - utter_greet
* showAll{"query": "deaths"}
    - slot{"query": "deaths"}
    - utter_ask_country
* active{"region": "columbia"}
    - slot{"region": "columbia"}
    - action_validate_location
    - slot{"region": "colombia"}
    - action_showDeaths
    - slot{"region": "colombia"}
    - utter_ask_more
* negativeRepsone
    - utter_goodbye
    - action_reset_slot
    - reset_slots

## interactive_story_10
* greet
    - utter_greet
* totalCases{"query": "Recovered"}
    - slot{"query": "Recovered"}
    - utter_ask_country
* active{"region": "afghanistan"}
    - slot{"region": "afghanistan"}
    - action_validate_location
    - slot{"region": "afghanistan"}
    - action_showRecovered
    - slot{"region": "afghanistan"}
    - utter_ask_more
* affirm
    - utter_greet
* active{"query": "activeCases"}
    - slot{"query": "activeCases"}
    - action_showActive
    - slot{"region": "afghanistan"}
    - utter_ask_more
* negativeRepsone
    - utter_goodbye
    - action_reset_slot
    - reset_slots

## interactive_story_11
* showAll{"query": "deatils", "region": "china"}
    - slot{"query": "deatils"}
    - slot{"region": "china"}
    - action_validate_location
    - action_showTotalCases
    - utter_ask_more
* affirm
    - utter_greet
* totalTest{"query": "totalTest"}
    - slot{"query": "totalTest"}
    - action_showTotalTest
    - utter_ask_more
* negativeRepsone
    - utter_goodbye
    - action_reset_slot
    - reset_slots

## interactive_story_12
* serious{"query": "serious", "region": "india"}
    - slot{"query": "serious"}
    - slot{"region": "india"}
    - action_validate_location
    - action_showTotalCases
    - utter_ask_more
* affirm
    - utter_greet
* active{"query": "activeCases"}
    - slot{"query": "activeCases"}
    - action_showActive
    - utter_ask_more
* negativeRepsone
    - utter_goodbye
    - action_reset_slot
    - reset_slots



## interactive_story_13
* showAll{"query": "details", "region": "japan"}
    - slot{"query": "details"}
    - slot{"region": "japan"}
    - action_validate_location
    - slot{"region": "japan"}
    - action_showTotalCases
    - slot{"region": "japan"}

## interactive_story_14
* showAll{"query": "details", "region": "japan"}
    - slot{"query": "details"}
    - slot{"region": "japan"}
    - action_validate_location
    - slot{"region": "japan"}
    - action_showAllDetails
    - slot{"region": "japan"}
    - utter_ask_more
* affirm
    - utter_greet
* totalCases{"query": "recovered", "region": "india"}
    - slot{"query": "recovered"}
    - slot{"region": "india"}
    - action_validate_location
    - slot{"region": "india"}
    - action_showRecovered
    - slot{"region": "india"}
    - utter_ask_more
* negativeRepsone
    - utter_goodbye
    - action_reset_slot
    - reset_slots

## interactive_story_15
* deaths{"query": "deaths", "region": "chile"}
    - slot{"query": "deaths"}
    - slot{"region": "chile"}
    - action_validate_location
    - slot{"region": "chile"}
    - action_showDeaths
    - slot{"region": "chile"}
    - utter_ask_more
* negativeRepsone
    - utter_goodbye
    - action_reset_slot
    - reset_slots
* greet
    - utter_greet
* totalCases{"query": "Recovered"}
    - slot{"query": "Recovered"}
    - utter_ask_country
* active{"region": "south africa"}
    - slot{"region": "south africa"}
    - action_validate_location
    - slot{"region": "south_africa"}
    - action_showRecovered
    - slot{"region": "south_africa"}
    - utter_ask_more
* negativeRepsone
    - utter_goodbye
    - action_reset_slot
    - reset_slots
* showAll{"query": "details", "region": "grenada"}
    - slot{"query": "details"}
    - slot{"region": "grenada"}
    - action_validate_location
    - slot{"region": "grenada"}
    - action_showAllDetails
    - slot{"region": "grenada"}
    - utter_ask_more
* negativeRepsone
    - utter_goodbye
    - action_reset_slot
    - reset_slots

## interactive_story_16
* showAll{"query": "details", "region": "china"}
    - slot{"query": "details"}
    - slot{"region": "china"}
    - action_validate_location
    - slot{"region": "china"}
    - action_showAllDetails
    - slot{"region": "china"}
    - utter_ask_more
* affirm
    - utter_greet
* deaths{"query": "deaths"}
    - slot{"query": "deaths"}
    - action_showTotalTest
    - slot{"region": "china"}
    - utter_ask_more
* negativeRepsone
    - utter_goodbye
    - action_reset_slot
    - reset_slots
* showAll{"query": "details", "region": "south africa"}
    - slot{"query": "details"}
    - slot{"region": "south africa"}
    - action_validate_location
    - slot{"region": "south_africa"}
    - action_showAllDetails
    - slot{"region": "south_africa"}
    - utter_ask_more
* affirm
    - utter_greet
* deaths{"query": "deaths"}
    - slot{"query": "deaths"}
    - action_showTotalTest
    - slot{"region": "south_africa"}
    - utter_ask_more
* negativeRepsone
    - utter_goodbye
    - action_reset_slot
    - reset_slots
