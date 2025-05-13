# ---------------------------------------------------------
# - music21 User Guide - Chapter 04
# ---------------------------------------------------------

from music21 import stream, note, duration, corpus

stream1 = stream.Stream()
stream2 = stream.Stream()

note1 = note.Note('C4', type='half')
note2 = note.Note('F#4', type='quarter')
note3 = note.Note('B-2', type='half')

noteList = [note1, note2, note3]

# for thisNote in noteList:
#     print(thisNote.step, thisNote.pitch, thisNote.duration.quarterLength)

stream1.append(noteList)

# print(stream1.analyze('ambitus'))

# print('----------')

note4 = note.Note('D#3')
triplet = duration.Tuplet(3,2)
note4.duration.appendTuplet(triplet)

stream2.repeatAppend(note4, 16)

biggerStream = stream.Stream()
note4 = note.Note('D#5')
biggerStream.insert(0, note4)

biggerStream.append(stream1)

# -------------------------------------
# Working with Streams

note1 = note.Note('C4')
note1.duration.type = 'half'
note2 = note.Note('F#4')
note3 = note.Note('B-2')
note3.duration.type = 'whole'

stream1 = stream.Stream()
stream1.id = 'some notes'
stream1.append(note1)
stream1.append(note2)
stream1.append(note3)

biggerStream = stream.Stream()
note2 = note.Note('D#5')
biggerStream.insert(0, note2)
biggerStream.append(stream1)

# biggerStream.show('text')

sBach = corpus.parse('joplin/maple_leaf_rag')

print(sBach)
print(len(sBach))

for item in sBach:
    print(item)

sBach.show()




