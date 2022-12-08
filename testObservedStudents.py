import collections
import datetime
import itertools
import sys
import time

Exam = collections.namedtuple("Exam", "name cfu")


class HistoryView:
    def __init__(self):
        self.data = []

    def update(self, model):
            self.data.append((model.grades.copy(),model.english_r,time.time()))


class LiveView:
    def __init__(self):
        self.english = False
        self.esami = {}

    def update(self, model):
        if model.english_r and not self.english:
            self.english = True
            print("Cambio stato: lo studente ha appena superato la prova di Inglese\n")
        if  model.esame is not None and self.esami.get(model.esame.name) is None :
            self.esami.update({model.esame.name : model.esame.cfu})
            print("Cambio stato: lo studente ha superato un nuovo esame")
            print("Cambio stato: il numero di CFU e`: ",model.total_cfu, "\n")

class Observed:

    def __init__(self):
        self.__observers = set()

    def observers_add(self, observer, *observers):
        for observer in itertools.chain((observer,), observers):
            self.__observers.add(observer)
            observer.update(self)

    def observer_discard(self, observer):
        self.__observers.discard(observer)

    def observers_notify(self):
        for observer in self.__observers:
            observer.update(self)


class LaureaT_Student(Observed):

    def __init__(self, total_cfu):
        super().__init__()
        self._total_cfu = self._esame= None
        self._english_r = False
        self._grades = {}
        self.total_cfu=total_cfu

    @property
    def total_cfu(self):
        return self._total_cfu

    @total_cfu.setter
    def total_cfu(self, value):
        if self._total_cfu != value:
            self._total_cfu = value
            self.observers_notify()

    @property
    def english_r(self):
        return self._english_r

    @english_r.setter
    def english_r(self, value):
        if self._english_r != value:
            self._english_r = value
            self.observers_notify()

    @property
    def grades(self):
        return self._grades

    def add_grade(self, esame, voto):
            self.esame=esame
            self._grades.update({esame.name:voto})
            self.observers_notify()

    @property
    def esame(self):
        return self._esame

    @esame.setter
    def esame(self, value):
        self._esame=value
        self.total_cfu+=value.cfu

def main():
    historyView = HistoryView()
    liveView = LiveView()
    student = LaureaT_Student(0)
    student.observers_add(historyView, liveView)
    print("Lo studente sta per superare analisi matematica")
    student.add_grade(Exam("analisi matematica", 9), 28)
    print("Lo studente sta per superare asistemi operativi")
    student.add_grade(Exam("sistemi operativi", 6), 20)
    print("Lo studente sta per superare la prova di Inglese")
    student.english_r = True

    for grades, flag, timestamp in historyView.data:
        print("Esami: {}, Inglese: {}, Data: {}".format(grades,
                                                        " " if flag == None else "superato" if flag else "non superato",
                                                        datetime.datetime.fromtimestamp(timestamp)), file=sys.stderr)


if __name__ == "__main__":
    main()

"""
Il programma stampa:

Lo studente sta per superare analisi matematica
Cambio stato: lo studente ha superato un nuovo esame
Cambio stato: il numero di CFU e` :  9 

Lo studente sta per superare a sistemi operativi
Cambio stato: lo studente ha superato un nuovo esame
Cambio stato: il numero di CFU e` :  15 

Lo studente sta per superare la prova di Inglese
Cambio stato: lo studente ha appena superato la prova di Inglese

Esami: {}, Inglese: non superato, Data: 2022-11-21 22:26:12.713307
Esami: {'analisi matematica': 28}, Inglese: non superato, Data: 2022-11-21 22:26:12.756684
Esami: {'analisi matematica': 28}, Inglese: non superato, Data: 2022-11-21 22:26:12.889491
Esami: {'analisi matematica': 28, 'sistemi operativi': 20}, Inglese: non superato, Data: 2022-11-21 22:26:12.923176
Esami: {'analisi matematica': 28, 'sistemi operativi': 20}, Inglese: non superato, Data: 2022-11-21 22:26:13.075015
Esami: {'analisi matematica': 28, 'sistemi operativi': 20}, Inglese: superato, Data: 2022-11-21 22:26:13.107723

"""
