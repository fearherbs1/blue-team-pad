import supervisor
import board

supervisor.next_stack_limit:8192
print("Booting...")
print("Board Details:")
print(dir(board))
