## PDF to Audio Converter using Google Cloud Text-to-Speech API

This script converts a PDF file to an audio file using the Google Cloud Text-to-Speech API. The audio file is saved in MP3 format.

### Prerequisites

- Python 3.6 or higher
- PyPDF2 module (install using `pip install pypdf2`)
- google-cloud-texttospeech module (install using `pip install google-cloud-texttospeech`)
- A Google Cloud Platform project with the Text-to-Speech API enabled
- A service account key file for the project in JSON format

### Configuration

Before running the script, make sure to set the following values in the CONFIGURATION section at the beginning of the script:

- `PDF_FILE`: The path to the PDF file that you want to convert to audio.
- `PAGE_NUMBER`: The page number of the PDF that you want to convert to audio (0-indexed).
- `CREDENTIALS`: The path to the JSON file containing your service account key.

### Running the script

To run the script, open a terminal window, navigate to the directory containing the script, and run the following command:
```bash
python pdf_to_audio.py
```


The script will convert the specified page of the PDF to an audio file and save it as `output.mp3` in the same directory as the script.

### How it works

The script follows these steps to convert the PDF to audio:

1. Import the necessary modules: `texttospeech` from the `google.cloud` library and `PyPDF2`.
2. Define the path to the PDF file, the page number of the PDF to be converted, and the path to the Google Cloud API credentials file.
3. Open the PDF file and create a `PdfFileReader` object using `PyPDF2`.
4. Extract the text from the specified page of the PDF using the `getPage` and `extractText` methods of the `PdfFileReader` object.
5. Instantiate a `TextToSpeechClient` object using the `from_service_account_file` method and the path to the Google Cloud API credentials file.
6. Define the text to be synthesized using the `SynthesisInput` object, and specify the language and voice gender using the `VoiceSelectionParams` object.
7. Specify the audio file type using the `AudioConfig` object.
8. Call the `synthesize_speech` method of the `TextToSpeechClient` object, passing in the synthesis input, voice parameters, and audio configuration as arguments. This method returns a response object containing the synthesized audio data.
9. Write the audio data to an MP3 file using the `write` method of the `out` file object.

That's it! You now have a script that can convert a PDF file to an audio file using the Google Cloud Text-to-Speech API.
