from google.cloud import texttospeech
import PyPDF2

# ---------------CONFIGURATION !IMPORTANT---------------#

# PDF_FILE = "PUT HERE THE PATH OF THE PDF FILE"  # string
# PAGE_NUMBER = "PUT HERE THE PAGE NUMBER"  # integer
# CREDENTIALS = "PUT HERE THE PATH OF JSON FILE FROM GOOGLE API"
# TO GET CREDS VISIT "https://accounts.google.com/v3/signin/identifier?dsh=S1510602019%3A1669057199795509&continue=https%3A%2F%2Fconsole.cloud.google.com%2Fiam-admin%2Fserviceaccounts%2Fdetails%2F118392327969830894897%3Bedit%3Dtrue%2Fkeys%3Fproject%3Dtext-to-speech-tts-369314&followup=https%3A%2F%2Fconsole.cloud.google.com%2Fiam-admin%2Fserviceaccounts%2Fdetails%2F118392327969830894897%3Bedit%3Dtrue%2Fkeys%3Fproject%3Dtext-to-speech-tts-369314&osid=1&passive=1209600&service=cloudconsole&flowName=GlifWebSignIn&flowEntry=ServiceLogin&ifkv=ARgdvAv50fjWAkX78BqwFl8QIAv5aC8pM362SGHJ580OOTAzGyhChU89gGjI4eV2d6LbMi00DQStwQ"

PDF_FILE = "example.pdf"
PAGE_NUMBER = 0
CREDENTIALS = "PUT HERE THE PATH OF JSON FILE FROM GOOGLE API"



# ------------------PDF-----------------------------#
pdfFileObj = open(PDF_FILE, 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

pageObj = pdfReader.getPage(PAGE_NUMBER)
text = pageObj.extractText() + "./n"

pdfFileObj.close()
# --------------------------------------------#

# Instantiates a client
client = texttospeech.TextToSpeechClient.from_service_account_file(CREDENTIALS)
# Set the text input to be synthesized
synthesis_input = texttospeech.SynthesisInput(text=text)
# Build the voice request, select the language code ("en-US") and the ssml
# voice gender ("neutral")
voice = texttospeech.VoiceSelectionParams(
    language_code="en-US", ssml_gender=texttospeech.SsmlVoiceGender.MALE
)
# Select the type of audio file you want returned
audio_config = texttospeech.AudioConfig(
    audio_encoding=texttospeech.AudioEncoding.MP3
)
# Perform the text-to-speech request on the text input with the selected
# voice parameters and audio file type
response = client.synthesize_speech(
    input=synthesis_input, voice=voice, audio_config=audio_config
)
# The response's audio_content is binary.
with open("output.mp3", "wb") as out:
    # Write the response to the output file.
    out.write(response.audio_content)
    print('Audio content written to file "output.mp3"')
