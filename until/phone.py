from faker import Faker

fake = Faker("zh_CN")
class TestFaker:
        # 选择中文


    def get_name(self):
        print(fake.name())
        return fake.name()

    def get_phone_number(self):
        print(fake.phone_number())
        return fake.phone_number()


if __name__ == "__main__":
    test = TestFaker()
    test.get_name()
    test.get_phone_number()

