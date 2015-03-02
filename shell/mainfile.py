__author__ = 'rainbowbreeze'

def dostuff():
    with open('mainfile.py', 'r') as f:
        read_line = f.read()
        print(read_line)
    f.closed

if __name__ == "__main__":
    print "ciao"
    dostuff()