import json


class AddressBook:
    def __init__(self):
        self.contacts = {}

    def add(self, name, phone):
        if name in self.contacts:
            return False
        self.contacts[name] = phone
        return True

    def find(self, name):
        if name in self.contacts:
            return self.contacts[name]

    def delete(self, name):
        if name in self.contacts:
            del self.contacts[name]
            return True
        return False

    def show_all(self):
        for key, value in sorted(self.contacts.items()):
            print(key, value)

    def save(self, path="contacts.json"):
        with open(path, "w", encoding="utf-8") as f:
            json.dump(self.contacts, f, ensure_ascii=False, indent=2)

    def load(self, path="contacts.json"):
        try:
            with open(path, "r", encoding="utf-8") as f:
                self.contacts =json.load(f)
        except FileNotFoundError:
            self.contacts = {}
              


book = AddressBook()

print(book.add("王五", "13600000000"))
print(book.add("张三", "13800000000"))
print(book.add("李四", "13900000000"))
print(book.add("张三", "13700000000"))
print(book.find("张三"))
print(book.find("赵六"))
print(book.delete("赵六"))
book.show_all()
book.save()
book2 = AddressBook()
book2.load()
print(book2.contacts)