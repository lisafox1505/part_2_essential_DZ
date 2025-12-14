class Editor:
    def __init__(self, document):
        self.document = document

    def view_document(self):
        print(self.document)
    def edit_document(self):
        print("Редагування документів недоступне для безкоштовної версії")

class ProEditor(Editor):
    def edit_document(self):
        print("Ви змінили документ")

res = input("Введіть ключ: ")
doc = None
if res == "123654":
    doc = ProEditor("Документ_новий")
else:
    print("Ключ не вірний")
    doc = Editor("Документ")
doc.edit_document()
doc.view_document()


