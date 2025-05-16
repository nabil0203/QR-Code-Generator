import qrcode               # importing the qrcode library


# text = input("Enter the Text or Url: ")
# fileName = input("Enter File name with jpg/png Extension: ")


# function
def generate_qr_code(filePath):
    
    # Handling the file
    my_file = open(filePath, "r")
    line = my_file.readlines()
    my_file.close()

    # extracting the input of input.txt
    text = line[0].strip()
    fileName = line[1].strip()


    #Convert text/url to qrcode
    image_qrcode = qrcode.make(text)

    #Save QR code Image
    image_qrcode.save(fileName)


# funtion call
generate_qr_code("input.txt")