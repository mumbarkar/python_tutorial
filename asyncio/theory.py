def odds(start, stop):
    for odd in range(start, stop + 1, 2):
        yield odd
        
def main():
    odds1 = list(odds(1, 10))
    print(odds1)

if __name__ == '__main__':
    main()
    