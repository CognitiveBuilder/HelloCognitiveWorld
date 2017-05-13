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


def parse_toneanalyzer_response(json_data):
    """Parses the JSON response from ToneAnalyzer to return
    a dictionary of emotions and their corresponding score.

    Parameters
    ----------
    json_data: {dict} a json response from ToneAnalyzer (see Notes)

    Returns
    -------
    dict : a {dict} whose keys are emotion ids and values are their corresponding score.
    """
    emotions = {}
    for entry in json_data['document_tone']['tone_categories']:
        if entry['category_id'] == 'emotion_tone':
            for emotion in entry['tones']:
                emotion_key = emotion['tone_name']
                emotion_value = emotion['score']
                emotions[emotion_key] = emotion_value
    return(emotions)


if __name__ == '__main__':
    while 1:
        # use line below if you're in python 2
        # input_content = raw_input('ToneAnalyzer>').strip()

        # get some sentence from user input
        input_content = input('ToneAnalyzer> ')

        # if you type one of these, you exit the script
        if (input_content.lower() in {'exit', 'quit', 'q', 'n'}):
            break


        json_response = tone_analyzer.tone(text=input_content)
        #print(json.dumps(json_response, indent=2))
        print(parse_toneanalyzer_response(json_response))
