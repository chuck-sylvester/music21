# Sample composition that has two parts

from music21 import stream, note, meter

# Create a Score (Entire Composition)
my_score = stream.Score()

# ---------------------------
# Create the Piano Part
piano_part = stream.Part()
piano_part.id = 'Piano'

# Create Measure 1 for Piano
piano_measure1 = stream.Measure(number=1)
piano_measure1.append(meter.TimeSignature('4/4'))

# Create Voice 1 (Right Hand)
piano_voice1 = stream.Voice()
piano_voice1.id = 'RH'
piano_voice1.append(note.Note('C5', type='quarter'))
piano_voice1.append(note.Note('E5', type='quarter'))
piano_voice1.append(note.Note('G5', type='quarter'))
piano_voice1.append(note.Rest(type='quarter'))

# Create Voice 2 (Left Hand)
piano_voice2 = stream.Voice()
piano_voice2.id = 'LH'
piano_voice2.append(note.Note('C3', type='half'))
piano_voice2.append(note.Note('G2', type='half'))

# Add Voices to Measure
piano_measure1.append(piano_voice1)
piano_measure1.append(piano_voice2)

# Add Measure to Piano Part
piano_part.append(piano_measure1)

# ---------------------------
# Create the Violin Part
violin_part = stream.Part()
violin_part.id = 'Violin'

# Create Measure 1 for Violin
violin_measure1 = stream.Measure(number=1)
violin_measure1.append(meter.TimeSignature('4/4'))

# Add Notes directly to Violin Measure (Single Line, No Voices)
violin_measure1.append(note.Note('A4', type='quarter'))
violin_measure1.append(note.Note('B4', type='quarter'))
violin_measure1.append(note.Note('C5', type='quarter'))
violin_measure1.append(note.Rest(type='quarter'))

# Add Measure to Violin Part
violin_part.append(violin_measure1)

# ---------------------------
# Add Both Parts to the Score
my_score.append(piano_part)
my_score.append(violin_part)

# ---------------------------
# Show the structure in text format
# my_score.show('text')

# ---------------------------
# Show composition in MuseScore
# my_score.show()

# ---------------------------
# Open composition in GarageBand
my_score.show('midi')
