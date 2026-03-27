import bcrypt


# Kelas induk
class Enkripsi:
    def __init__(self, nama):
        self.nama_algoritma = nama

    def hash(self, password):
        pass

# Kelas Turunan Enkripsi BCrypt
class EnkripsiBCrypt(Enkripsi):
    def __init__(self):
        super().__init__("BCrypt")

    def hash(self, password):
        print("Run enkripsi BCrypt...........")
        password_bytes = password.encode('utf-8')
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(password_bytes, salt)
        return hashed.decode('utf-8')


# Kelas Turunan Enkripsi Argon2
class EnkripsiArgon2(Enkripsi):
    def __init__(self):
        super().__init__("Argon2")

    def hash(self, password):
        print("Run enkripsi Argon2...........")
        return "45ed5sd5sd5s654s"



class User:
    def __init__(self, username: str, password: str, enkripsi: Enkripsi):
        self.__username = username
        self.__password = enkripsi.hash(password)

    def get_password(self):
        return self.__password
    

enkripsi1 = EnkripsiBCrypt()
enkripsi2 = EnkripsiArgon2()
user_x = User("budi08","qwerty123456",enkripsi1)
user1 = User("affa01","qwerty123456",enkripsi2)

print(user1.get_password())