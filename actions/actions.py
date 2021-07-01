# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/
# This is a simple example for a custom action which utters "Hello World!"
import json
import logging
import random
from token import AT
from typing import Dict, Text, Any, List, Union, Optional
from rasa_sdk.types import DomainDict
import psycopg2
from rasa_sdk import Action, FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet, FollowupAction, AllSlotsReset, EventType, ConversationPaused, UserUtteranceReverted
import requests
from rasa_sdk import Tracker


class ActionGreet(Action):
    def name(self) -> Text:
        return "action_greet"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        payload = {"products": "/actions_product", "shop_online": "/actions_shop_online",
                   "contact_us": "/action_contact_us",
                   "order_status": "/order_status", "store_location": "/action_store_location",
                   "cancel_order": "/action_cancel_order", "shop_by_categories": "/actions_product"}
            buttons = []
            buttons.append({"title": "Todays Best Deals", "payload": payload["products"]})
            buttons.append({"title": "Show Products", "payload": payload["products"]})
            buttons.append({"title": "Shop By Categories", "payload": payload["shop_by_categories"]})
            buttons.append({"title": "Store locations ", "payload": payload["store_location"]})
            buttons.append({"title": "Contact Us ", "payload": payload["contact_us"]})
            dispatcher.utter_message(text='HI! I am Search! I can help you with any questions you may have. You can '
                                          'click the links below for any specific information!', buttons=buttons)
        return []


