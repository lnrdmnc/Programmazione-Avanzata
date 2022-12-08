class Bambino():
	ISCRITTO, SECONDOANNO, TERZOANNO, DIPLOMATO=("iscritto","alSecondoAnno","alTerzoAnno","diplomato")

	def __init__(self):
		self.state=Bambino.ISCRITTO

	@property
	def state(self):
		return self.state

	@state.setter
	def state(self,state):
		if state==Bambino.ISCRITTO:
			self.pred=self._pred_iscritto
			self.succ=self._succ_iscritto
			self.stampaStato=self._stampaStato_iscritto
			self.salta_anno = self._salta_anno_iscritto
		elif state == Bambino.SECONDOANNO:
			self.pred = self._pred_secondo
			self.succ = self._succ_secondo
			self.stampaStato = self._stampaStato_secondo
			self.salta_anno = self._salta_anno_secondo
		elif state == Bambino.TERZOANNO:
			self.pred = self._pred_terzo
			self.succ = self._succ_terzo
			self.stampaStato = self._stampaStato_terzo
			self.salta_anno = self._salta_anno_terzo
		elif state == Bambino.DIPLOMATO:
			self.pred = self._pred_diplomato
			self.succ = self._succ_diplomato
			self.stampaStato = self._stampaStato_diplomato
			self.salta_anno=self._salta_anno_diplomato

	def _pred_iscritto(self):
		print("Il bambino  e` appena stato iscritto al I anno e non puo` tornare in uno stato precedente")

	def _succ_iscritto(self):
		self.state=Bambino.SECONDOANNO

	def _stampaStato_iscritto(self):
		print("Il bambino e` nello stato",Bambino.ISCRITTO)

	def _salta_anno_iscritto(self):
		self.state = Bambino.TERZOANNO

	def _pred_secondo(self):
		self.state=Bambino.ISCRITTO

	def _succ_secondo(self):
		self.state = Bambino.TERZOANNO

	def _stampaStato_secondo(self):
		print("Il bambino e` nello stato", Bambino.SECONDOANNO)

	def _salta_anno_secondo(self):
		self.state = Bambino.DIPLOMATO

	def _pred_terzo(self):
		self.state=Bambino.SECONDOANNO

	def _succ_terzo(self):
		self.state = Bambino.DIPLOMATO

	def _stampaStato_terzo(self):
		print("Il bambino e` nello stato", Bambino.TERZOANNO)

	def _salta_anno_terzo(self):
		print("Il bambino e` nello stato",Bambino.TERZOANNO, " e non puo` saltare un anno")

	def _pred_diplomato(self):
		self.state=Bambino.TERZOANNO

	def _succ_diplomato(self):
		print("Il bambino  si e` gia` diplomato e non puo` avanzare in uno stato successivo")

	def _stampaStato_diplomato(self):
		print("Il bambino e` nello stato", Bambino.DIPLOMATO)

	def _salta_anno_diplomato(self):
		print("Il bambino e` nello stato",Bambino.DIPLOMATO, " e non puo` saltare un anno")
def main():
	bambino =Bambino()
	bambino.stampaStato()
	bambino.pred()
	bambino.succ()
	bambino.stampaStato()
	bambino.succ()
	bambino.stampaStato()
	bambino.salta_anno()
	bambino.succ()
	bambino.stampaStato()
	bambino.succ()

if __name__== "__main__":
	main()



"""IL programma deve stampare:

Il bambino e` nello stato  iscritto
Il bambino  e` appena stato iscritto al I anno e non puo` tornare in uno stato precedente
Il bambino e` nello stato  alSecondoAnno
Il bambino e` nello stato  alTerzoAnno
Il bambino e` nello stato alTerzoAnno  e non puo` saltare un anno
Il bambino e` nello stato  diplomato
Il bambino  si e` gia` diplomato e non puo` avanzare in uno stato successivo
"""
