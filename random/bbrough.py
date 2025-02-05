class Sequencer:
    def __init__(self):
        self.expected_seq = 0  # The next sequence number we expect
        self.buffer = {}  # Dictionary to store out-of-order packets

    def handle(self, data: str, seq_num: int):
        if seq_num == self.expected_seq:
            # Print the in-order packet immediately
            print(data)
            self.expected_seq += 1
            
            # Check the buffer for the next expected packets
            while self.expected_seq in self.buffer:
                print(self.buffer.pop(self.expected_seq))
                self.expected_seq += 1
        elif seq_num > self.expected_seq:
            # Buffer out-of-order packets
            self.buffer[seq_num] = data


sequencer = Sequencer()

stream = [(1, 'aaa'), (2, 'bbb'), (4, 'ddd'), (3, 'ccc'), (6, 'fff'), (5, 'eee')]

for seq_num, data in stream:
    sequencer.handle(data, seq_num)