unit_types = [
    ("DP", "Dispatched"),
    ("AK", "Acknowledged"),
    ("ER", "Enroute"),
    ("OS", "Onscene"),
    ("TR", "Transport"),
    ("TA", "Transport Arrived"),
    ("AQ", "Available in Quarters"),
    ("AR", "Available on Radio / Cleared"),
    ("AE", "Available Onscene")
]

call_types = [
    # Aid
    ("AA", "Auto Aid"),
    ("MU", "Mutual Aid"),
    ("ST", "Strike Team"),
    # Aircraft
    ("AE", "Aircraft Emergency"),
    ("AES", "Aircraft Emergency Standby"),
    ("AC", "Aircraft Crash"),
    ("LZ", "Landing Zone"),
    # Alarm
    ("OA", "Alarm"),
    ("FA", "Fire Alarm"),
    ("SD", "Smoke Detector"),
    ("WFA", "Waterflow Alarm"),
    ("MA", "Manual Alarm"),
    ("CMA", "Carbon Monoxide"),
    ("AED", "AED Alarm"),
    ("TRBL", "Trouble Alarm"),
    # Assist
    ("FL", "Flooding"),
    ("LR", "Ladder Request"),
    ("LA", "Lift Assist"),
    ("PS", "Public Assist"),
    ("PA", "Police Assist"),
    ("SH", "Sheared Hydrant"),
    # Explosion
    ("EX", "Explosion"),
    ("PE", "Pipeline Emergency"),
    ("TE", "Transformer Explosion"),
    # Fire
    ("SF", "Structural Fire"),
    ("VEG", "Vegetation Fire"),
    ("WSF", "Confirmed Structure Fire"),
    ("WVEG", "Confirmed Vegetation Fire"),
    ("CF", "Commercial Fire"),
    ("RF", "Residential Fire"),
    ("WCF", "Working Commercial Fire"),
    ("WRF", "Working Residential Fire"),
    ("VF", "Vehicle Fire"),
    ("EF", "Extinguished Fire"),
    ("IF", "Illegal Fire"),
    ("MF", "Marine Fire"),
    ("OF", "Outside Fire"),
    ("PF", "Pole Fire"),
    ("GF", "Refuse / Garbage Fire"),
    ("FULL", "Full Assignment"),
    ("AF", "Appliance Fire"),
    ("CHIM", "Chimney Fire"),
    ("CB", "Controlled Burn / Prescribed Fire"),
    ("ELF", "Electric Fire"),
    ("FIRE", "Fire"),
    # Hazard
    ("GAS", "Gas Main"),
    ("HC", "Hazardous Condition"),
    ("BT", "Bomb Threat"),
    ("HMR", "Hazmat Response"),
    ("TD", "Tree Down"),
    ("EE", "Electrical Emergency"),
    ("EM", "Emergency"),
    ("ER", "Emergency Response"),
    ("WE", "Water Emergency"),
    # Investigation
    ("INV", "Investigation"),
    ("HMI", "Hazmat Investigation"),
    ("OI", "Odor Investigation"),
    ("SI", "Smoke Investigation"),
    ("AI", "Arson Investigation"),
    # Lockout
    ("LO", "Lockout"),
    ("CL", "Commercial Lockout"),
    ("RL", "Residential Lockout"),
    ("VL", "Vehicle Lockout"),
    # Medical
    ("ME", "Medical Emergency"),
    ("IFT", "Interfacility Transfer"),
    ("MCI", "Multi Casualty"),
    # Natural
    ("FLW", "Flood Warning"),
    ("TOW", "Tornado Warning"),
    ("TSW", "Tsunami Warning"),
    ("EQ", "Earthquake"),
    # Other/Non-Emergency
    ("CA", "Community Activity"),
    ("FW", "Fire Watch"),
    ("TRNG", "Training"),
    ("TEST", "Test"),
    ("NO", "Notification"),
    ("STBY", "Standby"),
    # Rescue
    ("RES", "Rescue"),
    ("CR", "Cliff Rescue"),
    ("CSR", "Confined Space"),
    ("RR", "Rope Rescue"),
    ("TR", "Technical Rescue"),
    ("Trench Rescue", "TNR"),
    ("WR", "Water Rescue"),
    ("AR", "Animal Rescue"),
    ("ELR", "Elevator Rescue"),
    ("USAR", "Urban Search and Rescue"),
    ("VS", "Vessel Sinking"),
    # Vehicle
    ("TCE", "Expanded Traffic Collision"),
    ("TC", "Traffic Collision"),
    ("TCT", "Traffic Collision Involving Train"),
    ("RTE", "Railroad / Train Emergency"),
    ("TCS", "Traffic Collision Involving Structure"),
    # Wires
    ("WA", "Wires Arcing"),
    ("WD", "Wires Down")
]

