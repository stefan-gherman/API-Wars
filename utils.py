from werkzeug.security import generate_password_hash, check_password_hash



def hash_password(string):
    return generate_password_hash(string);


def check_hashed_password(hash, string):
    return check_password_hash(hash,string)


