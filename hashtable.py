#  creates a HashTable class
class HashTable(object):
    def __init__(self, length=40):
        # Initializes the array with empty values.
        self.array = [None] * length

    def hash(self, key):
        # Get the index of the array for a specific string key.
        length = len(self.array)
        return hash(key) % length

    # Rubric: E - 'insert' function for storing package information
    def insert(self, key, value):
        # Adds a value to the array by its key.
        index = self.hash(key)
        if self.array[index] is not None:
            # Checks if the key already exists.
            for kvp in self.array[index]:
                # If key is found, then update its current value to the new value.
                if kvp[0] == key:
                    kvp[1] = value
                    break
            else:
                # No existing key was found. Add it to the end.
                self.array[index].append([key, value])
        else:
            # This index is empty. We should initiate 
            # a list and append our key-value-pair to it.
            self.array[index] = []
            self.array[index].append([key, value])

    # Rubric: F - 'lookup' function for retrieving package information by package ID
    def lookup(self, key):
        """Get a value by key"""
        index = self.hash(key)
        if self.array[index] is None:
            raise KeyError()
        else:
            # Checks if the key exists. If so, returns its value.
            for kvp in self.array[index]:
                if kvp[0] == key:
                    return kvp[1]

            # If no return was done during loop, the key didn't exist.
            raise KeyError()
