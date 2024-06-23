# PDF-Reader
A simple PDF Text-to-Speech Reader, with a simple UI.



markdown
# PDF Text to Speech Application

This is a Python application that extracts text from a PDF file and converts it to speech using the `pdfminer.six` and `pyttsx3` libraries. The application also features a graphical user interface (GUI) built with `tkinter` to make it easy for users to interact with the program.

## Features

- Select a PDF file using a file dialog.
- Specify the starting page number for text extraction.
- Specify the interval of pages after which the application prompts to continue.
- Converts the extracted text to speech.
- User-friendly GUI for easy interaction.

### Prerequisites

- Python 3.x
- `pdfminer.six`
- `pyttsx3`
- `tkinter` (usually comes pre-installed with Python)

### Install Required Packages

Use the following commands to install the required packages:

```sh
pip install pdfminer.six pyttsx3
```

## Usage
USE the application version 
OR
1. Clone the repository or download the script.
2. Run the script:

```sh
python pdf_text_to_speech.py
```

3. Use the GUI to:
   - Browse and select a PDF file.
   - Enter the starting page number.
   - Enter the page interval for when the "Continue" prompt should appear.
   - Click the "Start" button to begin text extraction and speech conversion.

## How It Works

1. The user selects a PDF file and specifies the starting page number and page interval.
2. The application extracts text from the specified starting page and converts it to speech.
3. The application continues to extract and convert text to speech for the specified interval of pages.
4. After the interval, the application prompts the user to continue or stop.

## Code Overview

- `PDFTextToSpeechApp`: The main class that initializes the Tkinter GUI and handles user interactions.
- `browse_file`: Opens a file dialog for the user to select a PDF file.
- `extract_text_from_pdf`: Extracts text from a specified page of the PDF file.
- `text_to_speech`: Converts the extracted text to speech using the `pyttsx3` library.
- `start`: The main function that handles the extraction and speech conversion process, including user prompts.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any bugs or feature requests.

## Acknowledgements

- [pdfminer.six](https://github.com/pdfminer/pdfminer.six)
- [pyttsx3](https://pyttsx3.readthedocs.io/en/latest/)

