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
    print(json.dumps(json_response, indent=2))
