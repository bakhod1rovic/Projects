import csv

class PhoneContact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def __str__(self):
        return f"Ismi: {self.name}\tTelefoni: {self.phone}"

class Phone:
    def __init__(self):
        self.contacts = []

    def load_contacts_from_csv(self):
        with open("contacts.csv", newline="") as csvfile:
            reader = csv.DictReader(csvfile, fieldnames=["ismi", "telefoni"])
            for row in reader:
                contact = PhoneContact(row['ismi'], row['telefoni'])
                self.contacts.append(contact)
    def save(self):
        with open('contacts2.csv', 'w', newline='') as csvfile:
            fieldnames = ['Name', 'Phone']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            for contact in self.contacts:
                writer.writerow({'Name': contact.name, 'Phone': contact.phone})

    def search_contacts(self, name):
        for contact in self.contacts:
            if contact.name == name:
                return contact.phone


phone = Phone()
# phone.load_contacts_from_csv()  # Fayldan kontaktlarni yuklaymiz
# print(phone.search_contacts("wife"))  # Qidiruv natijasini chop etamiz
print(phone.save)
# class talaba:
#     def __init__(self, fan, ismi, bali, bahosi):
#         self.fan = fan
#         self.ismi = ismi
#         self.bali = bali
#         self.bahosi = bahosi
#
# class imtihon:
#     def __init__(self):
#         natijalar = []
#
#     def natija(self):
#         with open('exam_results.csv', newline="") as csvfile:
#             reader = csv.reader(csvfile)
#             for row in reader:
#                 student_exam = talaba(row[0], row[1], row[2], row[3])
#                 self.natijalar.append(student_exam)
#
#     def passed_exam_number(selfself, ismi):
#         otganlar = []
#         pass
