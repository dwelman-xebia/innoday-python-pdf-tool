def encrypt(writer, password):
    writer.encrypt(password)
    return writer

def decrypt(reader, password):
    reader.decrypt(password)
    return reader