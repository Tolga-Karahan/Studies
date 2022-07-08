from passlib.context import CryptContext

password_context = CryptContext(schemas=['bcrypt'], depreceated='auto')

def encrypt_password(password: str):
    return password_context.hash(password)
