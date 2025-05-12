# --------------------------------------------------------
# Sample composition, created with the help of ChatGPT
# -------------------------------------------------------

from music21 import stream, note, chord, meter, instrument

# Create a Score (Entire Composition)
my_score = stream.Score()

# ---------------------------
# Create the Piano Part
piano_part = stream.Part()
piano_part.id = 'Piano'
piano_part.insert(0, instrument.Piano()) # Assign piano instrument

# Create Measure 1 for Piano
piano_measure1 = stream.Measure(number=1)
piano_measure1.append(meter.TimeSignature('4/4'))

# Create Right Hand (RH) voice for measure 1
piano_voice1_m1 = stream.Voice()
piano_voice1_m1.id = 'RH'

# Add Notes and a Chord to RH
piano_voice1_m1.append(note.Note('C5', type='quarter'))
piano_voice1_m1.append(chord.Chord(['E5', 'G5', 'B5'], type='quarter'))
piano_voice1_m1.append(note.Note('G5', type='quarter'))
piano_voice1_m1.append(chord.Chord(['C5', 'E5', 'G5'], type='quarter'))

# Create Left Hand (LH) voice for measure 1
piano_voice2_m1 = stream.Voice()
piano_voice2_m1.id = 'LH'
piano_voice2_m1.append(note.Note('C3', type='half'))
piano_voice2_m1.append(note.Note('G2', type='half'))

# Add Voices to Measure
piano_measure1.append(piano_voice1_m1)
piano_measure1.append(piano_voice2_m1)

# Create Measure 2 for Piano
piano_measure2 = stream.Measure(number=2)

# Right Hand Voice for Measure 2
piano_voice1_m2 = stream.Voice()
piano_voice1_m2.id = 'RH'

# Add Notes and a Chord to RH
piano_voice1_m2.append(note.Note('F5', type='quarter'))
piano_voice1_m2.append(chord.Chord(['A5', 'C6'], type='quarter'))
piano_voice1_m2.append(note.Note('D5', type='quarter'))
piano_voice1_m2.append(chord.Chord(['F5', 'A5', 'C6'], type='quarter'))

# Left Hand Voice for Measure 2
piano_voice2_m2 = stream.Voice()
piano_voice2_m2.id = 'LH'
piano_voice2_m2.append(note.Note('F3', type='half'))
piano_voice2_m2.append(note.Note('C3', type='half'))

# Add Voices to Measure 2
piano_measure2.append(piano_voice1_m2)
piano_measure2.append(piano_voice2_m2)

# Add Measures to Piano Part
piano_part.append(piano_measure1)
piano_part.append(piano_measure2)

# ---------------------------
# Create the Violin Part
violin_part = stream.Part()
violin_part.id = 'Violin'
violin_part.insert(0, instrument.Violin()) # Assign violin instrument

# Create Measure 1 for Violin
violin_measure1 = stream.Measure(number=1)
violin_measure1.append(meter.TimeSignature('4/4'))

# Add Notes directly to Violin Measure (Simple Melody)
violin_measure1.append(note.Note('A4', type='quarter'))
violin_measure1.append(note.Note('B4', type='quarter'))
violin_measure1.append(note.Note('C5', type='quarter'))
violin_measure1.append(note.Rest(type='quarter'))

# Create Measure 2 for Violin
violin_measure2 = stream.Measure(number=2)

violin_measure2.append(note.Note('D5', type='quarter'))
violin_measure2.append(note.Note('E5', type='quarter'))
violin_measure2.append(note.Note('F5', type='quarter'))
violin_measure2.append(note.Rest(type='quarter'))

# Add Measures to Violin Part
violin_part.append(violin_measure1)
violin_part.append(violin_measure2)

# ---------------------------
# Add Both Parts to the Score
my_score.append(piano_part)
my_score.append(violin_part)

# ---------------------------
# Show the structure in text format
# my_score.show('text')

# ---------------------------
# Open composition in MuseScore
my_score.show()
