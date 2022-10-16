# Code by @AmirMotefaker

# Merge Mails

# Names are in the file names.txt
# Body of the mail is in body.txt

with open("names.txt", 'r', encoding='utf-8') as names_file:

    with open("body.txt", 'r', encoding='utf-8') as body_file:

        body = body_file.read()

        for name in names_file:
            mail = "Hello " + name.strip() + "\n" + body

            with open(name.strip()+".txt", 'w', encoding='utf-8') as mail_file:
                mail_file.write(mail)
                
        