agency_list = [
    ("ANAPD", "Anaheim Police Department"),
    ("BUP", "Buena Park Police Department"),
    ("CYP", "Cypress Police Department"),
    ("FTV", "Fountain Valley Police Department"),
    ("FUL", "Fullerton Police Department"),
    ("LAH", "La Habra Police Department"),
    ("LAL", "Los Alamitos Police Department"),
    ("LPM", "La Palma Police Department"),
    ("SLB", "Seal Beach Police Department"),
    ("TUS", "Tustin Police Department"),
    ("WSM", "Westminster Police Department"),
    ("LF", "Orange County Sheriff's Department"),
    ("YL", "Orange County Sheriff's Department"),
    ("MV", "Orange County Sheriff's Department"),
    ("RS", "Orange County Sheriff's Department"),
    ("SA", "Santa Ana Police Department"),
    ("GG", "Garden Grove Police Department"),
    ("SC", "Orange County Sheriff's Department"),
    ("AV", "Orange County Sheriff's Department"),
    ("LN", "Orange County Sheriff's Department"),
    ("ST", "Orange County Sheriff's Department"),
    ("NH", "Orange County Sheriff's Department"),
    ("RO", "Orange County Sheriff's Department"),
    ("CN", "Orange County Sheriff's Department"),
    ("CS", "Orange County Sheriff's Department"),
    ("CZ", "Orange County Sheriff's Department"),
    ("JW", "Orange County Sheriff's Department"),
    ("LM", "Orange County Sheriff's Department"),
    ("LD", "Orange County Sheriff's Department"),
    ("LH", "Orange County Sheriff's Department"),
    ("FL", "Orange County Sheriff's Department"),
    ("RV", "Orange County Sheriff's Department"),
    ("SJ", "Orange County Sheriff's Department"),
    ("SI", "Orange County Sheriff's Department"),
    ("SN", "Orange County Sheriff's Department"),
    ("TC", "Orange County Sheriff's Department"),
    ("VP", "Orange County Sheriff's Department"),
    ("DP", "Orange County Sheriff's Department"),
]

city_list = [
    ("ANAPD", "Anaheim"),
    ("BUP", "Buena Park"),
    ("CYP", "Cypress"),
    ("FTV", "Fountain Valley"),
    ("FUL", "Fullerton"),
    ("LAH", "La Habra"),
    ("LAL", "Los Alamitos"),
    ("LPM", "La Palma"),
    ("SLB", "Seal Beach"),
    ("TUS", "Tustin"),
    ("WSM", "Westminster"),
    ("LF", "Orange County"),
    ("YL", "Orange County"),
    ("MV", "Orange County"),
    ("RS", "Orange County"),
    ("SA", "Santa Ana"),
    ("GG", "Garden Grove"),
    ("SC", "Orange County"),
    ("AV", "Orange County"),
    ("LN", "Orange County"),
    ("ST", "Orange County"),
    ("NH", "Orange County"),
    ("RO", "Orange County"),
    ("CN", "Orange County"),
    ("CS", "Orange County"),
    ("CZ", "Orange County"),
    ("JW", "Orange County"),
    ("LM", "Orange County"),
    ("LD", "Orange County"),
    ("LH", "Orange County"),
    ("FL", "Orange County"),
    ("RV", "Orange County"),
    ("SJ", "Orange County"),
    ("SI", "Orange County"),
    ("SN", "Orange County"),
    ("TC", "Orange County"),
    ("VP", "Orange County"),
    ("DP", "Orange County"),
]
