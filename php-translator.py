from translate import Translator
import re


def translate_php_text(php_text, source_lang='en', target_lang='ar'):
    translator = Translator(to_lang=target_lang)

    translated_lines = []
    lines = php_text.splitlines()

    for line in lines:
        if re.match(r"\s*\$lang\['(.+)'\]\s*=\s*'(.+)';\s*", line):
            match = re.match(r"\s*\$lang\['(.+)'\]\s*=\s*'(.+)';\s*", line)
            key, value = match.group(1), match.group(2)

            translated_value = translator.translate(value)
            translated_line = f"$lang['{key}'] = '{translated_value}';"
            translated_lines.append(translated_line)
        else:
            translated_lines.append(line)



    return '\n'.join(translated_lines)

# Example usage:
input_php_text = """
 
# General
$lang['id']                   = 'ID';
$lang['name']                 = 'Name';
 
"""

translated_php_text = translate_php_text(input_php_text)

 
output_file_path = "translated_output.php"
with open(output_file_path, "w", encoding="utf-8") as output_file:
    output_file.write(translated_php_text)

print(f"Translated PHP text saved to {output_file_path}")
