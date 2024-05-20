# Basic-mzml-plotter
A very basic mzml file plotting program that can plot single scans, merge all scans from a file, plot the TIC, and plot an EIC of a chosen m/z value.

I developed this quickly for myself after needing a way to plot both thermo and waters MS files. I had a lot of MALDI-MS analyses with ~100 scans each with only one sample per file, and wanted to easily combine all the scans and plot them in a similar way regardless of the origin instrument (e.g I had access to masslynx, but not xcalibur).  

I found that none of the popular free mzml analysis platforms (mzmine, openchrom, seeMS, etc.) could just merge all the scans of a file (at least not in a user friendly way that I could find), and instead forced you to look at only individual scans. This might be only useful for me but hopefully others can find it helpful!

# Requirements
-PyQT6

-pyOpenMS

-matplotlib

# Install

Download both the mzmlplot.py and mzmlplot_ui.py files into the same folder. To run the program, run the mzmlplot.py file.

# Usage

-Single scan: Plots a single user defined scan

-Combine scans: Merges all scans of a file (using pyOpenMS SpectraMerger)

-Plot TIC: Extracts the total ion current

-Plot EIC: Extracts the extracted ion current for a user defined m/z value

For single scan plotting, combined scan plotting, and TIC plotting, profile or centroid data is fine (profile will generate a standard plot, centroid will generate a stem plot without markers). For EIC plotting, the data should be centroided for the peak finding algorithm to work properly.

Select the mzml file you want to plot with the select file button. 

If you want to only plot a single scan, define the scan in the scan number box (otherwise the scan number box does nothing).

For EIC plotting, input the target m/z value in the m/z value box (higher m/z accuracy is better for the algorithm).

The plot settings options should hopefully be self explanatory!

When you click 'plot', this will open up the plotted mzml file in a standard matplotlib plot window where the plot can be manipulated at will, and saved in various file formats (I recommend SVG).

Enjoy!


