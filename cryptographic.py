import hashlib

h = 'd077f244def8a70e5ea758bd8352fcd8'
for letter in 'abcdefghijklmnopqrstuvwxyz':
    best_guess = 'ca' + letter
    b = hashlib.new('md5', best_guess.encode('UTF8')).hexdigest()
    print(best_guess, b)
    if h == b:
        print(f'The three letter word is {best_guess}')
        exit()
        
