# -*- coding: utf-8 -*-
import json
from watson_developer_cloud import ToneAnalyzerV3

# BEGIN of python-dotenv section
from os.path import join, dirname
from dotenv import load_dotenv
import os

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)
# END of python-dotenv section


tone_analyzer = ToneAnalyzerV3(
   username=os.environ.get("TONE_USERNAME"),
   password=os.environ.get("TONE_PASSWORD"),
   version='2016-05-19')


while 1:
    input_content = input('ToneAnalyzer> ')

    if (input_content.lower() in {'exit', 'quit', 'q', 'n'}):
        break

    json_response = tone_analyzer.tone(text=input_content)
    #print(json.dumps(json_response, indent=2))

    emotions = {}
    for entry in json_response['document_tone']['tone_categories']:
        if entry['category_id'] == 'emotion_tone':
            for emotion in entry['tones']:
                emotion_key = emotion['tone_name']
                emotion_value = emotion['score']
                emotions[emotion_key] = emotion_value

    for key in ['Anger','Disgust','Fear','Joy','Sadness']:
        print("{0}, {1:0.2f}".format(key, emotions[key]))
