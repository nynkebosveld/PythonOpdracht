import argparse
import csv
import json
import os
from datetime import datetime, timedelta

__winc_id__ = "a2bc36ea784242e4989deb157d527ba0"
__human_name__ = "superpy"

def buy(args):
    f = open("bought.csv", "a", newline="")
    tup1 = (args.product_name, args.price, args.expiration_date)
    writer = csv.writer(f)
    writer.writerow(tup1)
    f.close()
    print('Okay')


def sell(args):
    i = 0
    f = open("bought.csv", "r", newline="")
    reader = csv.reader(f)
    for row in reader:
        if row[0] == args.product_name:
            i += 1
    fsold = open("sold.csv", "r", newline="")
    reader2 = csv.reader(fsold)
    for row2 in reader2:
        if row2[0] == args.product_name:
            i -= 1

    if i > 0:
        f = open("sold.csv", "a", newline="")
        tup1 = (args.product_name, args.price, datetime.now().strftime('%Y-%m-%d'))
        writer = csv.writer(f)
        writer.writerow(tup1)
        f.close()
        print('Okay')
        return
    print('ERROR: No such product found')


def inventory(args):
    expirate = date()
    if args.day == 'yesterday':
        expirate = date() - timedelta(days=1)
        print("yesterday inventory is: ")
    elif args.day == 'today' or args.day == 'now':
        print("today inventory is: ")
        expirate = date()
    elif args.day == 'tomorrow':
        print("tomorrow inventory is: ")
        expirate = date() + timedelta(days=1)

    expire = expirate.strftime('%Y-%m-%d')
    print(expire)
    f = open("bought.csv", "r", newline="")
    reader = csv.reader(f)
    counts = {}

    print('+--------------+-------+-----------+-----------------+')
    print('| Product name | Price | Quantity  | Expiration date |')
    print('+==============+=======+===========+=================+')

    f = open("bought.csv", "r", newline="")
    reader = csv.reader(f)

    for row in reader:
        # Check if the expiration date is greater than or equal to the current date
        if row[2] >= str(expire):
            # Get the item name
            name = row[0]

            if name in counts:
                counts[name] += 1
            else:
                counts[name] = 1

    for name, count in counts.items():
        print('| {}      | {}   | {}         | {}      |'.format(name, row[1], count, row[2]))
    print('+--------------+-------+-----------+-----------------+')


def profit(args):
    expirate = date()
    if args.day == 'yesterday':
        expirate = date() - timedelta(days=1)
        print("yesterday profit is: ")
    else:
        print("today profit is: ")
    f = open("sold.csv", "r", newline="")
    reader = csv.reader(f)
    price = 0.0
    for row in reader:
        if row[2] == str(expirate):
            price += float(row[1])

    f2 = open("bought.csv", "r", newline="")
    reader2 = csv.reader(f2)
    for row2 in reader2:
        if row2[2] == str(expirate):
            price -= float(row2[1])
    print(price)


def advance_time(days):
    today = datetime.now()

    new_date = today + timedelta(days=days)

    # Serialize the new date as a string
    new_date_str = new_date.strftime('%Y-%m-%d')

    # Create a dictionary with the original and new dates
    data = {
        "date": new_date_str
    }

    # Write the data to a JSON file
    with open("dates.json", "w") as f:
        json.dump(data, f)

    print("Date advanced to {}".format(new_date_str))


def revenue(args):
    expire = date()
    if args.day == 'yesterday':
        expire = date() - timedelta(days=1)
        print("yesterday revenue is: ")
    elif args.day == 'tomorrow':
        print("tomorrow revenue is: ")
        expire = date() + timedelta(days=1)
    elif args.day == 'date':
        expire = parse_date(args.date)
        print(expire, " revenue is: ")
    else:
        print("today revenue is: ")
        expire = date()

    expirate = expire.strftime('%Y-%m-%d')
    f = open("sold.csv", "r", newline="")
    reader = csv.reader(f)
    price = 0.0
    for row in reader:
        if row[2] == str(expirate):
            price += float(row[1])
    print(price)


def run(args):
    if not os.path.exists("bought.csv"):
        open("bought.csv", 'w').close()
        if not os.path.exists("sold.csv"):
            open("bought.csv", 'w').close()
            if not os.path.exists("dates.json"):
                open("bought.csv", 'w').close()

    if args.command == 'buy':
        buy(args)
    elif args.command == 'sell':
        sell(args)
    elif args.command == 'report':
        if args.options == 'inventory':
            inventory(args)
        if args.options == 'profit':
            profit(args)
        if args.options == 'revenue':
            revenue(args)
    elif args.advance_time:
        advance_time(args.advance_time)


def parse_date(date_str):
    return datetime.strptime(date_str, '%Y-%m-%d').date()


def date():
    if os.path.getsize("dates.json") == 0:
        return datetime.now().date()
    else:
        with open("dates.json", "r") as f:
            data = json.load(f)
        return datetime.strptime(data["date"], '%Y-%m-%d')


def main():
    parser = argparse.ArgumentParser(description='SuperPy', prog='superPy')

    parser.add_argument('command', choices=['buy', 'sell', 'report'], type=str, nargs='?')

    parser.add_argument('options', choices=['inventory', 'revenue', 'profit'], type=str, nargs='?')

    parser.add_argument('--now', dest='day', action='store_const', const='today', default='today')
    parser.add_argument('--yesterday', dest='day', action='store_const', const='yesterday')
    parser.add_argument('--tomorrow', dest='day', action='store_const', const='tomorrow')
    parser.add_argument('--date', type=parse_date, default=datetime.now())

    parser.add_argument('--product-name', type=str)
    parser.add_argument('--price', type=float)
    parser.add_argument('--expiration-date', type=parse_date, default=datetime.now())

    parser.add_argument("--advance-time", type=int, default=0, help="Number of days to advance the time")

    parser.add_argument('--version', help='help', action='version', version='%(prog)s 1.0')
    parser.set_defaults(func=run)
    args = parser.parse_args()
    args.func(args)


if __name__ == '__main__':
    main()
