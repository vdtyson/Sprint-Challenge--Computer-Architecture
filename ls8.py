from cpu import CPU

if __name__ == '__main__':
    ls8 = CPU()
    ls8.load('sctest.ls8')
    ls8.run()
