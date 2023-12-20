from googletrans import Translator
import re

def read_php_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    return content

def write_php_file(file_path, content):
    new_file_path = file_path + '.translated'
    with open(new_file_path, 'w') as file:
        file.write(content)

def translate_php_file(php_file_path, target_language):
    translator = Translator()

    content = read_php_file(php_file_path)

    matches = re.findall(r'\$lang\[\'(.*?)\'\]\s*=\s*\'(.*?)\';', content)
    translated_texts = {}

    for match in matches:
        key, value = match
        translated_text = translator.translate(value, dest=target_language).text
        translated_texts[key] = translated_text

    new_content = content
    for key, value in translated_texts.items():
        new_content = re.sub(r'\$lang\[\'' + key + '\'\]\s*=\s*\'.*?\';', "$lang['" + key + "'] = '" + value + "';", new_content)

    write_php_file(php_file_path, new_content)

if __name__ == "__main__":
    php_file_path = "/Users/macbookpro/Desktop/domain and host/latest/english/english_land_mini.php"
    target_language = "ar"
    translate_php_file(php_file_path, target_language)