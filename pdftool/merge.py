def merge(writer, to_merge, position, pages):
    if position > -1:
        if len(pages) > 0:
            writer.merge(fileobj=to_merge, position=position, pages=pages)
        else:
            writer.merge(fileobj=to_merge, position=position)
    else:
        if len(pages) > 0:
            writer.append(fileobj=to_merge, pages=pages)
        else: 
            writer.append(to_merge)
    return writer