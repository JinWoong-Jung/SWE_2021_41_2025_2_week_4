def isHappy(n):
  seen_numbers = set()

  while n != 1 and n not in seen_numbers:
    seen_numbers.add(n)

    next_number = 0
    while n > 0:
      digit = n % 10
      next_number += digit * digit
      n //= 10

    n = next_number

  return n == 1

if __name__ == "__main__":
  sample0_output = isHappy(19)
  sample1_output = isHappy(2)
  
  with open("/app/bind_mount/output.txt", "w") as f:
    f.write(f"19: {sample0_output}\n")
    f.write(f"2: {sample1_output}\n")
    
  print("Results saved to /app/bind_mount/output.txt")