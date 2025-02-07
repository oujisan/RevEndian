import sys
import binascii


def helpMessage():
    print("[SIMPLE REVERSE ENDIAN by oujisan]")
    print("""USAGE: python3 revendian.py [OPTION] <input_file> <output_file>

OPTIONS:
    -h, --help       Show this help message and exit.
    -x, --hexdump    Save output as hexdump.
    -f, --file       Save output as file.
""")

def endianessReverse(inputfile):
    hexData = ""
    bytesReserved = []
    try:
        with open(inputfile,'rb') as file:
            fileRead = file.read()
            data = fileRead.hex()

            for i in range(0,len(data),8):
                chunk = data[i:i+8]
                byte4 = [chunk[j:j+2] for j in range(0,len(chunk),2)]
                byte4.reverse()
                bytesReserved.append(''.join(byte4).strip())
            hexData = ''.join(bytesReserved)
        return hexData
    
    except Exception as ex:
        print(f"Error: {ex}")

def hexDump(hexCode,outputfile='output.hex'):
    try:
        formatted_hex = "\n".join([hexCode[i:i+60] for i in range(0, len(hexCode), 60)])

        with open(outputfile, 'w') as file:
            file.write(formatted_hex)
        print(f"Save Successfull on {outputfile}")

    except Exception as ex:
        print(f"Error: {ex}")


def hexDecoding(hexCode,outputfile='output.txt'):
    try:
        with open(outputfile,'wb') as file:
            hexDecode = binascii.unhexlify(hexCode)
            file.write(hexDecode)
            print(f"Save Successfull on {outputfile}")
    except Exception as ex:
        print(f"Error: {ex}")
        
def main():
    try:
        if len(sys.argv) > 1:
            reverse = endianessReverse(sys.argv[2])
            formInput = sys.argv[1].lower().strip()
            if formInput in ['-h', '--help']:
                helpMessage()
            elif formInput in ['-x', '--hexdump']:
                if len(sys.argv) > 3:
                    hexDump(reverse, sys.argv[3])
                else:
                    hexDump(reverse)
            elif formInput in ['-f', '--file']:
                if len(sys.argv) > 3:
                    hexDecoding(reverse, sys.argv[3])
                else:
                    hexDecoding(reverse)
            else:
                print("Error: Invalid argument! Use -h or --help for usage.")
                sys.exit(1)
        else:
            helpMessage()
            sys.exit(0)
    except Exception as ex:
        print(f"Error: {ex}")
        helpMessage()
        sys.exit(1)

if __name__ == "__main__":
    main()