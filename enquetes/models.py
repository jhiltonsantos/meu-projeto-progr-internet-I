from django.db import models

class Enquete(object):
    def __init__(self, question1='', question2='', question3='', data_publicacao='',):
        self.question1 = question1
        self.question2 = question2
        self.question3 = question3
        self.data_publicacao = data_publicacao
