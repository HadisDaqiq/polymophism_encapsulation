############
# Part 1   #
############

# this is a subclass MelonType(parentclass_object)
class MelonType(object):
    """A species of melon at a melon farm."""

    def __init__(self, code, first_harvest, color, is_seedless, is_bestseller, 
                 name):
        """Initialize a melon."""

        # class attributes
        self.pairings = []
        self.name = name
        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = True
        self.is_bestseller = True
        # Fill in the rest

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""
        self.pairings.append(pairing)

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        self.code = new_code


# these are functions(not indented/not inside the subclass)
def make_melon_types():
    """Returns a list of current melon types."""

    # list of objects of class MelonType
    all_melon_types = []

    # instantiating
    # instances = class MelonType (attributes)
    musk = MelonType("musk",1998,"green",True,True, "Muskmelon")
    # call add_pairing method to add pairings to instance's pairing attribute
    musk.add_pairing("mint")
    all_melon_types.append(musk)

    cas = MelonType("cas",2003,"orange", True, False, "Casaba")
    cas.add_pairing("strawberries")
    cas.add_pairing("mint")
    all_melon_types.append(cas)

    cren = MelonType("cren",1996,"green",True,False, "Crenshaw")
    cren.add_pairing("proscuitto")
    all_melon_types.append(cren)

    yw = MelonType("yw",2013,"yellow",True,True, "Yellow Watermelon")
    yw.add_pairing("ice cream")
    all_melon_types.append(yw)

    # all_melons_types returns instance information
    return all_melon_types


def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    # melon_types is the list of class instances
    # melon is ONE of the class instance 
    for melon in melon_types:
        # getting the each instance and it's instance pairing list
       print(f"{melon.name} pairs with: \n - {melon.pairings}")



def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    # dictionary whos keys: reporting codes as strings
    # values as melontype instances (for that code)
    
    melon_dict = {}

    for melon in melon_types:
        # dict[code] = name
        melon_dict[melon.code] = melon.name

    return melon_dict
#invalid arugment
print(melons_by_id = make_melon_type_lookup(melon_types)


############melons_by_id[
# Part 2]   #
############

class Melon(object):
    """A melon in a melon harvest."""

    def __init__(self, mel_type, shape_r, color_r, field_num, harvester):
        """initializing melon class (attributes)"""

        self.mel_type = mel_type
        self.shape_r = shape_r
        self.color_r = color_r
        self.field_num = field_num
        self.harvester = harvester

    def is_sellable(self):
        """returns true or false if melons are sellable or not sellable

        shape rating and color rating must be greater than 5
        and should not come from field number 3 to be sellable 
        """

        if (self.shape_r and self.color_r > 5) and field_num != 3:
            return True 

        return False


def make_melons(melon_types):
    """Returns a list of Melon objects."""
    sell_melon = []

    melon_1 = Melon(melons_by_id["yw"], 8, 7, 3, "Sheila")
    sell_melon.append(melon_1)

    melon_2 = Melon(melons_by_id["yw"], 3, 4, 2, "Sheila")
    sell_melon.append(melon_2)
    
    melon_3 = Melon(melons_by_id["yw"], 9, 8, 3, "Sheila")
    sell_melon.append(melon_3)

    melon_4 = Melon(melons_by_id["cas"], 10, 6, 35, "Sheila")
    sell_melon.append(melon_4)

    melon_5 = Melon(melons_by_id["cren"], 8, 9, 35, "Michael")
    sell_melon.append(melon_5)

    melon_6 = Melon(melons_by_id["cren"], 8, 2, 35, "Michael")
    sell_melon.append(melon_6)

    melon_7 = Melon(melons_by_id["cren"], 2, 3, 4, "Michael")
    sell_melon.append(melon_7)

    melon_8 = Melon(melons_by_id["musk"], 6, 10, 3, "Sheila")
    sell_melon.append(melon_8)

    return sell_melon

print(melons_data = make_melons(melons_by_id()))

sellable = melon.is_sellable()
def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    for melon in melon_data:

        print(f" Havested by {melon.harvester} from Field {melon.field_num} {sellable}")

# get_sellability_report(make_melons(melons_data))


