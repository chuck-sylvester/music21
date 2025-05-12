# My first simple script using the music21 library

# For this simple script to verify installation, I will go ahead and import
# the entire music21 library into the global namespace. For subsequent programs,
# I will follow best practices for only importing the modules and classes needed.

from music21 import corpus
from music21 import note, pitch, stream, chord

# Initial test
# s = corpus.parse('bach/bwv65.2.xml')
# s = corpus.parse('weber/concertino_clarinet.xml')
# score_key = s.analyze('key')
# print(score_key)
# s.show('midi')
# s.show()

# Moving on to other basics
# f = note.Note('F5')
# print(f)
# print(f.name)
# print(f.pitch.frequency)
# print(f.pitch, f.quarterLength, f.octave)
# f.show('midi')

# bflat = note.Note('B-2')
# d = bflat.transpose('M3')
# p1 = pitch.Pitch('b-4')

note1 = note.Note('C4')
note2 = note.Note('D4')
note3 = note.Note('E4')
note4 = note.Note('F4')
note5 = note.Note('G4')
note6 = note.Note('A4')
note7 = note.Note('B4')
note8 = note.Note('C5')
chord1 = chord.Chord(['C4', 'E4', 'G4'])

note1.duration.type = 'half'
note4.duration.type = 'eighth'
note5.duration.type = 'eighth'
note6.duration.type = 'eighth'
note7.duration.type = 'eighth'
note8.duration.type = 'whole'
chord1.duration.type = 'whole'

print(note1.duration.quarterLength, note2.duration.quarterLength)
print(note1.step, note2.step)

stream1 = stream.Stream()
stream1.append(note1)
stream1.append(note2)
stream1.append(note3)
stream1.append(note4)
stream1.append(note5)
stream1.append(note6)
stream1.append(note7)
stream1.append(note8)
stream1.append(chord1)

stream1.show('midi')
