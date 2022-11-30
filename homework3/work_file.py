'''
from pathlib import Path
'''

'''
import pathlib

wave = pathlib.Path("ocean", "wave.txt")
print(wave)
'''

'''
wave = Path("ocean", "wave.txt")
print(wave)
'''

'''
home_directory = Path.home()
wave_absolute = Path(home_directory, "ocean", "wave.txt")
print(home_directory)
print(wave_absolute)
'''

'''
shark = Path(Path.home(), "ocean", "animals", Path("fish", "shark.txt"))
print(shark)
'''

'''
wave = Path("ocean", "wave.txt")
print(wave)
print(wave.name)
print(wave.suffix)
'''

'''
wave = Path("ocean", "wave.txt")
tides = wave.with_name("tides.md")
print(wave)
print(tides)
'''

'''
shark = Path("ocean", "animals", "fish", "shark.txt")
print(shark)
print(shark.parent)
print(shark.parent.parent)
print(shark.parent.parent.parent)
'''

'''
for txt_path in Path("ocean").glob("*.txt"):
    print(txt_path)
'''

'''
for txt_path in Path("ocean").glob("**/*.txt"):
    print(txt_path)
'''

'''
shark = Path("ocean", "animals", "fish", "shark.txt")
below_ocean = shark.relative_to(Path("ocean"))
below_animals = shark.relative_to(Path("ocean", "animals"))
print(shark)
print(below_ocean)
print(below_animals)
'''

'''
#shark = Path(Path.home(),"ocean", "animals", "fish", "shark.txt")
shark = Path("ocean", "animals", "fish", "shark.txt")
below_ocean = shark.relative_to(Path("ocean"))
below_animals = shark.relative_to(Path("ocean", "animals"))
print(shark)
print(below_ocean)
print(below_animals)
'''

'''
shark = Path("ocean", "animals", "fish", "shark.txt")
shark.relative_to(Path("unrelated", "path"))
'''

from pathlib import Path

#file_name = "create_file_with_pathlib.txt"
file_name = "create_file_with_pathlib.md"
home_directory = Path.home()
absolut_file_directory = Path(home_directory, "Desktop", "getting to know Python", "homework3", file_name)
print(home_directory)
print(absolut_file_directory)

with open(absolut_file_directory, 'a') as data:
    data.write(str("Chek one, two !\n"))