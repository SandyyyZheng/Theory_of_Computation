# Binary to Unary Conversion
# Tape 1: Binary Input
# Tape 2: Unary Output

states: [start, find_end, sub_one, rewind, halt, reject]
input_alphabet: ['$', '0', '1']
tape_alphabet_extra: ['X'] 
start_state: start
accept_state: halt
reject_state: reject

delta:
  start:
    # Start by writing an X on tape 2, which prevents crashing when rewinding later.
    '$_': [find_end, '$X', RR]

  find_end:
    # scroll right until hitting the blank at the end
    '0_': [find_end, '0_', RS]
    '1_': [find_end, '1_', RS]
    # Found the blank, step back left to the last digit
    '__': [sub_one, '__', LS]

  sub_one:
    # Logic: repeatedly subtract 1 from binary, add 1 to unary
    # Case 1: Found a 1. Flip to 0, add a 1 to output, go back to right side
    '1_': [find_end, '01', SR]

    # Case 2: Found a 0. Flip to 1, move left to borrow
    '0_': [sub_one, '1_', LS]

    # Case 3: Hit the $. 
    # Switch to rewind mode to fix the output tape position.
    '$_': [rewind, '$_', SL]

  rewind:
    # Tape 1 stays put. Tape 2 goes left to find the start.
    # Not yet back to the X
    '$1': [rewind, '$1', SL]
    
    # Hit the X anchor
    # Delete the X, step right once to sit on the first 1, finish.
    '$X': [halt, '$_', SR]