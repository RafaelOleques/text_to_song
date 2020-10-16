from midiutil.MidiFile import MIDIFile

# create your MIDI object
mf = MIDIFile(2)     # only 1 track
track = 0   # the only track

time = 0    # start at the beginning
mf.addTrackName(track, time, "Sample Track")
mf.addTempo(track, time, 120)

# add some notes
channel = 0
volume = 100

pitch = 60           # C4 (middle C)
time = 0             # start on beat 0
duration = 1         # 1 beat long
mf.addNote(track, channel, pitch, time, duration, volume)

pitch = 64           # E4
time = 2             # start on beat 2
duration = 1         # 1 beat long
mf.addNote(track, channel, pitch, time, duration, volume)

pitch = 67           # G4
time = 4             # start on beat 4
duration = 1         # 1 beat long
mf.addNote(track, channel, pitch, time, duration, volume)

track   = 0
time    = 3 # Eight beats into the composition
program = 21 # A Cello

mf.addProgramChange(track, channel, time, program)

################
track = 1   # the only track

time = 5    # start at the beginning
tempo    = 60  # In BPM
mf.addTrackName(track, time, "Track")
mf.addTempo(track, time, tempo)

# add some notes
channel = 0
volume = 100

pitch = 60           # C4 (middle C)
time = 5             # start on beat 0
duration = 1         # 1 beat long
mf.addNote(track, channel, pitch, time, duration, volume)

pitch = 64           # E4
time = 6             # start on beat 2
duration = 1         # 1 beat long
mf.addNote(track, channel, pitch, time, duration, volume)

pitch = 67           # G4
time = 7             # start on beat 4
duration = 1         # 1 beat long
mf.addNote(track, channel, pitch, time, duration, volume)

track   = 1
time    = 5 # Eight beats into the composition
program = 59 # A Cello

mf.addProgramChange(track, channel, time, program)

# write it to disk
with open("output.mid", 'wb') as outf:
    mf.writeFile(outf)