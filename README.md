# RevEndian
Simple CLI Tool to reverse Little-endian to Big-endian and vise versa

## Retrictions
1. CLI (Command Line Interface), no GUI (Graphical User Interface)
2. Can only display results as a hexdump or ASCII string
3. Reviece and output only file type

# Installation & Usage of the script
1. Download and install python in the Microsoft Store or Official Website [python.org](https://www.python.org/downloads/).
2. copy repository to the local directory.
```
https://github.com/oujisan/RevEndian.git
```
3. Open your terminal or CMD, make sure you're in path of RevEndian before run the script.
4. Run script.
```
python3 revEndian.py
```
This will lead to the instructions for using the script and an example.

# Argument Documentation
**USAGE:** 
```
python3 revendian.py [OPTION] <input_file> <output_file>
```
**OPTIONS:**
`-h`, `--help`       Show this help message and exit.
`-x`, `--hexdump`    Save output as hexdump.
`-f`, `--file`       Save output as file.

# Usage Example
```
python3 revEndian.py -x chall output.hex
```
```
python3 revEndian.py -f chall output.png
```

# Build-In
Python 3.13.1

Created date: Jum'at, 07 Februari 2025