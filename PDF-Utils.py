import shutil
import os
import sys
import subprocess
from PyPDF2 import PdfFileMerger, PdfFileReader, PdfFileWriter
from PyQt5.QtWidgets import QApplication, QFileDialog, QDialog, QMainWindow, QMessageBox
from PyQt5.QtCore import *
from UserInterface import *


class App(QMainWindow):
	def __init__(self):
		super().__init__()
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		self.setWindowTitle("PDF Utils")
		self.setWindowIcon(QtGui.QIcon('icon.png'))
		self.ui.openFile.clicked.connect(self.openFile)
		self.ui.rangePages.setDisabled(True)
		self.ui.extractPages.setDisabled(True)
		self.ui.extractPages.toggled.connect(self.ui.rangePages.setEnabled)
		self.ui.openFile.setDisabled(True)
		self.ui.mergeDocs.setDisabled(True)
		self.ui.clearFields.setDisabled(True)
		self.ui.clearFields.clicked.connect(self.clearFields)
		self.listDocs = QDialog(self)
		self.docsLayout = QtWidgets.QVBoxLayout(self.listDocs)
		self.ui.editListOfDocs.clicked.connect(self.editSelection)
		self.ui.editListOfDocs.clicked.connect(self.checkRemoveButton)
		self.remove = QtWidgets.QPushButton(text="Remove")
		self.add = QtWidgets.QPushButton(text="Add")
		self.buttonsLayout = QtWidgets.QHBoxLayout()
		self.buttonsLayout.addWidget(self.remove)
		self.buttonsLayout.addWidget(self.add)
		self.sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding,
		                                        QtWidgets.QSizePolicy.Expanding)
		self.add.setSizePolicy(self.sizePolicy)
		self.add.setMinimumSize(350, 50)
		self.add.setMaximumSize(13000000, 50)
		self.remove.setSizePolicy(self.sizePolicy)
		self.remove.setMinimumSize(350, 50)
		self.remove.setMaximumSize(13000000, 50)
		self.remove.clicked.connect(self.removeDocuments)
		self.remove.clicked.connect(self.checkRemoveButton)
		self.docsLayout.addLayout(self.buttonsLayout)
		self.add.clicked.connect(self.addDocuments)
		self.ui.OK.clicked.connect(self.execute)
		self.show()

	def editSelection(self):
		self.listDocs.show()
		self.updatePdfList()

	def updatePdfList(self):
		self.pdfs = [widget for widget in self.subWidgets(self.docsLayout) if isinstance(widget, QtWidgets.QCheckBox)]
		self.pdfs_text = [widget.text() for widget in self.pdfs]

	def enableRadios(self, pdfs):
		if len(pdfs) >= 1:
			if len(pdfs) == 1:
				self.ui.extractPages.setEnabled(True)
				self.ui.rangePages.setEnabled(True)
				self.ui.mergeDocs.setDisabled(True)
			elif len(pdfs) > 1:
				self.ui.mergeDocs.setEnabled(True)
				self.ui.extractPages.setDisabled(True)
				self.ui.rangePages.setDisabled(True)
		else:
			self.ui.mergeDocs.setDisabled(True)
			self.ui.extractPages.setDisabled(True)
			self.ui.rangePages.setDisabled(True)

	def addDocuments(self):
		self.updatePdfList()
		additions = QFileDialog.getOpenFileNames(self, caption="Select PDF documents", filter='PDF Files (*.pdf)')[0]
		for index, doc in enumerate(additions):
			if doc not in self.pdfs_text:
				checkbox = QtWidgets.QCheckBox(doc)
				checkbox.setText(doc)
				self.pdfs.append(checkbox)
				self.docsLayout.addWidget(checkbox, index)
		self.remove.setEnabled(True)
		self.enableRadios(self.pdfs)

	@staticmethod
	def subWidgets(layout):
		widgets = (layout.itemAt(i).widget() for i in range(layout.count()))
		return widgets

	def checkRemoveButton(self):
		if len(self.pdfs) != 0:
			self.remove.setEnabled(True)
		else:
			self.remove.setDisabled(True)

	def removeDocuments(self):
		self.updatePdfList()
		for widget in self.subWidgets(self.docsLayout):
			if isinstance(widget, QtWidgets.QCheckBox):
				if widget.isChecked():
					widget.deleteLater()
					self.pdfs.remove(widget)
					self.listDocs.resize(250, self.listDocs.minimumHeight())
		self.checkRemoveButton()
		self.enableRadios(self.pdfs)

	def clearFields(self):
		self.ui.openFile.setDisabled(True)
		self.ui.outputName.clear()
		for widget in self.subWidgets(self.docsLayout):
			if isinstance(widget, QtWidgets.QCheckBox):
				widget.deleteLater()
				self.pdfs.remove(widget)
		self.updatePdfList()

	def mergeDocs(self, pdfs):
		new_file = self.ui.outputName.text()
		merger = PdfFileMerger()
		if pdfs:
			while pdfs:
				pdf = pdfs[0]
				with open(file=pdf, mode="rb") as file:
					file = PdfFileReader(file)
					merger.append(file)
				pdfs.remove(pdf)
		merger.write(new_file)
		self.ui.openFile.setEnabled(True)

	def execute(self):
		self.updatePdfList()
		if os.path.exists(self.ui.outputName.text()):
			if self.overWrite():
				self.mergeDocs(pdfs=self.pdfs_text)
			else:
				pass
		else:
			self.mergeDocs(pdfs=self.pdfs_text)

	def openFile(self):
		folder = os.getcwd()
		file = os.path.join(folder, self.ui.outputName.text())
		if sys.platform == "win32":
			os.startfile(file)
		else:
			opener = "xdg-open" if sys.platform == "linux" else "open"
			subprocess.call([opener, file])

	def overWrite(self):
                warning = QMessageBox()
                warning.setIcon(QMessageBox.Question)
                warning.setText("The file name you have selected already exists. Do you wish to overwrite?")
                warning.setWindowTitle("Path exists.")
                warning.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
                choice = warning.exec_()
                yes, no = 16384, 65536
                if choice == yes:
                        return True
                elif choice == no:
                        return False

	def extractPages(self, doc):
		new_folder = ".temp"
		try:
			os.mkdir(new_folder)
		except FileExistsError:
			pass

		range_ = self.ui.rangePages.text().split("-")
		from_ = range_[0]
		to_ = range_[1] if len(range_) == 2 else (from_ + 1)
		every_ = range_[2] if len(range_) == 3 else 1
		inputPdf = PdfFileReader(open(doc, "rb"))
		output = PdfFileWriter()
		for page in inputPdf.numPages[from_:to_:every_]:
			output.addPage(inputPdf.getPage(page))

		with open("test.pdf", "wb") as outputStream:
			output.write(outputStream)
# os.remove(new_folder)


if __name__ == "__main__":
	app = QApplication(sys.argv)
	w = App()
	w.show()
	sys.exit(app.exec_())
