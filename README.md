# Barcode-Duplicator
Python app with GUI for duplicating barcodes using a Brother QL-1060N label printer.

# First Time Setup
1. Line 18 of the code must be updated depending on which connection method you use (pyusb, linux_kernel, network).
   - The default is "network"
3. If you are using a different Brother QL label printer model, you must update line 19 of the code to match your printer model.
4. Line 20 also needs to be updated to match your setup.

# Usage
1. Using a barcode scanner or manually entering the desired number into the first entry box.
     
   ![First Entry Box](https://github.com/Linja82/Barcode-Duplicator/blob/main/Images/Barcode%20Duplicator%20V1.1%20Screenshot%20First%20Entry%20Box.png)
3. Enter the desired number of duplicates into the second entry box. The default is one copy.
     
   ![Second Entry Box](https://github.com/Linja82/Barcode-Duplicator/blob/main/Images/Barcode%20Duplicator%20V1.1%20Screenshot%20Second%20Entry%20Box.png)
5. Ensure the correct label size is selected in the drop-down menu.
   - Currently, only 29mm x 90mm die-cut is tested to be working
   
   ![Drop-down Menu](https://github.com/Linja82/Barcode-Duplicator/blob/main/Images/Barcode%20Duplicator%20V1.1%20Screenshot%20Drop-down%20Menu.png)
6. Click "Print Barcodes"

# Notes
- This app uses the brother_ql library
