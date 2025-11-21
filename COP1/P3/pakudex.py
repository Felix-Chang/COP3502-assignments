from pakuri import Pakuri

class Pakudex():
    def __init__(self, capacity = 20):
        self.capacity = capacity
        self.pakuri_list = []

    def get_size(self):
        return len(self.pakuri_list)

    def get_capacity(self):
        return self.capacity
    
    def get_species_array(self):
        if not self.pakuri_list:
            return None
        else:
            species_list = []
            for pakuri in self.pakuri_list:
                species_list.append(pakuri.get_species())
            return species_list
        
    def get_stats(self, species):
        for pakuri in self.pakuri_list:
            if pakuri.get_species() == species:
                return [pakuri.get_attack(), pakuri.get_defense(), pakuri.get_speed()]
        return None
    
    def sort_pakuri(self):
        self.pakuri_list.sort(key=lambda x: x.get_species())

    def add_pakuri(self, species):
        # Check if full
        if len(self.pakuri_list) >= self.capacity:
            return False
        
        # Check for dupes
        for entry in self.pakuri_list:
            if entry.get_species() == species:
                return False
        
        # Add Pakruri
        else:
            self.pakuri_list.append(Pakuri(species))
            return True
        
    def evolve_species(self, species):
        for pakuri in self.pakuri_list:
            if pakuri.get_species() == species:
                pakuri.evolve()
                return True
        return False
        