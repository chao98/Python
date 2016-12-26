def gen_coder(n, coder):
    coder = coder[1:] + coder[:1]
    return coder

def get_input():
    n = int(input())
    coder = input()

    m = int(input())
    texts = []
    for i in range(m):
        texts.append(input())

    return n, coder, texts

def cipher(text, coder, new_coder):
    my_cipher = str.maketrans(coder, new_coder)
    return text.translate(my_cipher)

def main():
    n, coder, texts = get_input()
    new_coder = gen_coder(n, coder)

    for text in texts:
        print(cipher(text, coder, new_coder))

if __name__ == '__main__':
    # http://www.spoj.com/problems/SMPCPH1
    main()
