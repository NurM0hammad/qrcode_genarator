import qrcode

text = input("Enter The Text or Url be to converted in Qr code: ")
file_name = input("Enter File name to save the Qr code: ")


def generat_qrcode(text, file_name):

    image_qrcode = qrcode.make(text)
    image_qrcode.save(file_name)


generat_qrcode(text, file_name)
