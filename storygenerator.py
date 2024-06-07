import random

# Lists of story elements
characters = ["a brave knight", "a cunning thief", "a wise wizard", "a humble farmer", "a curious child"]
settings = ["in a dark forest", "in a bustling city", "in a quiet village", "on a distant planet", "in an ancient castle"]
conflicts = ["facing a fearsome dragon", "searching for a lost treasure", "defending their home", "solving a mysterious crime", "embarking on a dangerous quest"]
resolutions = ["and found unexpected allies.", "and discovered a hidden truth.", "and saved the day.", "and learned a valuable lesson.", "and restored peace."]

def generate_story():
    character = random.choice(characters)
    setting = random.choice(settings)
    conflict = random.choice(conflicts)
    resolution = random.choice(resolutions)
    
    story = f"Once upon a time, {character} was {setting}. They were {conflict} {resolution}"
    return story

# Generate and print a random story
print(generate_story())
