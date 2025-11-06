import time
import sys
import csv

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def type_print(text, delay=0.05):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def progress_bar(iteration, total, length=30):
    percent = iteration / total
    filled_length = int(length * percent)
    bar = '█' * filled_length + '-' * (length - filled_length)
    print(f'\rCalculating primes: |{bar}| {int(percent*100)}%', end='\r')
    if iteration == total:
        print()

def save_to_csv(primes, filename="primes.csv"):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Prime Numbers"])
        for prime in primes:
            writer.writerow([prime])

def main():
    type_print("=== Prime Number Generator ===")
    
    while True:
        try:
            count = int(input("Enter the number of prime numbers you want: "))
            if count <= 0:
                type_print("Please enter a positive number.")
                continue
            break
        except ValueError:
            type_print("Invalid input! Please enter an integer.")

    while True:
        speed = input("Choose typing speed (fast/slow): ").strip().lower()
        if speed == "fast":
            delay = 0.01
            break
        elif speed == "slow":
            delay = 0.05
            break
        else:
            type_print("Please type 'fast' or 'slow'.")

    primes = []
    num = 2
    while len(primes) < count:
        if is_prime(num):
            primes.append(num)
        num += 1
        progress_bar(len(primes), count)
        time.sleep(0.01)

    type_print(f"\nThe first {count} prime numbers are:")

    for i, prime in enumerate(primes, start=1):
        type_print(f"{prime}\t", delay=delay)
        if i % 5 == 0:
            print()

    save_to_csv(primes)
    type_print("\nPrime numbers have been saved to 'primes.csv'.")

if __name__ == "__main__":
    main()