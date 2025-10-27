class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        beams = 0
        receiver = 0

        for row in bank:
            transmitter = row.count('1')
            if transmitter:
                beams += transmitter * receiver
                receiver = transmitter

        return beams
