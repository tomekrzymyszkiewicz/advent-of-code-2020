file_name = "input.txt"


def main():
    with open(file_name,'r') as input:
        numbers = [int(line.strip('\n')) for line in input]
    for i in numbers:
        for j in numbers:
            if j+i == 2020:
                return i*j

if __name__ == "__main__":
    print(main())