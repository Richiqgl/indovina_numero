from view import View
from model import Model
import flet as ft


class Controller(object):
    def __init__(self, view: View):
        self._view = view
        self._model = Model()


    def handleNuova(self,e):
        self._view._txtMrim.value=self.getMmax()
        self._view.btnProva.disabled=False
        self._view._txtTentativo.disabled=False
        self._view.lvOut.controls.clear()
        self._view.lvOut.controls.append(ft.Text("Indovina il numero",color="green"))
        self._model.inizializza()
        self._view.update()
    def handleProva(self,e):
        tentativo=self._view._txtTentativo.value
        self._view._txtTentativo.value=""

        try:
            inttentativo=int(tentativo)
        except ValueError:
            self._view.lvOut.controls.append(ft.Text("Il tentativo deve essere intero"))
            self._view.update()
            return
        (mRim,result)=self._model.indovina(inttentativo)
        self._view._txtMrim.value = self._model.Mrim
        if mRim==0:
            self._view.lvOut.controls.append(ft.Text("hai perso il segreto era "+str(self._model.Segreto)))
            self._view.update()
            return
        if result== 0:
            self._view.lvOut.controls.append(ft.Text("Hai vinto"))
            self._view.btnProva.disabled = True
            self._view.update()
        if result==1:
            self._view.lvOut.controls.append(ft.Text("Il segreto è piu grande"))
            self._view.update()
        if result==-1:
            self._view.lvOut.controls.append(ft.Text("Il segreto e piu piccolo"))
            self._view.update()

    def getNmax(self):
        return self._model.Nmax
    def getMmax(self):
        return self._model.Mmax
    def getMrim(self):
        return self._model.Mrim
