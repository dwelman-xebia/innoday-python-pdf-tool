def merge(writer, to_merge, position):
    if position > -1:
        writer.merge(fileobj=to_merge, position=position)
    else:
        writer.append(to_merge)
    return writer