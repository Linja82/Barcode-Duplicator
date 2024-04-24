import time
import numbers
import tkinter as tk
from PIL import Image
from barcode import *
from io import BytesIO
from barcode.writer import ImageWriter
from brother_ql.conversion import convert
from brother_ql.backends.helpers import send
from brother_ql.raster import BrotherQLRaster

###################### MAINTENANCE MODE ######################
maintenanceMode = False  # Enabling maintenance mode will stop the code from sending the print commands to the printer, but everything else should function correctly

#   Printer Code Below   #

# Setting Printer Specificiations
backend = 'network'    # 'pyusb', 'linux_kernal', 'network'
model = 'QL-1060N' 
printer = 'tcp://00.00.000.000'    

qlr = BrotherQLRaster(model)
qlr.exception_on_warning = True

labelSizeOptions = [       # Label sizes that the printer can support
    '12mm endless',
    '29mm endless',
    '38mm endless',
    '50mm endless',
    '54mm endless',
    '62mm endless',
    '62mm endless (black/red/white)',
    '102mm endless',
    '17mm x 54mm die-cut',
    '17mm x 87mm die-cut',
    '23mm x 23mm die-cut',
    '29mm x 42mm die-cut',
    '29mm x 90mm die-cut',
    '38mm x 90mm die-cut',
    '39mm x 48mm die-cut',
    '52mm x 29mm die-cut',
    '62mm x 29mm die-cut',
    '62mm x 100mm die-cut',
    '102mm x 51mm die-cut',
    '102mm x 152mm die-cut',
    '12mm round die-cut',
    '24mm round die-cut',
    '58mm round die-cut']

##################### GUI INIT #####################

window = tk.Tk()
window.geometry("400x400")
window.title("Barcode Duplicator")

def GenerateBarcode(barcodeNumber):
    barcode = BytesIO()
    Code128(barcodeNumber, writer=ImageWriter()).write(barcode)

    resized = Image.open(barcode).resize((991, 306))
    
    return resized
    
    
def PrintBarcode():      
    instructions = convert(
        qlr=qlr, 
        images=[GenerateBarcode(barcodeValue.get())],    #  Takes a list of file names or PIL objects.
        label='29x90', 
        rotate='90',    # 'Auto', '0', '90', '270'
        threshold=35.0,    # Black and white threshold in percent.
        dither=False, 
        compress=False, 
        dpi_600=False, 
        hq=True,    # False for low quality.
        cut=True
    )
    
    for x in range(int(numTimes.get())):
        if not maintenanceMode:
            send(instructions=instructions, printer_identifier=printer, backend_identifier=backend, blocking=True)
    
    statusLabel.config(text="Printed %d labels." % int(numTimes.get()))


barcodeLabel = tk.Label(text="Enter barcode:", font=20).place(x=128, y=10)

barcodeValue = tk.Entry(bd=5, width=15, font=10)
barcodeValue.place(x=110, y=40)
    
numTimesLabel = tk.Label(text="Number of copies:", font=20).place(x=115, y=90)
    
numTimes = tk.Entry(bd=5, width=5, font=10)
numTimes.insert(0, "1")
numTimes.place(x=165, y=120)

labelSizeMenuTitle = tk.Label(text="Label Size:", font=20).place(x=40, y=170)

labelSize = tk.StringVar()
labelSize.set('29mm x 90mm die-cut')
labelSizeMenu = tk.OptionMenu(window, labelSize, *labelSizeOptions)
labelSizeMenu.place(x=40, y=200)

statusInfoLabel = tk.Label(text="Status:", font=20).place(x=40, y=240)

statusLabel = tk.Label(text="Idle...")
statusLabel.place(x=40, y=270)
    
printButton = tk.Button(text="Print Barcodes", width=20, height=2, font=10, fg="white", bg="#004c9b", command=PrintBarcode)
printButton.place(x=83, y=320)

window.mainloop()