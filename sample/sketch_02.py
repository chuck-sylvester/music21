# Code Meowstro (YouTube)
# Musical Containers: Working with Voice, Part, and Score in Music21

from music21 import stream, note

# Create a score object to hold all the musical parts and measures
score = stream.Score()

# Create a part object to represent a bass part
bass_line = stream.Part()

# Create two voice objects to represent the melody and the harmony parts
voice1 = stream.Part()
voice2 = stream.Part()

# Define a list of notenames that make up a C major scale
notes = ['C4', 'D4', 'E4', 'F4', 'G4', 'A4', 'B4', 'C5']

# Create a note object for each note and append it to voice1
for notename in notes:
    melody_note = note.Note(notename)
    voice1.append(melody_note)

    # Create a harmony note for each melody note and append it to voice2
    harmony_note = melody_note.transpose(-8)
    voice2.append(harmony_note)

    # Create a base note and append it to the base voice
    bass_note = note.Note(notename)
    bass_note.octave -= 2
    bass_line.append(bass_note)

# Insert the part objects into the score object (with 0 offset)
score.insert(0, voice1)
score.insert(0, voice2)
score.insert(0, bass_line)

score.show('midi')