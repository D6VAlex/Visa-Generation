#!/usr/bin/env python3
import json
import random
import string
import sys
from dataclasses import dataclass, asdict
from datetime import date, timedelta

BANNER = r"""
   ___         _     ___
  / __\ __ _  | |_  / __\ __ _  _ __
 / /   / _` | | __|/ /   / _` || '_ \
/ /___| (_| | | |_/ /___| (_| || | | |
\____/ \__,_|  \__\____/ \__, ||_| |_|
                         |___/
          Made By D6VAlex  
"""

def show_banner():
    print(BANNER)

def rand_name(lo=4, hi=10):
    v = "aeiouy"
    c = "bcdfghjklmnprstvwz"
    n = random.randint(lo, hi)
    out = []
    for i in range(n):
        out.append(random.choice(c if i % 2 == 0 else v))
    if random.random() < 0.3:
        out[-1] = random.choice(c)
    return "".join(out).capitalize()

def rand_street():
    tail = ["wood", "hill", "brook", "field", "ford", "dale", "crest",
            "ridge", "grove", "meadow", "bourne", "vale", "shaw", "moor",
            "haven", "stead", "port", "gate", "bridge", "stone"]
    s = rand_name(4, 8)
    if random.random() < 0.6:
        s += random.choice(tail)
    return s

def rand_suffix():
    v = "aeiou"
    c = "bcdfghjklmnprstvwz"
    n = random.randint(1, 3)
    return "".join(random.choice(c if i % 2 == 0 else v)
                   for i in range(n)).capitalize()

def rand_city():
    tail = ["ville", "ton", "burg", "field", "ford", "port", "mouth",
            "shire", "ham", "borough", "haven", "stead", "dale", "wood"]
    return rand_name(4, 8) + random.choice(tail)

def rand_region():
    return "".join(random.choice(string.ascii_uppercase)
                   for _ in range(random.randint(2, 3)))

def rand_country():
    tail = ["ia", "land", "stan", "nia", "ova", "ico", "ara", "esia",
            "onia", "ica", "ura"]
    return rand_name(4, 7) + random.choice(tail)

def rand_employer():
    a = rand_name(4, 8)
    b = random.choice(["Corp", "Inc", "LLC", "Group", "Co", "Ltd",
                       "Systems", "Solutions", "Works", "Labs",
                       "Holdings", "Partners", "Enterprises"])
    return f"{a} {b}"

def rand_job():
    verbs = ["Plan", "Build", "Lead", "Manage", "Run", "Drive", "Shape",
             "Guard", "Grow", "Fix", "Track", "Guide", "Coach", "Teach"]
    nouns = ["Ops", "Tech", "Data", "Sales", "Brand", "Growth", "Risk",
             "Comms", "Assets", "Code", "Flow", "Line", "Stack", "Site"]
    return f"{random.choice(nouns)} {random.choice(verbs)}r"

def rand_ua():
    plat = random.choice(["Windows NT 10.0; Win64; x64",
                          "Macintosh; Intel Mac OS X 14_3",
                          "X11; Linux x86_64"])
    eng = random.choice(["AppleWebKit/537.36", "AppleWebKit/605.1.15",
                         "Gecko/20100101"])
    ver = (f"{random.randint(80, 130)}.{random.randint(0, 9)}."
           f"{random.randint(0, 9)}.{random.randint(0, 99)}")
    return (f"Mozilla/5.0 ({plat}) {eng} "
            f"(KHTML, like Gecko) Chrome/{ver} Safari/537.36")

def rand_browser():
    return random.choice(["Chrome", "Safari", "Firefox", "Edge",
                          "Opera", "Brave", "Vivaldi", "Arc"])

def rand_device():
    b = ["iPhone", "Galaxy", "Pixel", "Xperia", "OnePlus", "Mi",
         "Surface", "ThinkPad", "MacBook", "ZenBook", "XPS"]
    return f"{random.choice(b)} {random.randint(9, 20)}"

def rand_domain():
    return rand_name(4, 8) + random.choice([".com", ".net", ".org",
                                            ".io", ".co", ".me", ".dev"])

def rand_email(fn, ln):
    dom = rand_domain()
    n = random.randint(1, 999)
    style = random.randint(0, 3)
    if style == 0:
        return f"{fn.lower()}.{ln.lower()}{n}@{dom}"
    if style == 1:
        return f"{fn.lower()}{ln.lower()}{n}@{dom}"
    if style == 2:
        return f"{fn.lower()[0]}{ln.lower()}{n}@{dom}"
    return f"{fn.lower()}{n}@{dom}"

def rand_issuer():
    return random.choice(["Visa", "Mastercard"]) + " " + \
        random.choice(["Classic", "Gold", "Platinum", "Signature",
                       "World", "Debit", "Business", "Corporate",
                       "Infinite", "Standard", "Rewards", "Test"])

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
    rights: str

def luhn(partial):
    t = 0
    for i, ch in enumerate(reversed(partial)):
        d = int(ch)
        if i % 2 == 0:
            d *= 2
            if d > 9:
                d -= 9
        t += d
    return str((10 - t % 10) % 10)

def make_pan(brand):
    if brand == "Visa":
        pre = "4" + "".join(random.choices(string.digits, k=5))
    else:
        if random.random() < 0.7:
            pre = str(random.randint(51, 55)) + \
                  "".join(random.choices(string.digits, k=4))
        else:
            pre = str(random.randint(2221, 2720))
    body = "".join(random.choices(string.digits, k=15 - len(pre)))
    start = pre + body
    return start + luhn(start)

def make_exp():
    f = date.today() + timedelta(days=random.randint(365, 365 * 5))
    return f"{f.month:02d}", str(f.year)

