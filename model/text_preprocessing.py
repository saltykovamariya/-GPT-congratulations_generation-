def processing(input_string: str) -> str:
    output_string = ' '.join([i.strip() for i in input_string.split()])
    output_string = output_string.replace('»', '', 1).replace('"', '', 1)
    while not (output_string.endswith('.') or output_string.endswith('!') or output_string.endswith('?')):
        output_string = output_string[:-1]
    return output_string