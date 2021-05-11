#!/usr/bin/python3
import hidden_4
if __name__ == '__main__':
    attrib = dir(hidden_4)
    for text in attrib:
        if text[0] == '_':
            continue
        print(text)