def make_dob():
    a = date(1960, 1, 1)
    b = date(2002, 12, 31)
    d = a + timedelta(days=random.randint(0, (b - a).days))
    return d.strftime("%m/%d/%Y")

def make_nid():
    s = random.randint(0, 3)
    if s == 0:
        return (f"{random.randint(100, 899):03d}-"
                f"{random.randint(10, 99):02d}-"
                f"{random.randint(1000, 9999)}")
    if s == 1:
        return (f"{''.join(random.choices(string.ascii_uppercase, k=2))}"
                f"{random.randint(100000, 999999)}"
                f"{random.choice(string.ascii_uppercase)}")
    if s == 2:
        return f"{random.randint(10000000000, 99999999999)}"
    return f"{random.randint(100000000, 999999999)}"

def make_postal():
    s = random.randint(0, 4)
    if s == 0:
        return f"{random.randint(10000, 99999)}"
    if s == 1:
        return (f"{random.choice(string.ascii_uppercase)}"
                f"{random.randint(1, 9)}"
                f"{random.choice(string.ascii_uppercase)} "
                f"{random.randint(1, 9)}"
                f"{random.choice(string.ascii_uppercase)}"
                f"{random.randint(1, 9)}")
    if s == 2:
        return f"{random.randint(1000, 9999)}"
    if s == 3:
        return f"{random.randint(10000, 99999)}-{random.randint(100, 999)}"
    return f"{random.randint(100000, 999999)}"

def make_phone():
    s = random.randint(0, 2)
    if s == 0:
        return (f"+1{random.randint(200, 989)}"
                f"{random.randint(200, 999)}{random.randint(1000, 9999)}")
    if s == 1:
        return f"+{random.randint(30, 99)}{random.randint(100000000, 999999999)}"
    return f"+{random.randint(200, 999)}{random.randint(10000000, 99999999)}"

def make_ip():
    return (f"{random.randint(11, 223)}.{random.randint(0, 255)}."
            f"{random.randint(0, 255)}.{random.randint(1, 254)}")

def make_currency():
    return random.choice(["USD", "EUR", "GBP", "CAD", "AUD", "JPY",
                          "CHF", "SEK", "NOK", "NZD", "MXN", "BRL"])

def make_rights():
    return "For Right My Right D6VAlex"

def make_card(brand):
    if brand == "Mix":
        brand = random.choice(["Visa", "Mastercard"])
    fn = rand_name()
    ln = rand_name()
    mm, yyyy = make_exp()
    return Card(
        brand=brand,
        pan=make_pan(brand),
        mm=mm,
        yyyy=yyyy,
        cvv=f"{random.randint(0, 999):03d}",
        issuer=rand_issuer(),
        name=f"{fn} {ln}",
        first=fn,
        last=ln,
        dob=make_dob(),
        national_id=make_nid(),
        street=f"{random.randint(1, 9899)} {rand_street()} {rand_suffix()}",
        city=rand_city(),
        region=rand_region(),
        postal=make_postal(),
        country=rand_country(),
        country_code="".join(random.choices(string.ascii_uppercase, k=2)),
        phone=make_phone(),
        email=rand_email(fn, ln),
        employer=rand_employer(),
        job_title=rand_job(),
        salary=random.randint(24000, 210000),
        currency=make_currency(),
        ip=make_ip(),
        device=rand_device(),
        browser=rand_browser(),
        user_agent=rand_ua(),
        rights=make_rights(),
    )

def gen(brand, n):
    out = []
    seen = set()
    while len(out) < n:
        c = make_card(brand)
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
        c.browser, c.user_agent, c.brand, c.issuer, c.rights,
    ])

def ask(q, default=None, valid=None):
    while True:
        suf = f" [{default}]" if default is not None else ""
        raw = input(f"{q}{suf}: ").strip()
        if not raw and default is not None:
            return default
        if not raw:
            print("  need an answer here.")
            continue
        if valid and raw.lower() not in valid:
            print(f"  pick one of: {', '.join(valid)}")
            continue
        return raw

def ask_int(q, default, lo, hi):
    while True:
        raw = input(f"{q} [{default}]: ").strip()
        if not raw:
            return default
        try:
            n = int(raw)
        except ValueError:
            print("  that's not a number.")
            continue
        if n < lo or n > hi:
            print(f"  keep it between {lo} and {hi}.")
            continue
        return n

def ask_yes(q, default="n"):
    r = ask(q + " (y/n)", default=default, valid=["y", "n"])
    return r.lower() == "y"

def main():
    show_banner()

    brand = ask("brand  (visa / mastercard / mix)", default="mix",
                valid=["visa", "mastercard", "mix"]).capitalize()
    if brand == "Mix":
        brand = "Mix"

    n = ask_int("how many cards", default=10, lo=1, hi=100000)
    fmt = ask("format (pipe / json / csv)", default="pipe",
              valid=["pipe", "json", "csv"]).lower()

    seed_raw = ask("seed (blank = random)", default="")
    seed = None
    if seed_raw:
        try:
            seed = int(seed_raw)
        except ValueError:
            print("  seed wasn't a number, ignoring it.")
    if seed is not None:
        random.seed(seed)

    save = ask_yes("save to a file?", default="n")
    path = None
    if save:
        ext = {"pipe": "txt", "json": "jsonl", "csv": "csv"}[fmt]
        path = ask("filename", default=f"cards.{ext}")

    print()
    print(f"  making {n} {brand} card(s) in {fmt}...")

    cards = gen(brand, n)

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
        print(f"  wrote {len(cards)} cards to {path}")
    else:
        print()
        print(blob)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n  canceled.")
        sys.exit(0)