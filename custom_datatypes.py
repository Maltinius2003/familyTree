class Relation:
    def __init__(self):
        self.id = None
        self.relation_description = None
        self.type = None
        # z.B. bei Partnership: 0 Ehe, 1 Partnerschaft, 2 Verlobung, 3 Affäre
        # bei Godparenthood: 0 Taufpate, 1 Firmpate/Konfirmation

class Partnership(Relation):
    def __init__(self):
        super().__init__()
        self.children = [] # list of childrenids
        self.marriage_type = None # 0 unbekannt, 1 standesamtlich, 2 kirchlich, bei mehreren, mehrere Einträge
        self.churchMarriageType = None; #Religion der Partner abfragen oder andere
        self.start = None
        self.end = None
        self.brakes = []
        self.legallyBinding = None # rechtlich bindend? 0 unbekannt, 1 Ja (Stand im Wohnland), 2 Nur im Schließungsland, 3 Nein
        
class Godparenthood(Relation):
    def __init__(self):
        super().__init__()
        self.godparent_type = None # 0 Taufpate, 1 Firmung/Konfirmation, 2 Sonstige
        self.relation_description = None

class RelationBrake:
    def __init__(self):
        self.start = None
        self.end = None
        self.relation_break_description = None  # z.B. Zeitweilige Trennung

class Religion:
    def __init__(self):
        self.nuances = [] # z.B. Christentum, Katholisch, römisch-katholisch (only save numbers)
        self.start = None
        self.end = None
        self.religion_description = None

class Gender:
    def __init__(self):
        self.gen = None # None: keine Angabe, 0 unbekannt, 1 männlich, 2 weiblich, 3 divers
        self.type = None # None: keine Angabe, 0 unbekannt, 1 Sonstiges, 2 Geburt/Chromosomen/Anatomie, 3 Geburt/Anatomie, 4 Chromosomen, 5 Selbstidentifikation
        self.start = None
        self.end = None

class Name:
    def __init__(self):
        self.name_components = [] # zusammengesetzte Namen
        self.type = None
        # firstnames: None: keine Angabe, 0: unbekannt, 1: Sonstiges, 2: amtl. Vorname, 3: Rufname, 4: Spitzname, 5: Selbstgewählter Name
        # secondnames: None: keine Angabe, 0: unbekannt, 1: Sonstige, 2: amtl. Zweitname, 3: Rufname, 4: Spitzname, 4: Selbstgewählter Name
        # familynames: None: keine Angabe, 0: unbekannt, 1: Sonstige, 2: Geburtsname, 3: Ehename, 4: Betrachtung in Einzelteilen
        self.origin = None
        # firstnames: None: keine Angabe, 0: unbekannt, 1: Sonstige, 2: kein besonderer Ursprung, 2 nach Paten, 3 nach Verwandschaft, 4 nach Heiligem
        # secondnames: None: keine Angabe, 0: unbekannt, 1: Sonstige, 2: kein besonderer Ursprung, 2 nach Paten, 3 nach Verwandschaft, 4 nach Heiligem
        # familynames: None: keine Angabe, 0: unbekannt, 1: Sonstige, 2: kein besonderer Ursprung
        self.start = None
        self.end = None

class Name_component:
    def __init__(self):
        self.component = None
        self.origin = None
        # Vorname: None: keine Angabe, 0: unbekannt, 1: Sonstige, 2: kein besonderer Ursprung, 2 nach Paten, 3 nach Verwandschaft, 4 nach Heiligem
        # Zweitname: None: keine Angabe, 0: unbekannt, 1: Sonstige, 2: kein besonderer Ursprung, 2 nach Paten, 3 nach Verwandschaft, 4 nach Heiligem
        # Familienname: None: keine Angabe, 0: unbekannt, 1: Sonstige, 2: kein besonderer Ursprung, 2 Ehename, 3 Geburtsname
        self.name_givers = [] # ids (wenn im Stammbaum) or names (wenn nicht), bei Ehenamen Partner, auch wenn geschieden
        self.start = None
        self.end = None

class Academic_degree:
    def __init__(self):
        self.degree = None # None: keine Angabe, 0: unbekannt, 1: Sonstige, 2: Doktor, 3: Prof., 4: Magister, 5: Diplom, 6: Diplom Ingenieur, 7: Bachelor, 8: Master
        self.degree_abbr = None # z.B. Dr., Prof., Mag., Dipl., Dipl.-Ing., B., M.
        self.start = None # Datum der Verleihung
        self.end = None # Datum des Entzugs
        self.reason_for_withdrawal = None # None: keine Angabe, 0: unbekannt, 1: Sonstige, 2: Entzug, 3: Niederlegung