#Just For Fun ! 
#For entertainment purposes only; I take no responsibility for anyone who uses this in an unethical manner
import json
import random
import string
import sys
from dataclasses import dataclass, asdict
from datetime import date, timedelta

first_names = [
    "James", "Marcus", "Elena", "Dana", "Victor", "Nadia", "Omar",
    "Lucas", "Ingrid", "Tomas", "Ruth", "Andre", "Kaya", "Felix",
    "Mona", "Hugo", "Sofia", "Dmitri", "Alicia", "Noah", "Maya",
    "Ethan", "Zara", "Leo", "Iris", "Caleb", "Nina", "Rafael",
    "Yuki", "Aisha", "Bruno", "Clara", "Kaito", "Lena", "Mateo",
    "Anya", "Diego", "Freya", "Gabriel", "Hana", "Ismail", "Julia",
    "Karim", "Lucia", "Milan", "Nora", "Oscar", "Paula", "Quentin",
    "Rosa", "Samuel", "Talia", "Umar", "Valentina", "Wesley", "Ximena",
    "Yusuf", "Zoe", "Anders", "Bianca", "Cheng", "Dalia", "Emre",
    "Farah", "Gustav", "Hiro", "Ines", "Jonas", "Keiko", "Liam",
    "Mei", "Nikolai", "Olga", "Pedro", "Rania", "Sven", "Tariq",
    "Amara", "Bo", "Camila", "Davi", "Eunji", "Fatima", "Giulia",
    "Hassan", "Ivy", "Jin", "Kofi", "Leila", "Minh", "Nia", "Owen",
    "Pablo", "Ravi", "Sana", "Theo", "Uma", "Viktor", "Wen", "Yara",
    "Zain", "Aiko", "Bilal", "Carmen", "Dmitri", "Esme", "Finn",
]

last_names = [
    "Brennan", "Kovac", "Okafor", "Delgado", "Whitmore", "Ivanova",
    "Haddad", "Nair", "Moreau", "Lindqvist", "Novak", "Adeyemi",
    "Ferreira", "Sato", "Brandt", "Rahman", "Costa", "Vogel",
    "Mercer", "Klein", "Duarte", "Sullivan", "Petrov", "Mensah",
    "Tanaka", "Rossi", "Dubois", "Schmidt", "Silva", "Kim",
    "Andersen", "Bauer", "Chen", "Diaz", "Eriksen", "Fischer",
    "Garcia", "Hansen", "Ibrahim", "Jensen", "Kaur", "Larsen",
    "Martinez", "Nakamura", "Olsen", "Park", "Quinn", "Rivera",
    "Santos", "Thompson", "Ueda", "Vargas", "Wagner", "Xu",
    "Yamamoto", "Zhang", "Almeida", "Bianchi", "Castillo", "Dvorak",
    "Esposito", "Fontaine", "Gomez", "Horvath", "Ito", "Jung",
    "Kowalski", "Lombardi", "Mbeki", "Nielsen", "Okonkwo", "Pereira",
    "Russo", "Sorensen", "Takahashi", "Urbina", "Voss", "Weber",
    "Yilmaz", "Zimmer", "Achebe", "Bakker", "Chowdhury", "Diallo",
    "Ekwueme", "Farouk", "Gupta", "Huang", "Iqbal", "Janssen",
    "Khan", "Lopez", "Mwangi", "Nguyen", "Oyelaran", "Patel",
    "Qureshi", "Reddy", "Sharma", "Tran", "Uddin", "Vasquez",
]

streets = [
    "Maple", "Oak", "Cedar", "Birch", "Franklin", "Lincoln",
    "Highland", "Riverside", "Sunset", "Park", "Washington",
    "Lake", "Willow", "Chestnut", "Madison", "Jefferson",
    "Adams", "Jackson", "Elm", "Pine", "Spruce", "Ash",
    "Bridge", "Church", "Mill", "Spring", "Union", "Market",
    "Center", "Valley", "Hill", "Forest", "Garden", "Meadow",
    "Harbor", "Bay", "Ridge", "Mountain", "Meadowbrook", "Colonial",
    "Hampton", "Briarwood", "Crestview", "Fairview", "Glenwood",
    "Greenwood", "Hillcrest", "Inglewood", "Kingsway", "Lakeshore",
    "Northgate", "Oakwood", "Pinecrest", "Quail", "Rosedale",
    "Sherwood", "Thornton", "Underwood", "Victoria", "Westfield",
]

