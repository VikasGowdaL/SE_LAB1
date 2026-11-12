BERTHS = ["SU", "LB", "MB", "UB", "LB", "MB", "UB", "SL"]

def parse_pnr(pnr):
    if not isinstance(pnr, str):
        return None
    if len(pnr) != 10 or not pnr.isascii() or not pnr.isdigit():
        return None
    return int(pnr[0]), int(pnr[1:])

def journey_distance(distances_csv):
    if not isinstance(distances_csv, str) or not distances_csv.strip():
        return None
    try:
        distances = [int(d.strip()) for d in distances_csv.split(",")]
        if not distances:
            return None
        return distances[-1] - distances[0]
    except ValueError:
        return None

def berth_type(seat):
    if not isinstance(seat, str):
        return None
    try:
        coach, number = seat.split("-")
        if not coach.strip() or not number.isdigit():
            return None
        number = int(number)
        if number <= 0:
            return None
        return coach.upper(), BERTHS[number % 8]
    except ValueError:
        return None

def main():
    print("==== Running parse_pnr ====")
    user_input = input("Enter a 10 digit PNR (e.g. 4521367890): ")
    result = parse_pnr(user_input)
    print("Zone and Number:", result)

    print("\n==== Running journey_distance ====")
    user_input = input("Enter station distances as CSV (e.g. 0,120,340): ")
    result = journey_distance(user_input)
    print("Total Distance:", result)

    print("\n==== Running berth_type ====")
    user_input = input("Enter coach and seat (e.g. S3-45): ")
    result = berth_type(user_input)
    print("Coach and Berth:", result)

if __name__ == "__main__":
    main()
