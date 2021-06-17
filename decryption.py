from PIL import Image
import sys
import argparse
def get_options():
    parser = argparse.ArgumentParser(description='Visual cipher image generator.')
    parser.add_argument('--key', '-k',  required = True, metavar = "ROTATIONAL_KEY", help='encryption key')
    parser.add_argument('--secret',  '-s', required = True, metavar = "SECRET_IMAGE_FILE_PATH",    default = "secret.png",   help='secret image (will be created if it does not exist)')
    parser.add_argument('--ciphered', '-c', required = True, metavar = "CIPHERED_IMAGE_FILE_PATH", default = "ciphered.png", help='ciphered image (to be generated)')
    args = parser.parse_args()    
    return args

def recover(r):
    r = r % 4
    r = 4 - r
    r = (r%4)*90
    return r

def nxor(i,j):
    return not(i^j)

args = get_options()    
infile1 = Image.open(args.ciphered)
infile2 = Image.open(args.secret)
key = args.key
r1 = int(key[0])
r2 = int(key[1])
inf1 = infile1.rotate(recover(r2))
inf2 = infile2.rotate(recover(r1))

outfile = Image.new('1', inf1.size)
for x in range(inf1.size[0]):
    for y in range(inf1.size[1]):
        outfile.putpixel((x, y), nxor(inf1.getpixel((x, y)), inf2.getpixel((x, y))))

outfile.show()