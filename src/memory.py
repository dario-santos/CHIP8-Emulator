import os

fontset = [
  0xF0, 0x90, 0x90, 0x90, 0xF0, # 0
  0x20, 0x60, 0x20, 0x20, 0x70, # 1
  0xF0, 0x10, 0xF0, 0x80, 0xF0, # 2
  0xF0, 0x10, 0xF0, 0x10, 0xF0, # 3
  0x90, 0x90, 0xF0, 0x10, 0x10, # 4
  0xF0, 0x80, 0xF0, 0x10, 0xF0, # 5
  0xF0, 0x80, 0xF0, 0x90, 0xF0, # 6
  0xF0, 0x10, 0x20, 0x40, 0x40, # 7
  0xF0, 0x90, 0xF0, 0x90, 0xF0, # 8
  0xF0, 0x90, 0xF0, 0x10, 0xF0, # 9
  0xF0, 0x90, 0xF0, 0x90, 0x90, # A
  0xE0, 0x90, 0xE0, 0x90, 0xE0, # B
  0xF0, 0x80, 0x80, 0x80, 0xF0, # C
  0xE0, 0x90, 0x90, 0x90, 0xE0, # D
  0xF0, 0x80, 0xF0, 0x80, 0xF0, # E
  0xF0, 0x80, 0xF0, 0x80, 0x80  # F
]

# Memory ram - 4KB
memory = [0] * 4096

# Registers: One of the 16 available variables
vn = [0] * 16

# The Stack - Used for returns, normally has 48 bytes and 12 levels
stack = []

# Timers 
timer_delay = 0
timer_sound = 0

def initialize():
  global memory, fontset
  # Load fontset
  for i in range(80):
    memory[i] = fontset[i]

def load_file(rom):
  global memory
  
  initialize()
  
  # Load the ROM into RAM.
  with open(rom, 'rb') as rom:
    rom_length = os.fstat(rom.fileno()).st_size

    if rom_length > 0xFFF - 0x200 + 1: 
      raise "The given file is too big to be a CHIP-8 ROM."
  
    for i in range(0, rom_length):
      memory[0x200 + i] = int.from_bytes(rom.read(1), "big")


import time
def print_debug(opcode):
  global memory, vn, stack, timer_delay, timer_sound, pc, I
  print('opcode:    ', hex(opcode))
  print('pc:    ', pc)
  print('I:    ', I)
  print('timer_delay:    ', timer_delay)
  print('timer_sound:    ', timer_sound)
  print('vn:    ', vn)
  #print('memory:    ', memory)

  time.sleep(0)