suffixes = [
    "St", "Ave", "Rd", "Blvd", "Ln", "Dr", "Ct", "Way", "Pl", "Ter",
    "Trail", "Circle", "Square", "Highway", "Parkway", "Pike",
    "Row", "Walk", "Path", "Bend", "Crossing", "Point", "Grove",
    "Alley", "Pass", "Loop", "Ridge", "Mews", "Close", "Green",
]

places = [
    # United States
    ("New York", "NY", "100", "212", "US", "United States"),
    ("Brooklyn", "NY", "112", "718", "US", "United States"),
    ("Chicago", "IL", "606", "312", "US", "United States"),
    ("Houston", "TX", "770", "713", "US", "United States"),
    ("Phoenix", "AZ", "850", "602", "US", "United States"),
    ("Philadelphia", "PA", "191", "215", "US", "United States"),
    ("San Diego", "CA", "921", "619", "US", "United States"),
    ("Dallas", "TX", "752", "214", "US", "United States"),
    ("Austin", "TX", "787", "512", "US", "United States"),
    ("Jacksonville", "FL", "322", "904", "US", "United States"),
    ("Columbus", "OH", "432", "614", "US", "United States"),
    ("Charlotte", "NC", "282", "704", "US", "United States"),
    ("Denver", "CO", "802", "303", "US", "United States"),
    ("Seattle", "WA", "981", "206", "US", "United States"),
    ("Boston", "MA", "021", "617", "US", "United States"),
    ("Nashville", "TN", "372", "615", "US", "United States"),
    ("Portland", "OR", "972", "503", "US", "United States"),
    ("Atlanta", "GA", "303", "404", "US", "United States"),
    ("Miami", "FL", "331", "305", "US", "United States"),
    ("Minneapolis", "MN", "554", "612", "US", "United States"),
    ("Las Vegas", "NV", "891", "702", "US", "United States"),
    ("Detroit", "MI", "482", "313", "US", "United States"),
    ("San Francisco", "CA", "941", "415", "US", "United States"),
    ("Los Angeles", "CA", "900", "213", "US", "United States"),
    ("San Jose", "CA", "951", "408", "US", "United States"),
    ("Sacramento", "CA", "958", "916", "US", "United States"),
    ("Orlando", "FL", "328", "407", "US", "United States"),
    ("Tampa", "FL", "336", "813", "US", "United States"),
    ("Pittsburgh", "PA", "152", "412", "US", "United States"),
    ("Cleveland", "OH", "441", "216", "US", "United States"),
    ("St. Louis", "MO", "631", "314", "US", "United States"),
    ("Kansas City", "MO", "641", "816", "US", "United States"),
    ("Indianapolis", "IN", "462", "317", "US", "United States"),
    ("Milwaukee", "WI", "532", "414", "US", "United States"),
    ("Cincinnati", "OH", "452", "513", "US", "United States"),
    ("Raleigh", "NC", "276", "919", "US", "United States"),
    ("Richmond", "VA", "232", "804", "US", "United States"),
    ("New Orleans", "LA", "701", "504", "US", "United States"),
    ("Salt Lake City", "UT", "841", "801", "US", "United States"),
    ("Albuquerque", "NM", "871", "505", "US", "United States"),
    # Canada
    ("Toronto", "ON", "M5", "416", "CA", "Canada"),
    ("Vancouver", "BC", "V6", "604", "CA", "Canada"),
    ("Montreal", "QC", "H3", "514", "CA", "Canada"),
    ("Calgary", "AB", "T2", "403", "CA", "Canada"),
    ("Ottawa", "ON", "K1", "613", "CA", "Canada"),
    ("Edmonton", "AB", "T5", "780", "CA", "Canada"),
    # United Kingdom
    ("London", "ENG", "EC1", "20", "GB", "United Kingdom"),
    ("Manchester", "ENG", "M1", "161", "GB", "United Kingdom"),
    ("Birmingham", "ENG", "B1", "121", "GB", "United Kingdom"),
    ("Leeds", "ENG", "LS1", "113", "GB", "United Kingdom"),
    ("Glasgow", "SCT", "G1", "141", "GB", "United Kingdom"),
    ("Edinburgh", "SCT", "EH1", "131", "GB", "United Kingdom"),
    # Ireland
    ("Dublin", "D", "D01", "1", "IE", "Ireland"),
    ("Cork", "CO", "T12", "21", "IE", "Ireland"),
    # Germany
    ("Berlin", "BE", "101", "30", "DE", "Germany"),
    ("Munich", "BY", "803", "89", "DE", "Germany"),
    ("Hamburg", "HH", "200", "40", "DE", "Germany"),
    ("Frankfurt", "HE", "603", "69", "DE", "Germany"),
    # France
    ("Paris", "IDF", "750", "1", "FR", "France"),
    ("Lyon", "ARA", "690", "4", "FR", "France"),
    ("Marseille", "PAC", "130", "4", "FR", "France"),
    # Netherlands
    ("Amsterdam", "NH", "101", "20", "NL", "Netherlands"),
    ("Rotterdam", "ZH", "301", "10", "NL", "Netherlands"),
    # Spain
    ("Madrid", "MD", "280", "91", "ES", "Spain"),
    ("Barcelona", "CT", "080", "93", "ES", "Spain"),
    # Italy
    ("Rome", "RM", "001", "06", "IT", "Italy"),
    ("Milan", "MI", "201", "02", "IT", "Italy"),
    # Australia
    ("Sydney", "NSW", "200", "2", "AU", "Australia"),
    ("Melbourne", "VIC", "300", "3", "AU", "Australia"),
    ("Brisbane", "QLD", "400", "7", "AU", "Australia"),
    ("Perth", "WA", "600", "8", "AU", "Australia"),
    # New Zealand
    ("Auckland", "AUK", "101", "9", "NZ", "New Zealand"),
    ("Wellington", "WGN", "601", "4", "NZ", "New Zealand"),
    # Japan
    ("Tokyo", "13", "100", "3", "JP", "Japan"),
    ("Osaka", "27", "530", "6", "JP", "Japan"),
    # Brazil
    ("Sao Paulo", "SP", "010", "11", "BR", "Brazil"),
    ("Rio de Janeiro", "RJ", "200", "21", "BR", "Brazil"),
    # Mexico
    ("Mexico City", "CDMX", "010", "55", "MX", "Mexico"),
    ("Guadalajara", "JAL", "441", "33", "MX", "Mexico"),
]

