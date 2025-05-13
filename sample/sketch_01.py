# Code Meowstro (Youtube)
# Introduction to Music21 for Python

from music21 import note, pitch, stream, meter

# Creating a simple note object
n = note.Note('C4')

print()
print('            Note Name: ', n.name)
print('          Note Octave: ', n.octave)
print(' Note Pitch Frequency: ', n.pitch.frequency)
print()

# n.show()

# Stream - a key container class within music21
s = stream.Stream()
s.append(meter.TimeSignature('3/4'))
s.append(note.Note('C4'))
s.append(note.Note('D4'))
s.append(note.Note('E4'))
s.show()