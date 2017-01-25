from lxml import html

def parse_changes(bill_file):
    rv = ''
    tree = html.parse(bill_file)
    bill_rows = tree.xpath('/html/body/table[2]/tbody/tr/td[2]')
    for row in bill_rows:
        row_text = row.text or ''
        row_text = row_text.strip()
        if len(row_text) > 0:
            rv = '{}\n{}'.format(rv, row_text)
    return rv

if __name__ == '__main__':
    parse_changes('/Users/jeffrey/Work/onesiphore/tests/example_docs/84R_HB4.htm')