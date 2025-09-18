inventory = {"Dune": 15, "1984": 5, "Fondation": 3}


# will be used for showing all or specific items
def show_articles(articles=inventory):
    for article_name, article_qty in articles.items():
        print(f"{article_name} => {article_qty} unit(s)")


def add_article():
    # repeat until user enters valid data
    while not (article_name := input("[+] Enter new article's name: ").strip()):
        print("[!] Invalid name, please type again.")

    # repeat until user enters valid data
    while not (
        (article_qty := input("[+] Enter article quantity: ").strip())
        and article_qty.isdigit()
    ):
        print("[!] Invalid quantity, please type again.")

    global inventory
    inventory[article_name] = int(article_qty)


def search_articles():
    article_name = input("[+] Enter article's name (empty to skip): ").strip()
    OPERATORS = (">", ">=", "<", "<=", "=")

    # repeat until user enters valid data
    while not (
        (article_qty := input("[+] Enter article's quantity (empty to skip): ").strip())
        and article_qty.isdigit()
        or (article_qty == "")
    ):
        print("[!] Invalid quantity, please type again.")

    comparison_operator = None
    filtered_inventory = inventory.copy()

    # comparison operator should be should be considered only when article_qty is set
    if article_qty.isdigit():

        # repeat until user enters one of the valid operators or an emtpy space
        while not (
            (
                comparison_operator := input(
                    f"[+] (article.qty [OPERATOR] {article_qty} ) Operator should be either (>, >=, <, <=, = or empty for =): "
                ).strip()
            )
            in [*OPERATORS, ""]
        ):
            print("[!] Invalid input, please type again.")

        # comparison logic
        match comparison_operator:
            case ">":
                filtered_inventory = {
                    **dict(
                        filter(
                            lambda i: int(article_qty) < i[1],
                            filtered_inventory.items(),
                        )
                    )
                }
            case "<":
                filtered_inventory = {
                    **dict(
                        filter(
                            lambda i: int(article_qty) > i[1],
                            filtered_inventory.items(),
                        )
                    )
                }
            case ">=":
                filtered_inventory = {
                    **dict(
                        filter(
                            lambda i: int(article_qty) >= i[1],
                            filtered_inventory.items(),
                        )
                    )
                }
            case "<=":
                filtered_inventory = {
                    **dict(
                        filter(
                            lambda i: int(article_qty) <= i[1],
                            filtered_inventory.items(),
                        )
                    )
                }
            case "=" | _:
                filtered_inventory = {
                    **dict(
                        filter(
                            lambda i: int(article_qty) == i[1],
                            filtered_inventory.items(),
                        )
                    )
                }

    filtered_inventory = {
        **dict(
            filter(lambda i: article_name in i[0].lower(), filtered_inventory.items())
        )
    }

    print(f"[+] {len(filtered_inventory)} Articles Found.")

    show_articles(filtered_inventory)


def remove_article():
    # no empty article name
    while not (article_name := input("[+] Enter article's name: ").strip()):
        print(f"[!] Invalid article name.")
        pass

    if article_name not in inventory.keys():
        print(f'[!] Article "{article_name}" doesn\'t exist.')
    else:
        print(f"[+] {article_name} deleted.")


def modify_article():
    # check validity & existance
    while not (article_name := input("[+] Enter article's name: ").strip()):
        print(f"[!] Invalid article name.")
        pass

    if article_name not in inventory.keys():
        print(f'[!] Article "{article_name}" doesn\'t exist.')
    else:
        article_qty = inventory[article_name]

        # no need for validation either use the new name keep the old one
        new_article_name = input(
            f'[+] Enter Article\'s Name (empty to keep it "{article_name}"): '
        ).strip()

        # keep the old name only if the new name isn't set
        new_article_name = new_article_name if new_article_name else article_name

        # qty validation either empty or a valid digit
        while not (
            (
                new_article_qty := input(
                    f'[+] Enter Article\'s Quantity (empty to keep it "{article_qty}"): '
                )
                .strip()
            ).isdigit()
            or (article_qty == "")
        ):
            print("[!] Invalid quantity, please type again.")

        # keep the old name only if the new name isn't set
        new_article_qty = int(new_article_qty) if (new_article_qty != "") else article_qty

        # remove the old article
        inventory.pop(article_name)
        # create the new article
        inventory[new_article_name] = new_article_qty


        print(f"[+] Updated to {article_name} : {article_qty} -> {new_article_name} : {new_article_qty}")


def show_menu():
    for i in range(len(MENU)):
        (label, _) = MENU[i]
        print(f"{i + 1}) {label}")


MENU = (
    ("Show Articles", show_articles),
    ("Search Article(s)", search_articles),
    ("Add an Article", add_article),
    ("Remove an Article", remove_article),
    ("Modify an Article", modify_article),
    ("Show This Menu", show_menu),
    ("Quit", exit),
)

show_menu()

while True:
    try:
        while (n := input("-> ")) and n.isdigit() and 1 <= (n := int(n)) <= (len(MENU)):
            (label, fn) = MENU[n - 1]
            fn()

    except KeyboardInterrupt:
        exit()
