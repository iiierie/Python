import qrcode as qc
#qr code module has QRCode class for more control

qr = qc.QRCode(
    version = 1,
    error_correction = qc.constants.ERROR_CORRECT_L,
    box_size = 10,
    border = 4
)
while True:
    string = input("Enter any link or data to make the QRCODE of:")
    fore, back = input("Enter color of qrcode and bgcolor with space (Type D D for default): ").split()
    if fore == "D" and back == "D" : #default white black qr
        fore = "black"
        back = "white"
    filename = input("What would you like to name the file? ")

    qr.add_data(string)
    qr.make(fit=True)
    image = qr.make_image (fill_color = fore,back_color = back)
    image.save(filename+".png")
    print("Your QR Code has been generated successfully and saved to the location where the main file is.")
    choice = input("Make another QR? Y/N ").upper()
    if choice == "N":
        print("Thank you for using our service.")
        break

'''
--------------------------------------------------------------------------------------------------------------------
https://pypi.org/project/qrcode/ documentation
general format :
import qrcode
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data('Some data')
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
'''