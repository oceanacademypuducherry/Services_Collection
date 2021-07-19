import pyttsx3
import PyPDF2

W  = '\033[0m'  # white (normal)
R  = '\033[31m' # red
G  = '\033[32m' # green
O  = '\033[33m' # orange
B  = '\033[34m' # blue
P  = '\033[35m' # purple


speeker = pyttsx3.init()
voices = speeker.getProperty('voices')
speeker.setProperty('voice', voices[1].id)
try:
    book = open('sample.pdf', 'rb')
    pdfReader = PyPDF2.PdfFileReader(book)
    pages = pdfReader.numPages
    print(pages)

    page = pdfReader.getPage(1)
    myText = page.extractText()

    text = page.extractText()
    # myText = 'Something magical was happening in the fish bowl  and he wasn’t  quite ready for what lay in store.  Read this captivating free illustrated book for kids that encourages them to explore and be awed by the many wonders of nature. '
    speeker.say(myText)
    print(G,end='')
    print(myText)
    print(W)

    speeker.runAndWait()
except Exception as e:
    print(R, end='')
    print(e)
    print(W)
    speeker.say(str(e))
    speeker.runAndWait()

