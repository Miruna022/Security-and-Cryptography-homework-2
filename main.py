from pathlib import Path


og_file = Path("mesarosiu_maria")
signatures = Path("signatures")


# used from previous hw
def read(input_file):
    with open(input_file, 'rb') as f:
        return f.read()


def write(output_file, data):
    with open(output_file, 'wb') as f:
        return f.write(data)


def decrypt(data, shift):
    res = []
    for d in data:
        val = (d - shift) % 256
        res.append(val)
    return bytes(res)





def load_signatures(file):
    sig = {}
    with open(file, 'r') as f:
        for line in f:
            name, hex = line.strip().split(",")
            no_space_hex = hex.replace(" ", "")
            sig[bytes.fromhex(no_space_hex)] = name
    return sig


def brute_force(data, sig):
    header = data[:20]
    for shift in range(256):
        res = decrypt(header, shift)
        for byte, name in sig.items():
            if res.startswith(byte):
                return shift, name
    return None, None


sig = load_signatures(signatures)
enc_data = read(og_file)
shift, name = brute_force(enc_data, sig)

if shift is not None:
    print(f"The file you were looking for is of type {name}, found using a {shift} byte shift.")
    decr_data = decrypt(enc_data, shift)
    extension = name.lower()

    if name == "DOC/PPT/XLS":
        longer_header = enc_data[:50]
        if b'word' in decr_data.lower():
            print("This is specifically a DOC file.")
            extension = "doc"
        elif b'excel' in decr_data.lower():
            print("This is specifically an XLS file.")
            extension = "xls"
        elif b'slide' in decr_data.lower():
            print("This is specifically a PPT file.")
            extension = "ppt"
        else:
            print("I have no idea what extension this is")
            
    write(f"decrypted_file.{extension}", decr_data)
    print("Decrypted file was saved!!!")
else:
    print("You did something wrong cuz the type was not found :(")
