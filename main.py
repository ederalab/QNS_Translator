import sys
from translator import *


def main():
    try:
        args = []
        for arg in sys.argv:
            args.append(arg)

        # verify languages
        languages = ["it", "en", "fr", "es", "de"]
        if args[1].lower() not in languages:
            print("Please specify a correct and available origin language choosing among: IT, EN, FR, ES, DE")
            exit()
        if args[2].lower() not in languages:
            print("Please specify a correct and available target language choosing among: IT, EN, FR, ES, DE")
            exit()
        if args[1].lower() == args[2].lower():
            print("Origin and Target languages must be different.")
            exit()

        # verify quiz type
        quiz_types = ["img", "trivia", "personality"]
        if args[3].lower() not in quiz_types:
            print("Please specify a correct and available quiz type choosing among: IMG, TRIVIA, PERSONALITY")
            exit()

        # verify file type
        if args[4].lower() == "csv":
            command = Translator(args).translate_csv()
        elif args[4].lower() == "txt":
            command = Translator(args).translate_txt()
        else:
            print("Please specify the file type choosing between CSV and TXT")
            exit()
    except NameError:
        print("an error occurred :" + NameError)
    else:
        if command:
            print("Translation completed!")


if __name__ == '__main__':
    main()
