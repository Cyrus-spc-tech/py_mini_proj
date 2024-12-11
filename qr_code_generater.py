# Import QRCode from pyqrcode 
import pyqrcode 
from pyqrcode import QRCode 
import png as png
  
  
# String which represents the QR code 
s = input("  Enter the site you want to search >> ")
  
# Generate QR code 
url = pyqrcode.create(s) 
  
# Create and save the svg file naming "myqr.svg" 
url.svg("myqr.svg", scale = 8) 
  
# Create and save the png file naming "myqr.png" 
url.png('myqr.png', scale = 6) 
# NOTE: the qr png and svg will save in the same file 