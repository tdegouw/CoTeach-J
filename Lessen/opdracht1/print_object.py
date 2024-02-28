from pprint import pprint

def print_object(obj, toon_constanten: bool = False, toon_private: bool = False, toon_hidden: bool = False):
    # Controleren of het object een ingebouwd datatype is
    if isinstance(obj, (int, float, str, bool)):
        pprint(obj)
    # Controleren of het object een lijst is
    elif isinstance(obj, list):
        pprint(obj, indent=4)
    # Controleren of het object een dictionary is
    elif isinstance(obj, dict):
        pprint(obj, indent=4)
    # Controleren of het object een tuple is
    elif isinstance(obj, tuple):
        pprint(obj, indent=4)
    # Als het object een aangepaste klasse is, afdrukken van attributen en methoden
    else:
        pprint(obj)
        print(type(obj))
        public_methods=[]
        private_methods=[]
        public_variables=[]
        private_variables=[]
        hidden=[]
        constants=[]
        # Itereer over de attributen van het object
        for attr in dir(obj):
            # Controleer of het attribuut geen ingebouwde methode is
            # Haal de waarde van het attribuut op
            value = getattr(obj, attr)
            # Controleer of de waarde een methode is
            if attr.startswith("__"):
                if callable(value):
                    hidden.append(f"{attr}: <method>")
                else:
                    hidden.append(f"{attr}: {value}")
            elif attr.startswith("_"):
                if callable(value):
                    private_methods.append(f"{attr}: <method>")
                else:
                    private_variables.append(f"{attr}: {value}")
            elif callable(value):
                public_methods.append(f"{attr}: <method>")
            elif(attr == attr.upper()):
                constants.append(f"{attr}: {value}")
            else:
                public_variables.append(f"{attr}: {value}")

        if toon_hidden:
            print("[Hidden]")
            hidden.sort()
            for item in hidden:
                print(f"\t{item}")
        if toon_constanten:
            print("[Constants]")
            constants.sort()
            for item in constants:
                print(f"\t{item}")
        if toon_private:
            print("[Private variables]")
            for item in private_variables:
                private_variables.sort()
                print(f"\t{item}")
            print("[Private methods]")
            for item in private_methods:
                private_methods.sort()
                print(f"\t{item}")
        print("[Public variables]")
        public_variables.sort()
        for item in public_variables:
            print(f"\t{item}")
        print("[Public methods]")
        public_methods.sort()
        for item in public_methods:
            print(f"\t{item}")
