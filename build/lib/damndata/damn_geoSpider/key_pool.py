import os
def key_pool():
    files= os.listdir(os.getcwd()) 
    s = []
    for file in files: 
        if file.endswith('.damnkey'):
            with open(file) as f:
                iter_f = iter(f) 
                for line in iter_f: 
                    s.append(line.strip('\n')) 
    return s

# print(os.getcwd())
if __name__ == '__main__':
    keys = key_pool()
    print(key_pool)