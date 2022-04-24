from docx import Document

numbersdone = 0
numberoffixes = 0

doc = Document('doc.docx')
for para in doc.paragraphs:
    newtxt = ''
    for char in para.text:
        if char in '1234567890':
            numberoffixes += 1
            if numbersdone == 0:
                newtxt += char
                numbersdone +=1
            else:
                newtxt = newtxt[:-1*numbersdone] + char + newtxt[-1*numbersdone:]
                numbersdone += 1
        else:
            newtxt += char
            numbersdone = 0

    para.text = newtxt
print('in total I fixed', numberoffixes)
doc.save('fixed.doc.docx')