country_phone = {
    "United States": ("+1", 10),
    "Canada": ("+1", 10),
    "United Kingdom": ("+44", 10),
    "Ireland": ("+353", 9),
    "Germany": ("+49", 11),
    "France": ("+33", 9),
    "Netherlands": ("+31", 9),
    "Spain": ("+34", 9),
    "Italy": ("+39", 10),
    "Australia": ("+61", 9),
    "New Zealand": ("+64", 9),
    "Japan": ("+81", 10),
    "Brazil": ("+55", 11),
    "Mexico": ("+52", 10),
}

domains = [
    "gmail.com", "outlook.com", "yahoo.com", "proton.me", "icloud.com",
    "aol.com", "hotmail.com", "mail.com", "zoho.com", "gmx.com",
    "yandex.com", "fastmail.com", "tutanota.com", "hey.com",
]

employers = [
    "Acme Corp", "Northwind Traders", "Globex", "Initech",
    "Umbrella LLC", "Stark Industries", "Wayne Enterprises",
    "Soylent Co", "Cyberdyne", "Massive Dynamic", "Hooli",
    "Vandelay Imports", "Pendant Publishing", "Dunder Mifflin",
    "Wonka Industries", "Gringotts", "Monarch Solutions",
    "Blue Sun", "Aperture Science", "Black Mesa", "Tyrell Corp",
    "Oceanic Airlines", "Virtucon", "Bluth Company", "Prestige Worldwide",
    "Sterling Cooper", "Pierce & Pierce", "Kramerica", "Vandelay",
    "Cogswell Cogs", "Spacely Sprockets", "Initech Systems",
    "Rekall Inc", "Omni Consumer Products", "Buy n Large",
    "Encom", "Weyland-Yutani", "Sirius Cybernetics", "MomCorp",
    "Planet Express", "Duff Brewing", "Springfield Nuclear",
]

