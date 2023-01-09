import deepl


class Settings:
    """
    This class defines the translation settings, origin and target languages and folders,
    and get auth key from DEEPL
    """
    def __init__(self, origin, target, quiz):
        self.origin = origin
        # target language will be uppercase
        self.target = target.upper()

        self.quiz = quiz
        self.filename = "deepl.txt"

    @staticmethod
    def get_auth_key(filename):
        # get url and key from file
        with open(filename, mode='r', encoding="UTF-8") as f:
            lines = f.readlines()

        url = lines[0].rstrip()
        auth_key = lines[1].rstrip()

        t = deepl.Translator(auth_key)
        return t

    def translate_formality(self, filename, target):
        # get auth key
        translator = self.get_auth_key(filename)

        translate_formality = ""

        if self.target == "EN":
            self.target = "EN-US"

        for language in translator.get_target_languages():
            if language.supports_formality:
                if language.code == target:
                    translate_formality = "less"

        return translate_formality

    @staticmethod
    def origin_folder(quiz):
        # file paths depending on quiz type
        of = "_" + quiz.lower() + "/"
        return of

    def from_folder(self, quiz, origin):
        origin_folder = self.origin_folder(quiz)
        # define origin folder from origin language
        from_lang = origin.lower() + "/"
        from_folder = origin_folder + from_lang
        return from_folder

    def to_folder(self, quiz, target):
        origin_folder = self.origin_folder(quiz)
        # define target folders
        to_lang = target.lower() + "/"
        to_folder = origin_folder + to_lang
        return to_folder

