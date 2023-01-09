from settings import Settings
import os
import csv


class Translator:
    """
    Business logic: translate csv or txt
    Or Strip spaces from already translated files
    """
    def __init__(self, args):
        self.args = args
        settings = Settings(args[1], args[2], args[3])
        self.quiz = settings.quiz
        self.origin = settings.origin
        self.target = settings.target
        self.filename = settings.filename

        self.origin_folder = settings.origin_folder(self.quiz)
        self.from_folder = settings.from_folder(self.quiz, self.origin)
        self.to_folder = settings.to_folder(self.quiz, self.target)
        self.translator = settings.get_auth_key(self.filename)
        self.translate_formality = settings.translate_formality(self.filename, self.target)

    def translate_csv(self):
        if self.target == "EN":
            self.target = "EN-US"

        # walk the origin folder
        for root, dirs, files in os.walk(self.from_folder):
            for file in files:
                filepath = self.from_folder + file
                ext = file.split(".")
                if ext[1] == 'csv':
                    if self.quiz == 'trivia' or self.quiz == 'img':
                        f = open(filepath, 'r')
                        tmp = dict()
                        with f as csv_file:
                            csv_reader = csv.reader(csv_file, delimiter=';')
                            count = 0
                            for row in csv_reader:
                                question_num = row[0]
                                n_answers = row[2]
                                correct_1 = row[4]
                                correct_2 = row[6]
                                correct_3 = row[8]
                                correct_4 = row[10]

                                if question_num != "#" and question_num != "\ufeff#":
                                    # translate and rename the row
                                    question = self.translator.translate_text(row[1], target_lang=self.target,
                                                                         formality=self.translate_formality)
                                    answer_1 = self.translator.translate_text(row[3], target_lang=self.target,
                                                                         formality=self.translate_formality)
                                    answer_2 = self.translator.translate_text(row[5], target_lang=self.target,
                                                                         formality=self.translate_formality)

                                    if n_answers == "4":
                                        answer_3 = self.translator.translate_text(row[7], target_lang=self.target,
                                                                             formality=self.translate_formality)
                                        answer_4 = self.translator.translate_text(row[9], target_lang=self.target,
                                                                             formality=self.translate_formality)
                                    else:
                                        answer_3 = ""
                                        answer_4 = ""
                                else:
                                    # keep the first row as the original file
                                    question = row[1]
                                    answer_1 = row[3]
                                    answer_2 = row[5]
                                    answer_3 = row[7]
                                    answer_4 = row[9]

                                tmp[count] = [question_num, question, n_answers, answer_1, correct_1, answer_2,
                                              correct_2, answer_3, correct_3, answer_4, correct_4]
                                count += 1
                        f.close()

                        # write the new file and save in the new folder
                        new_filepath = self.to_folder + file
                        f = open(new_filepath, mode='w')

                        with f as fn:
                            newrow = csv.writer(fn, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                            for row in tmp.values():
                                newrow.writerow(row)
                        f.close()
                    elif self.quiz == 'personality':
                        f = open(filepath, 'r')
                        tmp = dict()
                        with f as csv_file:
                            csv_reader = csv.reader(csv_file, delimiter=';')
                            count = 0
                            for row in csv_reader:
                                question_num = row[0]
                                n_answers = row[2]
                                p1 = row[3]
                                p2 = row[4]
                                p3 = row[5]
                                p4 = row[6]

                                if question_num != "#" and question_num != "\ufeff#":
                                    # translate and rename the row
                                    question = self.translator.translate_text(row[1], target_lang=self.target,
                                                                         formality=self.translate_formality)
                                    p1 = self.translator.translate_text(row[3], target_lang=self.target,
                                                                   formality=self.translate_formality)
                                    p2 = self.translator.translate_text(row[4], target_lang=self.target,
                                                                   formality=self.translate_formality)
                                    p3 = self.translator.translate_text(row[5], target_lang=self.target,
                                                                   formality=self.translate_formality)
                                    p4 = self.translator.translate_text(row[6], target_lang=self.target,
                                                                   formality=self.translate_formality)
                                else:
                                    # keep the first row as the original file
                                    question = row[1]
                                    p1 = row[3]
                                    p2 = row[4]
                                    p3 = row[5]
                                    p4 = row[6]

                                tmp[count] = [question_num, question, n_answers, p1, p2, p3, p4]
                                count += 1
                        f.close()

                        # write the new file and save in the new folder
                        new_filepath = self.to_folder + file
                        f = open(new_filepath, mode='w')

                        with f as fn:
                            newrow = csv.writer(fn, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                            for row in tmp.values():
                                newrow.writerow(row)
                        f.close()

        return True

    def translate_txt(self):
        if self.target == "EN":
            self.target = "EN-US"

        for root, dirs, files in os.walk(self.from_folder):
            for file in files:
                from_filepath = self.from_folder + file
                to_filepath = self.to_folder + file
                f = open(from_filepath, 'r')
                ext = from_filepath.split(".")
                if ext[1] == 'txt':
                    self.translator.translate_document_from_filepath(
                        from_filepath,
                        to_filepath,
                        target_lang=self.target,
                        formality=self.translate_formality,
                    )

                f.close()

        self.strip_spaces()

        return True

    def strip_spaces(self):
        search_colon = " :"
        replace_colon = ":"
        search_question = " ?"
        replace_question = "?"
        search_exclamation = " !"
        replace_exclamation = "!"

        for root, dirs, files in os.walk(self.to_folder):
            for file in files:
                filepath = self.to_folder + file
                ext = file.split(".")
                if ext[1] != ('jpeg' or 'jpg' or 'png' or 'webp'):
                    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                        data = f.read()
                        data = data.replace(search_colon, replace_colon).replace(search_question,
                                                                                 replace_question).replace(
                            search_exclamation, replace_exclamation)

                    with open(filepath, 'w') as f:
                        f.write(data)

        return True

