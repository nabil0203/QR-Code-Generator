import qrcode
#Library - make(data text value url{a function}) --> qrcode

text = input("Enter the Text or Url: ")

fileName = input("Enter File name with jpg/png Extension: ")


def generate_qr__code(text, fileName):
    
    #Convert text or url to qrcode
    image_qrcode = qrcode.make(text)  

    #Save QR code Image
    image_qrcode.save(fileName)


generate_qr__code(text, fileName)