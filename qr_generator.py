import qrcode
import sys


def generate_qr_code(input_file):
    try:
        # Read the input file
        with open(input_file, 'r') as file:
            lines = file.readlines()

        # Extract URL and filename
        if len(lines) < 2:
            raise ValueError(
                "Input file must contain at least 2 lines (URL and filename)")

        url = lines[0].strip()
        output_filename = lines[1].strip()

        # Generate QR code
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(url)
        qr.make(fit=True)

        # Create and save QR code image
        img = qr.make_image(fill_color="black", back_color="white")
        img.save(output_filename)

        print(f"QR code generated successfully and saved as {output_filename}")

    except FileNotFoundError:
        print(f"Error: The file '{input_file}' was not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python qr_generator.py <input_file.txt>")
    else:
        generate_qr_code(sys.argv[1])
