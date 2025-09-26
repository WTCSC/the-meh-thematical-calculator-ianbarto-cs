# Calculator  
=========================  
  ____      _            _       _             _               
 / ___|__ _| | ___ _   _| | __ _| |_ ___  _ __(_)_ __   __ _ 
| |   / _` | |/ __| | | | |/ _` | __/ _ \| '__| | '_ \ / _` |  
| |__| (_| | | (__| |_| | | (_| | || (_) | |  | | | | | (_| |  
 \____\__,_|_|\___|\__,_|_|\__,_|\__\___/|_|  |_|_| |_|\__, |  
                                                       |___/   
  
A tiny command-line calculator script with deliberately cheeky messages.  
This README describes what it does, how to run it, known quirks, and quick ways to improve it.  
  
## Overview  
This script is a simple interactive calculator that:  
- Prompts for two numbers  
- Prompts for an operation (`+`, `-`, `*`, `/`, `^`)  
- Shows a short "calculating..." animation (using `time.sleep`)  
- Prints the result and asks if you want to run another calculation  

The original script prints results using `int(...)` which truncates floats. It also includes some rude debug messages — feel free to edit those strings.  
  
## Requirements  
- Python 3.x (3.6+ recommended)  
- No external libraries required (uses only `time.sleep` from the standard library)  

## How to run  
1. Save the script to a file, e.g. `calculator.py`.  
2. Run it from a terminal:  

``bash
python3 calculator.py``  
