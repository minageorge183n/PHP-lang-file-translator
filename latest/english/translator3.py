from googletrans import Translator
import re 


def translate_php_array(php_code, target_language='ar'):
    lines = php_code.split('\n')
    translator = Translator()

    translated_lines = []
    for line in lines:
        if "['" in line and "']" in line and "=" in line:
            key = line.split("= '")[1].split("';")[0]
            value = line.split("'")[1]

            # Identify placeholders and their corresponding translations
            placeholders = re.findall(r'%s', value)
            translations = [translator.translate(placeholder, dest=target_language).text for placeholder in placeholders]

            # Replace placeholders with their translated values
            for i, placeholder in enumerate(placeholders):
                value = value.replace(placeholder, translations[i], 1)

            translated_line = f"$lang['{key}'] = '{value}';"
            translated_lines.append(translated_line)
        else:
            translated_lines.append(line)

    return '\n'.join(translated_lines)


def save_translated_php_code(php_code, translated_php_code, output_file):
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(translated_php_code)

if __name__ == "__main__":
    php_code = """
$lang['invoice_status_paid']                   = 'Paid';
$lang['invoice_status_unpaid']                 = 'Unpaid';
$lang['invoice_status_overdue']                = 'Overdue';
$lang['invoice_status_not_paid_completely']    = 'Partially Paid';
$lang['invoice_pdf_heading']                   = 'INVOICE';
$lang['invoice_table_item_heading']            = 'Item';
$lang['invoice_table_quantity_heading']        = 'Qty';
$lang['invoice_table_rate_heading']            = 'Rate';
$lang['invoice_table_tax_heading']             = 'Tax';
$lang['invoice_table_amount_heading']          = 'Amount';
$lang['invoice_subtotal']                      = 'Sub Total';
$lang['invoice_adjustment']                    = 'Adjustment';
$lang['invoice_total']                         = 'Total';
$lang['invoice_bill_to']                       = 'bill To';
$lang['invoice_data_date']                     = 'Invoice Date:';
$lang['invoice_data_duedate']                  = 'Due Date:';
$lang['invoice_received_payments']             = 'Transactions';
$lang['invoice_no_payments_found']             = 'No payments found for this invoice';
$lang['invoice_note']                          = 'Note:';
$lang['invoice_payments_table_number_heading'] = 'Payment #';
$lang['invoice_payments_table_mode_heading']   = 'Payment Mode';
$lang['invoice_payments_table_date_heading']   = 'Date';
$lang['invoice_payments_table_amount_heading'] = 'Amount';

    """

    translated_php_code = translate_php_array(php_code)

    # Specify the output file name
    output_file = "translated_output.php"

    # Save the translated content to the output file
    save_translated_php_code(php_code, translated_php_code, output_file)