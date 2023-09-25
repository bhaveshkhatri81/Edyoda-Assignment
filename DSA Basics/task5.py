# 5. Read about the Tower of Hanoi algorithm. Write a program to implement it.

def tower_of_hanoi(n, source, target, auxiliary):
    if n > 0:
        tower_of_hanoi(n-1, source, auxiliary, target)
        
        print(f"Move disk {n} from {source} to {target}")
        
        tower_of_hanoi(n-1, auxiliary, target, source)


num_disks = 3
source_peg = "A"
target_peg = "C"
auxiliary_peg = "B"

tower_of_hanoi(num_disks, source_peg, target_peg, auxiliary_peg)
