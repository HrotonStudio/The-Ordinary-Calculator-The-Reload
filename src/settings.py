from src.lib_usual import read_settings

settings = read_settings("text\\settings.ini")

Background = settings["Background"]
Debug = settings["Debug"] == "True"
MusicIsPlaying = settings["MusicIsPlaying"] == "True"
MusicContinuePlaying = settings["MusicContinuePlaying"]