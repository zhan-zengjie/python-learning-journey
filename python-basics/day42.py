class Phone:
    IMEI=None
    producer="HM"
    def call_by_5g(self):
        print("使用5g网络进行通话")
class NFCReader:
    nfc_type="第五代"
    producer="ITCAST"
    def read_card(self):
        print("NFC读卡")
    def write_card(self):
        print("NFC写卡")
class RemoteControl:
    rc_type="红外遥控"
    def control(self):
        print("红外遥控开启了")
class MyPhone(Phone,NFCReader,RemoteControl):
    pass #用于保证类定义的完整性
phone=MyPhone()
phone.call_by_5g()
phone.read_card()
phone.write_card()
phone.control()
print(phone.producer)#对于同名成员 按从左到右继承
class Myphone_2(Phone):
    producer="ITHEIMA"                   #复写父类的成员属性
    def call_by_5g(self):                #复写父类的成员方法
        print("开启CPU单核模式")
        print("使用5g网络进行通话")
        #调用父类成员法一:
        print(f"父类的厂商是:{super().producer}")
        super().call_by_5g()
        #调用父类成员法二：
        print(f"父类的厂商是:{phone.producer}")
        Phone.call_by_5g(self)
phone_2=Myphone_2()
phone_2.call_by_5g()
print(phone_2.producer)