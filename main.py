import os
import aspose.words as asp

# cd = os.chdir('./Documents/Personal/GitHub/PDF_to_Word/PDF_To_Word/')
print(os.getcwd())

pdf_file_name = input("Enter the File Name without the extension: ")+".pdf"
pdf_file = open(pdf_file_name,"rb")
pdf = asp.Document(pdf_file)

output_file = input("Enter the Output File Name: ")
output_file_name = output_file + ".docx"
pdf.save(output_file_name)

