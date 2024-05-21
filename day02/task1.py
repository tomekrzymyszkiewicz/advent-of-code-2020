import re
file_name = "input.txt"

valid = lambda min,max,char,passwd : int(min) <= passwd.count(char) and passwd.count(char) <= int(max)

def main():
    with open(file_name,'r') as input:
        passwords = [re.split('-| |: ',line.strip('\n')) for line in input]
    valid_counter = 0
    for password in passwords:
        if valid(*password):
            valid_counter += 1
    return valid_counter
        
        
        
if __name__ == "__main__":
    print(main())