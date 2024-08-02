# Zip Bomb Generator
(This Project is unfinished)
## Overview

The Zip Bomb Generator is a Python script designed to create zip bomb files quickly and efficiently. A zip bomb is a malicious archive file designed to consume excessive system resources or cause denial-of-service conditions when extracted. This project was developed as part of a project/presentation on malware for a computer science course.

## Features

1. Generates zip bomb files with customizable parameters:
  - Number of directories
  - Number of files per directory
  - Size of each text file
  - Content of the text files
2. Utilizes multithreading to optimize file creation process for faster execution
3. Automatically creates a zip bomb archive file
4. Includes cleanup process to delete temporary files and directories after creating the zip bomb

## Prerequisites

   - Python 3.x
   - Dependencies: None

## Usage
1. Clone the repository to your local machine.
2. Open a terminal and navigate to the project directory.
3. Run the script using Python:

```bash
python ZIPBOOM.py
```

4. Follow the on-screen prompts to specify the parameters for the zip bomb:
        -Number of directories
        -Number of files per directory
        -Size of each text file (in MB)
        -Content of the text files
5. Once the script completes execution, the zip bomb archive file (bomb.zip) will be created in the project directory.

## Disclaimer

This project is for educational purposes only and should be used responsibly and ethically. Generating and distributing zip bomb files without proper authorization may be illegal and unethical. The developers of this project are not responsible for any misuse or damage caused by the use of this software.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

