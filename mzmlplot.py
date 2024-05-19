import os
import sys
from PyQt6 import uic
from PyQt6.QtGui import *
from PyQt6.QtCore import pyqtSlot, Qt, pyqtSignal
from PyQt6.QtWidgets import *
from PyQt6.uic import loadUi
import pyopenms as oms
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import pandas as pd
from mzmlplot_ui import Ui_MainWindow



class MainWindow(QMainWindow):
    def __init__ (self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.fileselectButton.clicked.connect(self.file_finder)
        self.ui.plotButton.clicked.connect(self.plot)
        self.show()

    def extract_intensity(self, spectrum, mz_value):
        try:
            #Peak pick for closest peak to desired m/z value
            closest_peak = min(spectrum, key=lambda x: abs(x.getMZ() - mz_value))
            #return intensity of the closest peak
            return closest_peak.getIntensity()
        except ValueError: #if a peak is not present, an empty line will be added to the dataframe
            return None

    def file_finder(self):
        #User input for input file location - must be mzml currently
        file_dialog_result = QFileDialog.getOpenFileName()
        selected_file_path = file_dialog_result[0]

        if selected_file_path:
            self.ui.fileLineedit.setText(selected_file_path)

    def plot(self):
        modeboxindex = self.ui.modeBox.currentIndex()
        if modeboxindex == 0:
            self.plotsinglescan()
        elif modeboxindex == 1:
            self.plotmergedscans()
        elif modeboxindex == 2:
            self.plottic()
        elif modeboxindex == 3:
            self.ploteic()


    
    def plotsinglescan(self):
        file = self.ui.fileLineedit.text()
        #create an MSExperiment object to load the mzml file into
        inp = oms.MSExperiment()
        oms.MzMLFile().load(file, inp)

        #In the square brackets, type the scan number you want to view
        scan = [self.ui.scannumberSpinbox.value()]

        #Create a new MSExperiment object to extract the scan to
        filtered = oms.MSExperiment()

        #Add the selected scan to the filtered MSExperiment object
        for k, s in enumerate(inp):
            if k in scan:
                filtered.addSpectrum(s)

        #Set up the plot window - not too important as it can be resized at will when open
        fig, axs = plt.subplots(1)
        fig.set_figheight(4)
        plt.subplots_adjust(hspace=1)

        #setup the axis params for the figure
        s = filtered[0]

        #If you are using profile data, keep this as 'axs.plot'. If using centroid, change to 'axs.stem' and delete ', linewidth = x'
        #You can change the line colour here by changing the colour name in " ", and also change the line thickness
        if self.ui.profileButton.isChecked():
            axs.plot(s.get_peaks()[0],s.get_peaks()[1], self.ui.colourBox.currentText(), linewidth = self.ui.widthBox.value())
        elif self.ui.centroidButton.isChecked():
            markerline, stemlines, baseline = axs.stem(s.get_peaks()[0],s.get_peaks()[1], self.ui.colourBox.currentText(), markerfmt='none')
            plt.setp(stemlines, 'linewidth', self.ui.widthBox.value())

        #set the y-axis upper and lower limits - accepts raw integers or scientific notation
        axs.set_ylim(self.ui.lowySpinbox.value(), self.ui.highySpinbox.value())

        #Set the x-axis upper and lower limit - accepts raw integers or scientific notation
        axs.set_xlim(self.ui.lowxSpinbox.value(), self.ui.highxSpinbox.value())

        #Sets the x/y-axis labels
        axs.set_xlabel("m/z")
        axs.set_ylabel("Counts")

        #sets the y-axis tick labels to scientific notation
        axs.yaxis.set_major_formatter(ticker.FormatStrFormatter('%0.0e'))

        #sets the figure to a tight layout
        fig.tight_layout()

        #shows the figure where you can zoom/resize at will, and save to a file (recommended to save as a .svg for figure scaling)
        plt.show()

    def plotmergedscans(self):
        file = self.ui.fileLineedit.text()

        # load MS data and store as MSExperiment object
        exp = oms.MSExperiment()
        oms.MzMLFile().load(file, exp)

        spectra = exp.getSpectra()

        # Collecting only MS1 spectra
        spectra_ms1 = [s for s in spectra if s.getMSLevel() == 1]
        print(f"Number of MS1 spectra before merge are {len(spectra_ms1)}")

        # merges blocks of MS1
        merger = oms.SpectraMerger()
        merger.mergeSpectraBlockWise(exp)
        param = merger.getParameters()
        param.setValue("block_method:rt_block_size", len(exp.getSpectra()))
        merger.setParameters(param)
        merger.mergeSpectraBlockWise(exp)

        # adjust block size to 10 spectra and merge
        merger = oms.SpectraMerger()

        param = merger.getParameters()
        param.setValue("block_method:rt_block_size", len(exp.getSpectra()))
        merger.setParameters(param)
        merger.mergeSpectraBlockWise(exp)

        spectraMerged = exp.getSpectra()
        spectraMerged_ms1_10scans = [s for s in spectraMerged if s.getMSLevel() == 1]

                #Set up the plot window - not too important as it can be resized at will when open
        fig, axs = plt.subplots(1)
        fig.set_figheight(4)
        plt.subplots_adjust(hspace=1)

        #setup the axis params for the figure
        s = spectraMerged[0]

        #If you are using profile data, keep this as 'axs.plot'. If using centroid, change to 'axs.stem' and delete ', linewidth = x'
        #You can change the line colour here by changing the colour name in " ", and also change the line thickness
        if self.ui.profileButton.isChecked():
            axs.plot(s.get_peaks()[0],s.get_peaks()[1], self.ui.colourBox.currentText(), linewidth = self.ui.widthBox.value())
        elif self.ui.centroidButton.isChecked():
            markerline, stemlines, baseline = axs.stem(s.get_peaks()[0],s.get_peaks()[1], self.ui.colourBox.currentText(), markerfmt='none')
            plt.setp(stemlines, 'linewidth', self.ui.widthBox.value())
        #set the y-axis upper and lower limits - accepts raw integers or scientific notation
        axs.set_ylim(self.ui.lowySpinbox.value(), self.ui.highySpinbox.value())

        #Set the x-axis upper and lower limit - accepts raw integers or scientific notation
        axs.set_xlim(self.ui.lowxSpinbox.value(), self.ui.highxSpinbox.value())

        #Sets the x/y-axis labels
        axs.set_xlabel("m/z")
        axs.set_ylabel("Counts")

        #sets the y-axis tick labels to scientific notation
        axs.yaxis.set_major_formatter(ticker.FormatStrFormatter('%0.0e'))

        #sets the figure to a tight layout
        fig.tight_layout()

        #shows the figure where you can zoom/resize at will, and save to a file (recommended to save as a .svg for figure scaling)
        plt.show()

    def plottic(self):
        file = self.ui.fileLineedit.text()
        exp1 = oms.MSExperiment()
        oms.MzMLFile().load(file, exp1)
        fig, axs = plt.subplots()
        fig.set_figheight(4)
        plt.subplots_adjust(hspace=1)
        for chrom in exp1.getChromatograms():
            retention_times, intensities = chrom.get_peaks()
            axs.plot(retention_times, intensities, self.ui.colourBox.currentText(), linewidth = self.ui.widthBox.value())
        axs.set_xlabel("time (s)")
        axs.set_ylabel("Counts")
        #set the y-axis upper and lower limits - accepts raw integers or scientific notation
        axs.set_ylim(self.ui.lowySpinbox.value(), self.ui.highySpinbox.value())

        #Set the x-axis upper and lower limit - accepts raw integers or scientific notation
        axs.set_xlim(self.ui.lowscanSpinbox.value(), self.ui.highscanSpinbox.value())
        axs.yaxis.set_major_formatter(ticker.FormatStrFormatter('%0.0e'))
        plt.tight_layout()
        plt.show()

    def ploteic(self):
        file = self.ui.fileLineedit.text()

        # load MS data and store as MSExperiment object
        exp1 = oms.MSExperiment()
        oms.MzMLFile().load(file, exp1)

        mz_values = [self.ui.mzSpinbox.value()]
        print(len(exp1.getSpectra()))
        intensity_values = []
        for i in range(0, len(exp1.getSpectra())):
            current_spectrum = exp1.getSpectra()[i]
            for mz_value in mz_values:
                intensity = self.extract_intensity(current_spectrum, mz_value)
                if intensity is not None: # if intensity is none, the value will not be added to the list and the corresponding scan in the final output will read 0
                    intensity_values.append(intensity)
        fig, axs = plt.subplots()
        fig.set_figheight(4)
        plt.subplots_adjust(hspace=1)
        axs.plot(intensity_values, self.ui.colourBox.currentText(), linewidth = self.ui.widthBox.value())

        axs.set_xlabel("Scan")
        axs.set_ylabel("Counts")
        #set the y-axis upper and lower limits - accepts raw integers or scientific notation
        axs.set_ylim(self.ui.lowySpinbox.value(), self.ui.highySpinbox.value())

        #Set the x-axis upper and lower limit - accepts raw integers or scientific notation
        axs.set_xlim(self.ui.lowscanSpinbox.value(), self.ui.highscanSpinbox.value())
        axs.yaxis.set_major_formatter(ticker.FormatStrFormatter('%0.0e'))
        plt.tight_layout()
        plt.legend()
        plt.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    GUI = MainWindow()
    sys.exit(app.exec())