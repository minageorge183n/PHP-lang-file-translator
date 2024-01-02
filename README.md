Translation Helper for PHP Files
This Python script is designed to assist users in translating PHP language files easily. It utilizes the translate library to automatically translate the values in PHP language files from one language to another. The primary purpose is to simplify the translation process by automating the conversion of key-value pairs within the language file.

Usage
1-Install the required library by running the following command:
pip install translate
2-Replace the example PHP text in the input_php_text variable with your own language file content. Make sure to maintain the same format for key-value pairs as demonstrated in the provided example:
input_php_text = """
 
# General
$lang['id']                   = 'ID';
$lang['name']                 = 'Name';
 """
Important Notes

1-Set the source and target languages using the source_lang and target_lang variables. By default, the source language is set to English ('en') and the 
target language is set to Arabic ('ar'). Modify these variables if you are working with different languages.
2-Ensure that the translate library supports the languages you are working with. Some languages may have limitations or require additional configuration.

Feel free to customize the script based on your specific needs. If you encounter any issues or have suggestions for improvement, please open an issue or submit a pull request on GitHub.

Happy translating!
