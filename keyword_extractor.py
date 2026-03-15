import pytesseract
from pdf2image import convert_from_path
import spacy
import pdfplumber




nlp = spacy.load("en_core_web_sm")

# function to read text from pdf
def extract_text_from_pdf(pdf_path):

    text = ""

    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

    return text

# OCR for scanned/image PDFs
def extract_text_with_ocr(pdf_path):

    text = ""

    # convert pdf pages to images
    pages = convert_from_path(pdf_path)

    for page in pages:
        ocr_text = pytesseract.image_to_string(page)
        text += ocr_text + "\n"

    return text

def clean_text(text):
    
    # remove weird symbols and extra spaces
    text = text.replace("\n", " ")

    # remove strange unicode bullets/icons
    text = text.replace("\uf0e8", " ")

    # make everything lowercase
    text = " ".join(text.split())  # removes extra spaces
    text = text.lower()


    return text

# function to extract keywords
def extract_keywords(text):
    
    text = text.strip()   # remove extra spaces/newlines
    doc = nlp(text)

    ignore_words = [
    "experience", "skills", "projects", "work",
    "age", "student", "board", "india", "kolkata",
    "contact", "website", "qualification", "currently",
    "percent", "%"
    ]
    skill_keywords = [
    "python", "java", "machine learning", "html", "css",
    "react", "javascript", "aws", "devops",
    "web development", "computer science", "cse"
    ]



    keywords = []

    # 1️⃣ noun chunks
    # 1️⃣ noun chunks
    for chunk in doc.noun_chunks:

        phrase = chunk.text.lower().strip()

    # skip if phrase starts with a verb word
        if chunk[0].pos_ == "VERB":
            continue

    # remove generic words but keep useful part
        for word in ignore_words:
            phrase = phrase.replace(word, "").strip()

        if phrase and not any(char.isdigit() for char in phrase):
            keywords.append(phrase)




    # 2️⃣ single-word skills
    for token in doc:
        if token.pos_ == "PROPN":
            word = token.text.lower()

            already_in_phrase = any(word in phrase for phrase in keywords)

            if not already_in_phrase and word not in ignore_words:
                keywords.append(word)
    
    # keep only skill-related keywords
    # keywords = [k for k in keywords if k in skill_keywords or any(k.startswith(skill) for skill in skill_keywords)]


    # split combined skill phrases
    # final_keywords = []
    # for kw in keywords:
    #     for skill in skill_keywords:
    #         if skill in kw and skill not in final_keywords:
    #             final_keywords.append(skill)

    # return final_keywords

    clean_keywords = []

    for k in keywords:
        k = k.strip().lower()

        # remove very short noise
        if len(k) <= 3:
            continue

        # remove OCR bullets / symbols
        if k.startswith(("e ", "-", "~", "©")):
            continue

        # remove pronoun/article starts (universal linguistic rule)
        if k.startswith(("my ", "the ", "an ", "a ")):
            continue

        # remove very long merged header lines
        if len(k.split()) > 6:
            continue

        # split obvious OCR connectors but stay generic
        parts = k.replace(">", " ").replace(",", " ").split(" e ")

        for part in parts:
            part = part.strip()
            if part:
                clean_keywords.append(part)


    # remove duplicates while keeping order
    clean_keywords = list(dict.fromkeys(clean_keywords))

    return clean_keywords







if __name__ == "__main__":
    
    # read text from file
    resume_text = extract_text_from_pdf("resume3.pdf")

    # if pdfplumber finds no text → use OCR
    if not resume_text.strip():
        print("⚡ Using OCR because no selectable text found...")
        resume_text = extract_text_with_ocr("KanchanAgrawal.pdf")
        # print("\n--- OCR TEXT DEBUG ---\n")
        # print(resume_text[:500])   # print first 500 characters


    resume_text = clean_text(resume_text)

    result = extract_keywords(resume_text)

    print("\n--- KEYWORDS FROM FILE ---(KanchanAgrawal)")
    print(result)