job_titles = [
    "Analyst", "Engineer", "Manager", "Consultant", "Designer",
    "Technician", "Specialist", "Coordinator", "Director",
    "Supervisor", "Accountant", "Developer", "Architect",
    "Administrator", "Associate", "Executive", "Officer",
    "Lead", "Principal", "Scientist", "Researcher", "Planner",
    "Strategist", "Representative", "Agent", "Auditor",
    "Buyer", "Clerk", "Controller", "Counsel", "Economist",
    "Editor", "Estimator", "Examiner", "Inspector", "Instructor",
    "Investigator", "Librarian", "Mechanic", "Nurse", "Paralegal",
    "Pharmacist", "Photographer", "Pilot", "Producer", "Programmer",
    "Receptionist", "Recruiter", "Reporter", "Secretary", "Surveyor",
    "Teacher", "Therapist", "Translator", "Treasurer", "Writer",
]

devices = [
    "iPhone 15 Pro", "iPhone 15", "iPhone 14", "iPhone 13",
    "iPhone SE", "Samsung Galaxy S24 Ultra", "Samsung Galaxy S24",
    "Samsung Galaxy S23", "Samsung Galaxy A54", "Google Pixel 8 Pro",
    "Google Pixel 8", "Google Pixel 7a", "OnePlus 12", "OnePlus 11",
    "Xiaomi 14", "Xiaomi 13", "Huawei P60", "Sony Xperia 1 V",
    "iPad Pro 12.9", "iPad Air", "iPad Mini", "Galaxy Tab S9",
    "MacBook Pro 14", "MacBook Pro 16", "MacBook Air M2",
    "Dell XPS 13", "Dell XPS 15", "HP Spectre x360", "Lenovo ThinkPad X1",
    "Surface Pro 9", "Surface Laptop 5", "ASUS ZenBook 14",
    "Acer Swift 3", "Razer Blade 15", "Framework Laptop 13",
]

