from googletrans import Translator

def translate_php_array(php_code, target_language='ar'):
    lines = php_code.split('\n')
    translator = Translator()

    translated_lines = []
    for line in lines:
        if "= '" in line and "';'" in line :
            key = line.split("= '")[1].split("';")[0]
            value = line.split("'")[1]

            # Escape %s before translation
            value_escaped = value.replace('%s', '%%s')
            translation = translator.translate(value_escaped, dest=target_language).text

            # Replace %%s back with %s in the translation
            translation = translation.replace('%%s', '%s')
            
            translated_line = f"$lang['{key}'] = '{translation}';"
            translated_lines.append(translated_line)
        else:
            translated_lines.append(line)

    return '\n'.join(translated_lines)


def save_translated_php_code(php_code, translated_php_code, output_file):
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(translated_php_code)

if __name__ == "__main__":
    php_code = """
$lang['submit']               = 'Save';
$lang['added_successfully']   = '%s added successfully.';
    """

    translated_php_code = translate_php_array(php_code)

    # Specify the output file name
    output_file = "translated_output.php"

    # Save the translated content to the output file
    save_translated_php_code(php_code, translated_php_code, output_file)