import json
import os
import argparse

DATA_FILE = "tickets.json"


def load_data():
    """Load ticket data from disk or return a default structure."""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {"flights": {}, "tickets": []}


def save_data(data):
    """Persist ticket data to disk."""
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


def add_flight(number, origin, destination, seats):
    """Register a new flight in the system."""
    data = load_data()
    if number in data["flights"]:
        raise SystemExit("Flight already exists")
    data["flights"][number] = {
        "origin": origin,
        "destination": destination,
        "seats": seats,
        "booked": 0,
    }
    save_data(data)


def book_ticket(flight_number, passenger_name):
    """Book a ticket for a passenger if seats are available."""
    data = load_data()
    flight = data["flights"].get(flight_number)
    if not flight:
        raise SystemExit("Flight not found")
    if flight["booked"] >= flight["seats"]:
        raise SystemExit("No seats available")
    ticket_id = len(data["tickets"]) + 1
    data["tickets"].append({
        "ticket_id": ticket_id,
        "passenger_name": passenger_name,
        "flight_number": flight_number,
    })
    flight["booked"] += 1
    save_data(data)
    print(f"Ticket {ticket_id} booked for {passenger_name} on flight {flight_number}")


def list_flights():
    """Show all registered flights and their seat availability."""
    data = load_data()
    if not data["flights"]:
        print("No flights found")
        return
    for number, info in data["flights"].items():
        print(
            f"{number}: {info['origin']} -> {info['destination']} "
            f"({info['booked']}/{info['seats']} seats booked)"
        )


def list_tickets():
    """Show all booked tickets."""
    data = load_data()
    if not data["tickets"]:
        print("No tickets booked")
        return
    for t in data["tickets"]:
        print(f"{t['ticket_id']}: {t['passenger_name']} on flight {t['flight_number']}")


def main():
    parser = argparse.ArgumentParser(description="Airport ticket management system")
    sub = parser.add_subparsers(dest="command")

    add = sub.add_parser("add-flight", help="Register a new flight")
    add.add_argument("number")
    add.add_argument("origin")
    add.add_argument("destination")
    add.add_argument("seats", type=int)

    book = sub.add_parser("book", help="Book a ticket")
    book.add_argument("number", help="Flight number")
    book.add_argument("name", help="Passenger name")

    sub.add_parser("list-flights", help="List available flights")
    sub.add_parser("list-tickets", help="List booked tickets")

    args = parser.parse_args()

    if args.command == "add-flight":
        add_flight(args.number, args.origin, args.destination, args.seats)
    elif args.command == "book":
        book_ticket(args.number, args.name)
    elif args.command == "list-flights":
        list_flights()
    elif args.command == "list-tickets":
        list_tickets()
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
