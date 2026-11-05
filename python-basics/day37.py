class Clock:
    id=None
    price=None
    def ring(self):
        import winsound
        winsound.Beep(2000,3000)
class1=Clock()
class1.id="003032"
class1.price=19.99
print(f"闹钟id为:{class1.id},价格为:{class1.price}")
class1.ring()
class2=Clock()
class2.id="003033"
class2.price=29.99
print(f"闹钟id为:{class2.id},价格为:{class2.price}")
class2.ring()