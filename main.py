def find_sieve(num):
    prime = [True for i in range(num+1)]
    current_number = 2
    while current_number * current_number <= num:
        if prime[current_number]:
            for i in range(current_number * current_number, num + 1, current_number):
                prime[i] = False
            current_number += 1
    prime[0] = False
    prime[1] = False

    for j in range(num + 1):
        if prime[j]:
            print(j, end= " ")

num= int(input("Enter a number to find all prime number less than or equal to the number: "))
find_sieve(num)