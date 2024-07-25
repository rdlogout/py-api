import argparse
from tabulate import tabulate
import json
from repo import FoodRepository
food_repo = FoodRepository()

def list_food(args):
    items = food_repo.get_all_food(start=args.offset, limit=args.limit, q=args.query, zipcode=args.zipcode, max_distance=args.max_distance)
    print(tabulate(items, headers='keys', tablefmt='heavy_grid'))
    # print(json.dumps(items, indent=2))

def get_food(args):
    food = food_repo.get_food_by_id(args.food_id)
    if food:
        print(json.dumps(food, indent=2))
    else:
        print("Food not found")

def save_email(args):
    # In a real implementation, you'd save this to a database or file
    print(f"Saving email {args.email} for food ID {args.food_id}")

def main():
    parser = argparse.ArgumentParser(description="Food Repository CLI")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # List food command
    list_parser = subparsers.add_parser("list", help="List all food items")
    list_parser.add_argument("--offset", type=int, default=0, help="Start offset")
    list_parser.add_argument("--limit", type=int, default=24, help="Number of items to retrieve")
    list_parser.add_argument("--query", "-q", type=str, default="", help="Search query")
    list_parser.add_argument("--zipcode", "-z", type=str, default="", help="Zipcode")
    list_parser.add_argument("--max_distance", "-d", type=int, default=40, help="Max distance in miles")
    list_parser.set_defaults(func=list_food)

    # Get food by ID command
    get_parser = subparsers.add_parser("get", help="Get food item by ID")
    get_parser.add_argument("food_id", help="ID of the food item")
    get_parser.set_defaults(func=get_food)

    # Save email command
    email_parser = subparsers.add_parser("notify", help="Save email for notification")
    email_parser.add_argument("food_id", help="ID of the food item")
    email_parser.add_argument("email", help="Email address for notification")
    email_parser.set_defaults(func=save_email)

    args = parser.parse_args()
    if hasattr(args, 'func'):
        args.func(args)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()