browsers = [
    ("Chrome", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"),
    ("Chrome", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"),
    ("Safari", "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.3 Safari/605.1.15"),
    ("Safari", "Mozilla/5.0 (iPhone; CPU iPhone OS 17_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.3 Mobile/15E148 Safari/604.1"),
    ("Firefox", "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0"),
    ("Firefox", "Mozilla/5.0 (X11; Linux x86_64; rv:123.0) Gecko/20100101 Firefox/123.0"),
    ("Edge", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0"),
    ("Opera", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 OPR/108.0.0.0"),
    ("Brave", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Brave/122"),
    ("Vivaldi", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Vivaldi/6.6"),
]

visa_bins = [
    ("411111", "Visa Test"), ("401288", "Visa Classic"),
    ("424242", "Visa Classic"), ("453201", "Visa Platinum"),
    ("491761", "Visa Debit"), ("414720", "Visa Signature"),
    ("400000", "Visa Generic"), ("426684", "Visa Rewards"),
    ("448590", "Visa Business"), ("411770", "Visa Electron"),
    ("402400", "Visa Classic"), ("455660", "Visa Gold"),
    ("456789", "Visa Infinite"), ("476173", "Visa Debit"),
]

mc_bins = [
    ("510510", "MC Test"), ("555555", "MC World"),
    ("222300", "MC New Range"), ("541029", "MC Standard"),
    ("522516", "MC Platinum"), ("530125", "MC Debit"),
    ("550000", "MC Generic"), ("222100", "MC New Range"),
    ("272099", "MC New Range"), ("519999", "MC World Elite"),
    ("544444", "MC Gold"), ("535353", "MC Business"),
    ("556677", "MC Corporate"), ("526789", "MC World"),
]

@dataclass
class Card:
    brand: str
    pan: str
    mm: str
    yyyy: str
    cvv: str
    issuer: str
    name: str
    first: str
    last: str
    dob: str
    national_id: str
    street: str
    city: str
    region: str
    postal: str
    country: str
    country_code: str
    phone: str
    email: str
    employer: str
    job_title: str
    salary: int
    currency: str
    ip: str
    device: str
    browser: str
    user_agent: str


def check_digit(partial):
    total = 0
    for i, ch in enumerate(reversed(partial)):
        d = int(ch)
        if i % 2 == 0:
            d *= 2
            if d > 9:
                d -= 9
        total += d
    return str((10 - total % 10) % 10)


def make_pan(brand):
    pool = visa_bins if brand == "Visa" else mc_bins
    prefix, issuer = random.choice(pool)
    body = "".join(random.choices(string.digits, k=9))
    start = prefix + body
    return start + check_digit(start), issuer


def make_exp():
    future = date.today() + timedelta(days=random.randint(365, 365 * 5))
    return f"{future.month:02d}", str(future.year)


def make_dob():
    start = date(1960, 1, 1)
    end = date(2002, 12, 31)
    d = start + timedelta(days=random.randint(0, (end - start).days))
    return d.strftime("%m/%d/%Y")


def make_ssn():
    area = random.randint(100, 899)
    while area == 666:
        area = random.randint(100, 899)
    return f"{area:03d}-{random.randint(10, 99):02d}-{random.randint(1000, 9999)}"


def make_national_id(country):
    if country == "United States":
        return make_ssn()
    if country == "Canada":
        return f"{random.randint(100, 999)}-{random.randint(100, 999)}-{random.randint(100, 999)}"
    if country == "United Kingdom":
        return f"QQ{random.randint(10, 99)}{random.randint(10, 99)}{random.randint(10, 99)}C"
    if country == "Ireland":
        return f"{random.randint(1000000, 9999999)}{random.choice('ABDEFGHJKLMNPQRSTVWXYZ')}"
    if country == "Germany":
        return f"{random.randint(10000000000, 99999999999)}"
    if country == "France":
        return f"{random.randint(1, 2)}{random.randint(60, 99)}{random.randint(10, 12)}{random.randint(100, 999)}{random.randint(100, 999)}{random.randint(10, 99)}"
    if country == "Netherlands":
        return f"{random.randint(100000000, 999999999)}"
    if country == "Spain":
        return f"{random.randint(10000000, 99999999)}{random.choice('TRWAGMYFPDXBNJZSQVHLCKE')}"
    if country == "Italy":
        return f"{random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')}{random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')}{random.randint(10000, 99999)}"
    if country == "Australia":
        return f"{random.randint(100, 999)} {random.randint(100, 999)} {random.randint(100, 999)}"
    if country == "New Zealand":
        return f"{random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')}{random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')}{random.randint(10000, 99999)}"
    if country == "Japan":
        return f"{random.randint(1000, 9999)} {random.randint(1000, 9999)} {random.randint(1000, 9999)}"
    if country == "Brazil":
        return f"{random.randint(100, 999)}.{random.randint(100, 999)}.{random.randint(100, 999)}-{random.randint(10, 99)}"
    if country == "Mexico":
        return f"{random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')}{random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')}{random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')}{random.randint(100000, 999999)}H{random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')}{random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')}{random.randint(10, 99)}"
    return f"{random.randint(100000000, 999999999)}"


def make_postal(prefix, country):
    if country == "United States":
        return f"{prefix}{random.randint(10, 99)}"
    if country == "Canada":
        return f"{prefix[0]}{random.randint(1, 9)}{random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')} {random.randint(1, 9)}{random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')}{random.randint(1, 9)}"
    if country == "United Kingdom":
        return f"{prefix} {random.randint(1, 9)}{random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')}{random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')}"
    if country == "Ireland":
        return f"{prefix}{random.randint(10, 99)} {random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')}{random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')}{random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')}{random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')}"
    if country == "Germany":
        return f"{prefix}{random.randint(10, 99)}"
    if country == "France":
        return f"{prefix}{random.randint(10, 99)}"
    if country == "Netherlands":
        return f"{prefix}{random.randint(10, 99)} {random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')}{random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')}"
    if country == "Spain":
        return f"{prefix}{random.randint(10, 99)}"
    if country == "Italy":
        return f"{prefix}{random.randint(10, 99)}"
    if country == "Australia":
        return f"{prefix}{random.randint(10, 99)}"
    if country == "New Zealand":
        return f"{prefix}{random.randint(10, 99)}"
    if country == "Japan":
        return f"{prefix}-{random.randint(1000, 9999)}"
    if country == "Brazil":
        return f"{prefix}{random.randint(10000, 99999)}-{random.randint(100, 999)}"
    if country == "Mexico":
        return f"{prefix}{random.randint(10, 99)}"
    return f"{prefix}{random.randint(10, 99)}"


def make_phone(country, area):
    code, length = country_phone.get(country, ("+1", 10))
    digits_needed = max(0, length - len(area))
    rest = "".join(str(random.randint(0, 9)) for _ in range(digits_needed))
    return f"{code}{area}{rest}"


def make_email(fn, ln):
    style = random.randint(0, 4)
    dom = random.choice(domains)
    n = random.randint(1, 999)
    if style == 0:
        return f"{fn.lower()}.{ln.lower()}{n}@{dom}"
    if style == 1:
        return f"{fn.lower()}{ln.lower()}{n}@{dom}"
    if style == 2:
        return f"{fn.lower()[0]}{ln.lower()}{n}@{dom}"
    if style == 3:
        return f"{fn.lower()}{n}@{dom}"
    return f"{fn.lower()}.{ln.lower()[0]}{n}@{dom}"


def make_ip():
    return f"{random.randint(11, 223)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(1, 254)}"


def currency_for(country):
    return {
        "United States": "USD", "Canada": "CAD", "United Kingdom": "GBP",
        "Ireland": "EUR", "Germany": "EUR", "France": "EUR",
        "Netherlands": "EUR", "Spain": "EUR", "Italy": "EUR",
        "Australia": "AUD", "New Zealand": "NZD", "Japan": "JPY",
        "Brazil": "BRL", "Mexico": "MXN",
    }.get(country, "USD")


def make_card(brand, country_filter=None):
    pan, issuer = make_pan(brand)
    fn = random.choice(first_names)
    ln = random.choice(last_names)

    pool = places
    if country_filter:
        pool = [p for p in places if p[5] == country_filter] or places
    city, region, postal_prefix, area, cc, country = random.choice(pool)

    street = f"{random.randint(1, 9899)} {random.choice(streets)} {random.choice(suffixes)}"
    mm, yyyy = make_exp()
    bname, ua = random.choice(browsers)

    return Card(
        brand=brand, pan=pan, mm=mm, yyyy=yyyy,
        cvv=f"{random.randint(0, 999):03d}", issuer=issuer,
        name=f"{fn} {ln}", first=fn, last=ln,
        dob=make_dob(), national_id=make_national_id(country),
        street=street, city=city, region=region,
        postal=make_postal(postal_prefix, country),
        country=country, country_code=cc,
        phone=make_phone(country, area),
        email=make_email(fn, ln),
        employer=random.choice(employers),
        job_title=random.choice(job_titles),
        salary=random.randint(28000, 185000),
        currency=currency_for(country),
        ip=make_ip(), device=random.choice(devices),
        browser=bname, user_agent=ua,
    )


def gen_cards(brand, n, country_filter=None):
    out, seen = [], set()
    while len(out) < n:
        b = random.choice(["Visa", "Mastercard"]) if brand == "Mix" else brand
        c = make_card(b, country_filter)
        if c.pan in seen:
            continue
        seen.add(c.pan)
        out.append(c)
    return out


def as_pipe(c):
    return "|".join([
        c.pan, c.mm, c.yyyy, c.cvv, c.name, c.first, c.last,
        c.dob, c.national_id, c.street, c.city, c.region, c.postal,
        c.country, c.country_code, c.phone, c.email, c.employer,
        c.job_title, str(c.salary), c.currency, c.ip, c.device,
        c.browser, c.user_agent, c.brand, c.issuer,
    ])

def ask(prompt, default=None, valid=None):
    while True:
        suffix = f" [{default}]" if default is not None else ""
        raw = input(f"{prompt}{suffix}: ").strip()
        if not raw and default is not None:
            return default
        if not raw:
            print("need an answer here.")
            continue
        if valid and raw.lower() not in valid:
            print(f"pick one of: {', '.join(valid)}")
            continue
        return raw


def ask_int(prompt, default, lo, hi):
    while True:
        raw = input(f"{prompt} [{default}]: ").strip()
        if not raw:
            return default
        try:
            n = int(raw)
        except ValueError:
            print("that's not a number.")
            continue
        if n < lo or n > hi:
            print(f"keep it between {lo} and {hi}.")
            continue
        return n


def ask_yes(prompt, default="n"):
    r = ask(prompt + " (y/n)", default=default, valid=["y", "n"])
    return r.lower() == "y"


def banner():
    print()
    print("cardgen")
    print("full info")
    print(f"  {len(first_names)} first names, {len(last_names)} last names,")
    print(f"  {len(places)} places, {len(employers)} employers.")
    print()


def main():
    banner()

    brand = ask("By D6VAlex > brand ? > visa / mastercard / mix", default="mix",
                valid=["visa", "mastercard", "mix"]).capitalize()
    if brand == "Mix":
        brand = "Mix"

    countries = sorted(set(p[5] for p in places))
    print("countries available:")
    country_pick = ask("country (blank = any)", default="")
    country_filter = None
    if country_pick:
        for c in countries:
            if c.lower() == country_pick.lower():
                country_filter = c
                break
        if not country_filter:
            print("didn't match a country, using any.")

    n = ask_int("how many cards", default=10, lo=1, hi=100000)

    fmt = ask("format (pipe / json / csv)", default="pipe",
              valid=["pipe", "json", "csv"]).lower()

    seed_raw = ask("seed (blank = random)", default="")
    seed = None
    if seed_raw:
        try:
            seed = int(seed_raw)
        except ValueError:
            print("seed wasn't a number, ignoring it.")

    if seed is not None:
        random.seed(seed)

    save = ask_yes("save to a file?", default="n")
    path = None
    if save:
        ext = {"pipe": "txt", "json": "jsonl", "csv": "csv"}[fmt]
        path = ask("filename", default=f"cards.{ext}")

    print()
    label = country_filter or "any country"
    print(f"making {n} {brand} card(s) · {label} · {fmt}...")

    cards = gen_cards(brand, n, country_filter)

    if fmt == "json":
        lines = [json.dumps(asdict(c), separators=(",", ":")) for c in cards]
    elif fmt == "csv":
        header = list(asdict(cards[0]).keys())
        lines = [",".join(header)]
        for c in cards:
            row = list(asdict(c).values())
            lines.append(",".join(
                f'"{v}"' if isinstance(v, str) and "," in v else str(v)
                for v in row))
    else:
        lines = [as_pipe(c) for c in cards]

    blob = "\n".join(lines) + "\n"

    if path:
        with open(path, "w", encoding="utf-8") as f:
            f.write(blob)
        print(f"wrote {len(cards)} cards to {path}")
    else:
        print()
        print(blob)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n canceled.")
        sys.exit(0)