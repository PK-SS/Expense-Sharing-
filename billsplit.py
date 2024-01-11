class BillSplitter:
    def _init_(self):
        self.users = {}
        self.expenses = []

    def add_user(self, name):
        self.users[name] = 0

    def add_expense(self, payer, amount, participants):
        total_participants = len(participants)
        if total_participants == 0:
            print("Error: At least one participant is required.")
            return

        individual_share = amount / total_participants
        self.users[payer] += amount

        for participant in participants:
            self.users[participant] -= individual_share

        self.expenses.append({
            'payer': payer,
            'amount': amount,
            'participants': participants
        })

    def print_balances(self):
        print("Current Balances:")
        for user, balance in self.users.items():
            print(f"{user}: {balance}")

    def settle_expenses(self):
        for user, balance in self.users.items():
            if balance < 0:
                for other_user, other_balance in self.users.items():
                    if other_balance > 0:
                        amount_to_settle = min(-balance, other_balance)
                        print(f"{user} owes {other_user}: {amount_to_settle}")
                        self.users[user] += amount_to_settle
                        self.users[other_user] -= amount_to_settle
                        balance += amount_to_settle
                        other_balance -= amount_to_settle
                        if balance == 0:
                            break

    def run(self):
        while True:
            print("\nOptions:")
            print("1. Add user")
            print("2. Add expense")
            print("3. Print balances")
            print("4. Settle expenses")
            print("5. Exit")

            choice = input("Enter your choice (1-5): ")

            if choice == '1':
                name = input("Enter user name: ")
                self.add_user(name)
            elif choice == '2':
                payer = input("Enter payer's name: ")
                amount = float(input("Enter the expense amount: "))
                participants_str = input("Enter participants' names separated by commas: ")
                participants = [p.strip() for p in participants_str.split(',')]
                self.add_expense(payer, amount, participants)
            elif choice == '3':
                self.print_balances()
            elif choice == '4':
                self.settle_expenses()
            elif choice == '5':
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    bill_splitter = BillSplitter()
    bill_splitter.run()