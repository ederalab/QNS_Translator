# QNS TRANSLATOR
This translator was meant to simplify effort and time spent to prepare the translations for the articles and quizzes for QuantoNeSai network, a personal project developed with Django framework.

The goal was to translate the txt and csv files in different languages, choosing every time the original and the translation languages. The translator reads all the files in the origin folder and save the translation in the target folder.

# Requirements 
Since the translations are automatically made with Deepl using their APIs, it is necessary to have url and auth key of Deepl Free or Pro, depending on the quantity of text to translate.
For more informations: https://www.deepl.com/it/pro-api?cta=header-pro-api/

It is necessary to install *deepl* library https://pypi.org/project/deepl/


# Disclaimer 

This project is specifically related to QuantoNeSai project, using their specific quiz types, file types and available languages.
For this reason folder structure is pre-defined (3 quiz-type folder named "_" + quiz type with a folder for each language inside)
You can customize the code for your needs.

# How to start 

Launch the command:<br/>
<strong>python3 main.py origin_lang target_lang quiz_type file_type </strong><br/>

where:
- *origin_lang* and *target_lang* must be choosen among: IT, EN, FR, ES, DE
- *quiz_type* must be choosen among: IMG, TRIVIA, PERSONALITY
- *file_type* must be choosen between TXT and CSV

example:<br/>
<strong>python3 main.py it fr personality txt </strong><br/>
