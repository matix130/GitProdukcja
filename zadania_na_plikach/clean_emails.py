import sys
if len(sys.argv) !=3:
    print("Podałeś złą liczbę argumentów")
    exit()
_, file_in, file_out = sys.argv
print(file_in)


with open("dane/emails.txt") as f:
    unigue_emails = set()
    for linia in f:
         a = linia.strip().lower()
         if a.count('@') == 1:
            unigue_emails.add(a)

emails=sorted(unigue_emails)


with open(file_out, "w") as f:
    for email in emails:
        f.write(email+"\n")