import xlrd

def vcfWriter(name, phone):
    vcfLines = []
    vcfLines.append('BEGIN:VCARD')
    vcfLines.append('VERSION:4.0')
    vcfLines.append(f'FN:{name}')
    vcfLines.append(f'TEL:{phone}')
    vcfLines.append('END:VCARD')
    vcfString = '\n'.join(vcfLines) + '\n'
    return vcfString

user_file = "input.xlsx"

wb = xlrd.open_workbook(user_file)
sheet = wb.sheet_by_index(0)

with open('contacts.vcf', 'w', encoding="utf-8") as fhand:
    for row in range(sheet.nrows):
        name = sheet.cell_value(row,0)
        phone = sheet.cell_value(row,1)
        fhand.write(vcfWriter(name, phone))
