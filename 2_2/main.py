import re
file_name = "2_2/input.txt"

valid = lambda first,second,char,passwd : (passwd[int(first)-1] == char) ^ (passwd[int(second)-1] == char)

def main():
    passwords = [re.split('-| |: ',line.strip('\n')) for line in open(file_name,'r')]
    valid_counter = 0
    for password in passwords:
        if valid(*password):
            valid_counter += 1
    return valid_counter
        
        
        
if __name__ == "__main__":
    print(main())