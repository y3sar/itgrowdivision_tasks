import argparse
from googletrans import Translator

def translate_bangla_to_french(text):
    translator = Translator()
    translation = translator.translate(text, src='bn', dest='fr')
    return translation.text

def main():
    parser = argparse.ArgumentParser(description='Translate Bengali to French using Google Translate API')
    parser.add_argument('text', type=str, help='The Bengali text to translate')
    args = parser.parse_args()

    translated_text = translate_bangla_to_french(args.text)
    print(f'Translation (Bangla to French): {translated_text}')

if __name__ == '__main__':
    main()
