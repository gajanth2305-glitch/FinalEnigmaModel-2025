# File: EnigmaModel.py

""" This is the starter file for the Enigma project. """


from EnigmaView import EnigmaView

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ROTOR_PERMUTATION_SLOW = "EKMFLGDQVZNTOWYHXUSPAIBRCJ"
ROTOR_PERMUTATION_MEDIUM = "AJDKSIRUXBLHWTMCQGZNPYFVOE"
ROTOR_PERMUTATION_FAST = "BDFHJLCPRTXVZNYEIWGAKMUSQO"
REFLECTOR_PERMUTATION = "IXUHFEZDAOMTKQJWNSRLCYPBVG"

class EnigmaModel:


    def __init__(self):
        """Creates a new EnigmaModel with no views."""
        self._views = [ ]
        self._key_is_down = {}
        self._lamp_light = {}
        self._rotors = [("A"),("A"),("A")]
        for letter in ALPHABET:
            self._key_is_down[letter] = False
            self._lamp_light[letter] = False
            

    def add_view(self, view):
        """Adds a view to this model."""
        self._views.append(view)

    def update(self):
        """Sends an update request to all the views."""
        for view in self._views:
            view.update()

    def is_key_down(self, letter):
        return self._key_is_down[letter]        # In the stub version, keys are never down

    def is_lamp_on(self, letter):
        return self._lamp_light[letter]   # In the stub version, lamps are always off

    def key_pressed(self, letter):
        self._key_is_down[letter] = True

#Code thats used to reach milestone 6
        current=self._rotors[2] 
        pos=(ord(current)-ord('A'))
        pos=(pos+1)%26
        self._rotors[2]=chr(pos+ord('A'))
        if pos==0:
            current=self._rotors[1]
            pos=(ord(current)-ord('A'))
            pos=(pos+1)%26
            self._rotors[1]=chr(pos+ord('A'))
            if pos==0:
                current=self._rotors[0]
                pos=(ord(current)-ord('A'))
                pos=(pos+1)%26
                self._rotors[0]=chr(pos+ord('A'))
#The code thats used to reach milestone 5    

        fast_pos = self._rotors[2] # Variable stores position of fast rotor
        fast_offset = (ord(fast_pos) - ord('A')) # Calculates the offset of the fast rotor
        pos = ord(letter) - ord('A') # The "ord" function converts a character into a integer,
        # which represents unicode of said character. This code converts input letter to position 0-25
        pos = (pos + fast_offset) % 26 # Modulo 26 prevents going above the 26 letters in the alphabet
        c_fast = ROTOR_PERMUTATION_FAST[pos] # Stores new letter after the fast rotor has moved forward
        med_pos = self._rotors[1] # Variable stores position of medium rotor
        med_offset = (ord(med_pos) - ord('A')) # Calculates the offset of the medium rotor
        pos = (ord(c_fast) - ord('A') + med_offset) % 26 
        c_med = ROTOR_PERMUTATION_MEDIUM[pos] # Stores new letter after the medium rotor has moved forward
        slow_pos = self._rotors[0] # Variable stores position of fast rotor
        slow_offset = (ord(slow_pos) - ord('A')) # Same steps as before
        pos = (ord(c_med) - ord('A') + slow_offset) % 26 
        c_slow = ROTOR_PERMUTATION_SLOW[pos] 
        pos = (ord(c_slow) - ord('A') - slow_offset) % 26 # Backwards through slow rotor
        c_slow_forward=ROTOR_PERMUTATION_SLOW[pos] # Letter after slow rotor moves  forward
        pos=ord(c_slow_forward)-ord('A') # Finds the index of letter in SLOW_ROTOR
        c_reflected=REFLECTOR_PERMUTATION[pos] # Reflector step
        pos=ROTOR_PERMUTATION_SLOW.index(c_reflected) # Finds the index of letter in SLOW_ROTOR
        pos=(pos - slow_offset) % 26 # Final position after reflector steps
        c_slow_backward=chr(pos + ord('A')) # Final letter after slow rotor backward
        # "chr" function converts a unicode (int) back into a character
        pos=ROTOR_PERMUTATION_MEDIUM.index(c_slow_backward) # Finds the index of letter in MEDIUM_ROTOR
        pos=(pos - med_offset) % 26 # Final position after slow rotor backward
        c_med_backward=chr(pos + ord('A'))# Final letter after medium rotor backward
        pos=ROTOR_PERMUTATION_FAST.index(c_med_backward)# Finds the index of letter in FAST_ROTOR
        pos=(pos - fast_offset) % 26 # Final position after all rotors
        encoded= chr(pos + ord('A')) # THE final encoded letter
        self._lamp_light[encoded] = True # Turns on the lamp for the letter which was encoded
        self.update()

    def key_released(self, letter):
        self._key_is_down[letter] = False
        for ch in ALPHABET:
            self._lamp_light[ch] = False
        self.update()

    def get_rotor_letter(self, index):
        return self._rotors[index]          # In the stub version, all rotors are set to "A"

    def rotor_clicked(self, index):
        current_letter = self._rotors[index] # Variable stores current letter
        pos = (ord(current_letter) - ord('A')) # Converts letter to position 0-25 
        # The "ord" function converts a character into a integer, which represents unicode of said character.
        pos = (pos + 1) % 26 # Advance position by 1, modulo prevents position going above the 26 letters in the alphabet
        self._rotors[index] = chr(pos+ord('A')) # "chr" function translates a unicode (int) back into a character (str)
        self.update()


def enigma():
    """Runs the Enigma simulator."""
    model = EnigmaModel()
    view = EnigmaView(model)
    model.add_view(view)

# Startup code

if __name__ == "__main__":
    enigma()
