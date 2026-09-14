# data.py

ONET_QUESTIONS = {
    "Realistic": [
        "Build kitchen cabinets", "Lay brick or tile", "Repair household appliances",
        "Raise fish in a fish hatchery", "Assemble electronic parts", "Drive a truck to deliver packages",
        "Test the quality of parts before shipment", "Repair and install locks", 
        "Set up and operate machines to make products", "Put out forest fires"
    ],
    "Investigative": [
        "Develop a new medicine", "Study ways to reduce water pollution", "Conduct chemical experiments",
        "Study the movement of planets", "Examine blood samples using a microscope", "Investigate the cause of a fire",
        "Develop a way to better predict the weather", "Work in a biology lab", "Invent a replacement for sugar",
        "Do laboratory tests to identify diseases"
    ],
    "Artistic": [
        "Write books or plays", "Paint sets for plays", "Play a musical instrument",
        "Compose or arrange music", "Draw pictures", "Create special effects for movies",
        "Write scripts for movies or television shows", "Perform jazz or tap dance", "Sing in a band", "Edit movies"
    ],
    "Social": [
        "Teach an individual an exercise routine", "Help people with personal or emotional problems",
        "Give career guidance to people", "Perform rehabilitation therapy", "Do volunteer work at a non-profit organization",
        "Teach children how to play sports", "Teach sign language to people who are deaf", "Help conduct a group therapy session",
        "Take care of children at a day-care center", "Teach a high-school class"
    ],
    "Enterprising": [
        "Negotiate business contracts", "Buy and sell stocks and bonds", "Manage a retail store",
        "Represent a client in a lawsuit", "Operate a beauty salon or barber shop", "Manage a department within a large company",
        "Start your own business", "Market a new line of clothing", "Sell merchandise at a department store", "Manage a clothing store"
    ],
    "Conventional": [
        "Develop a spreadsheet using computer software", "Proofread records or forms", "Install software across computers on a large network",
        "Calculate the wages of employees", "Inventory supplies using a hand-held computer", "Operate a calculator",
        "Keep shipping and receiving records", "Record rent payments", "Keep inventory records", "Stamp, sort, and distribute mail"
    ]
}

SHS_PATHWAYS = {
    "STEM": {"Degrees": ["BS Computer Science", "BS Civil Engineering", "BS Nursing"], "TESDA": ["NC II Computer Systems Servicing"], "CHED": ["Priority Group A - S&T"]},
    "ABM": {"Degrees": ["BS Accountancy", "BS Business Administration", "BS Real Estate"], "TESDA": ["NC III Bookkeeping"], "CHED": ["Priority Group B - Business"]},
    "HUMSS": {"Degrees": ["BA Communication", "BS Psychology", "BS Education"], "TESDA": ["NC II Caregiving"], "CHED": ["Priority Group C - Social Sciences"]},
    "TVL-ICT/Industrial": {"Degrees": ["BS Information Technology", "Bachelor in Industrial Tech"], "TESDA": ["NC II Web Development", "NC II Machining"], "CHED": ["Priority TVET-Aligned Group"]}
}