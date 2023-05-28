import qrcode as qc

# simple mode
string = input("Enter any link or data to make the QRCODE of:")
filename = input("What would you like to name the file? ")

image = qc.make(string)
image.save(filename+".png")
print("Done. Go check your directory.")

'''
------------------------------------------------------------------------------------
general:
image = qr.make("link or any string")
image.save("filename.png")
'''