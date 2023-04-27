from pypdf import PdfWriter, PdfReader, PageObject, Transformation
import argparse
import os

parser = argparse.ArgumentParser(description='Convert PDF to double-page format with swapped left and right pages.')
parser.add_argument('-i', '--input', required=True, help='Input PDF file name')
parser.add_argument('-o', '--output', help='Output PDF file name (optional)')

args = parser.parse_args()

input_pdf = args.input

if args.output:
    output_pdf = args.output
else:
    file_name, file_extension = os.path.splitext(input_pdf)
    output_pdf = f"{file_name}_swapped{file_extension}"

reader = PdfReader(input_pdf)
writer = PdfWriter()

p1 = reader.pages[0]
writer.add_page(p1)

for i in range(1, len(reader.pages), 2):
    if i + 1 == len(reader.pages):
        right_page = reader.pages[i]
        writer.add_page(right_page)
        break

    right_page = reader.pages[i]
    left_page = reader.pages[i + 1]

    total_width = left_page.mediabox.right + right_page.mediabox.right
    total_height = max(left_page.mediabox.top, right_page.mediabox.top)

    new_page = PageObject.create_blank_page(width=total_width, height=total_height)

    new_page.merge_page(left_page)
    op = Transformation().translate(tx=left_page.mediabox.right)
    right_page.add_transformation(op)
    right_page.mediabox.left = left_page.mediabox.right
    right_page.mediabox.right = left_page.mediabox.right + right_page.mediabox.right
    new_page.merge_page(right_page)

    writer.add_page(new_page)

with open(output_pdf, mode='wb') as f:
    writer.write(f)
