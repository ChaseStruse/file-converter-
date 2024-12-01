from operator import index

from pypdf import PdfReader


def convert_fareway_receipt_to_dict():
    reader = PdfReader(
        '/Users/chasestruse/Developer/Python/file-converter-service/test_pdf_files/test_fareway_order.pdf'
    )

    page = reader.pages[0]
    extracted = page.extract_text().splitlines()
    extracted = extracted[extracted.index('ITEM UNITS QTY AMOUNT TAX/FOOD') + 1:extracted.index('Thank\xa0you')]
    extracted = [e.replace('\xa0', ' ') for e in extracted]
    for i, e in enumerate(extracted):
        if e.__contains__('Unit'):
            extracted[i] = e[:e.index('Unit')]
        elif e.__contains__('Weight'):
            extracted[i] = e[:e.index('Weight')]
        
    print(extracted)


if __name__ == '__main__':
    convert_fareway_receipt_to_dict()
