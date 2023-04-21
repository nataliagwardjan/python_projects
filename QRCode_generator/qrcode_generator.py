# script to generate QRCode by given via user url address
import qrcode


def generate_qrcode(url, img_name):
    qr = qrcode.QRCode(
        version = 1,
        error_correction = qrcode.constants.ERROR_CORRECT_L,
        box_size = 20,
        border = 5
    )

    qr.add_data(url)
    qr.make(fit = True)
    img = qr.make_image(fill_color = 'black', back_color = 'white')
    img.save(f'{img_name}.png')

url = input("Write url address: ")
img_name = input("Write name of file: ")
generate_qrcode(url, img_name)
