import qrcode
from pystyle import *
print(Box.Lines('[+] Abood[+]'))
Write.Print('[+] this program for QRcode\n\n',Colors.purple_to_blue,interval=0.1)
print(Box.DoubleCube('QRcode'))
text = Write.Input('Enter your texet : ',Colors.blue_to_purple,interval=0.1)
qr = qrcode.make(text)
qr.save('D:\\qr5.jpg')
Write.Print('\n The QRcode Saved \n ',Colors.green)
input('\n..........\n')