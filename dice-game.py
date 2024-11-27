import random
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.box import ROUNDED

console = Console()

# ==================== MESSAGE EMPHASIS

# Helper functions for styled messages
def success(message: str):
    console.print(message, style="bold green")

def error(message: str):
    console.print(message, style="bold red")

def info(message: str):
    console.print(message, style="bold cyan")

def warning(message: str):
    console.print(message, style="bold yellow")

# ==================== GAME STATS CLASS

class GameStats:
    def __init__(self):
        self.games_played = 0
        self.games_won = 0
        self.games_lost = 0
        self.highest_balance = 0
        
    def increment_played(self):
        self.games_played += 1
    
    def increment_won(self):
        self.games_won += 1
    
    def increment_lost(self):
        self.games_lost += 1
        
    def update_highest_balance(self, balance):
        # Update the highest balance if the current balance is greater
        if balance > self.highest_balance:
            self.highest_balance = balance
            
    def display(self):
        # Calculate win ratio
        win_ratio = (self.games_won / self.games_played) if self.games_played > 0 else 0

        # Create a table with the correct box style (ROUNDED in this case)
        table = Table(title="Game Stats", box=ROUNDED)
        table.add_column("Stat", justify="right", style="bold magenta")
        table.add_column("Value", justify="left", style="bold cyan")

        table.add_row("Total games played", str(self.games_played))
        table.add_row("Total games won", str(self.games_won))
        table.add_row("Total games lost", str(self.games_lost))
        table.add_row(f"[bold yellow]Highest balance achieved[/bold yellow]", f"[bold magenta]{self.highest_balance}[/bold magenta]")
        table.add_row("Win ratio", f"{win_ratio:.2f}")

        # Create a panel to contain the table
        panel = Panel(table, title="Game Summary", box=ROUNDED, expand=False)

        # Print the panel containing the table
        console.print(panel)

# ==================== MAIN MENU

def startmenu():
    console.print("\n========== Roll to Target ====================")
    console.print("\n[bold cyan]Welcome to the Main Menu![/bold cyan]")
    
    # initialise GameStats object
    game_stats = GameStats()
    
    while True:
        try:
            choice = int(input("Select an option:\n" +
                            "1. Read the rules.\n" +
                            "2. Play the game.\n" +
                            "3. Check the stats.\n" +
                            "4. Quit.\n"))
            
            if choice == 1:
                display_rules()
            
            elif choice == 2:
                # increment new_game count each time playgame function runs
                game_stats.increment_played()
                result = playgame(game_stats)
                
                # update games_won and games_lost based on results
                if result == "won":
                    game_stats.increment_won()
                elif result == "lost":
                    game_stats.increment_lost()
                
            elif choice == 3:
                game_stats.display()
                
            elif choice == 4:
                console.print("[bold red]Exiting the game. Goodbye![/bold red]")
                break
            
            else:
                console.print("[bold red]Invalid option. Please select a number between 1 and 4.[/bold red]")
        
        except ValueError:
            console.print("[bold red]Invalid input. Please enter a valid number.[/bold red]")

# ==================== GAME RULES

def display_rules():
    console.print(""" 
    ==============================  
            GAME RULES          
    ==============================

    1. **Objective**:
       - Reach or exceed the randomly assigned target score 
         by managing your bets and rolling the dice.

    2. **Starting Balance**:
       - The game begins with a balance entered by the player.

    3. **Betting**:
       - Before each round, you must place a bet.
       - You cannot bet more than your current balance.
       - Your bet must be greater than zero.

    4. **Dice Roll Outcomes**:
       - The result of each dice roll determines your winnings or losses:
         - **Rolling a 1 or 2**: You lose your bet.
         - **Rolling a 3 or 4**: You win 1.5 times your bet.
         - **Rolling a 5**: You win 2 times your bet.
         - **Rolling a 6**: Enter the **Bonus Round**.

    5. **Bonus Round**:
       - If you roll a **6**, you get a bonus roll:
         - **Rolling 1 to 3**: Lose half of your bet.
         - **Rolling 4 to 6**: Win 3 times your bet.

    6. **Game End Conditions**:
       - The game ends when:
         - Your balance reaches **zero**: You lose the game.
         - Your balance reaches or exceeds the target score: You win the game.

    7. **Additional Notes**:
       - Winnings and losses are automatically updated in your balance after each round.
       - Plan your bets carefully to reach the target score without running out of money.

    ==============================
    """)

# ==================== GAME

def playgame(game_stats):
    # Welcome Message
    console.print("[bold cyan]Welcome to Roll to Target![/bold cyan]", style="bold blue")
    console.print("Reach the target score by rolling the dice and managing your bets wisely.", style="dim")
    
    # Initialise game state
    starting_balance = int(input("Enter starting balance: "))
    balance = starting_balance
    target_score = random.randint(20, 100)
    round_number = 0

    # Display target score
    console.print(f"[bold magenta]Your target score is: {target_score}[/bold magenta]")
    
    while True:
        # Round and balance display
        info(f"\nRound: {round_number + 1}")
        info(f"Your current balance: [bold yellow]{balance}[/bold yellow]")
        
        # Input bet amount
        bet_amount = int(input("Enter bet amount: "))
        
        # Validate the bet amount
        if bet_amount > balance:
            error("You cannot bet more than your current balance.")
            continue
        if bet_amount <= 0:
            error("Bet amount must be greater than zero.")
            continue
        
        # Roll the dice
        roll_dice = random.randint(1, 6)
        console.print(f"[bold white]You rolled: {roll_dice}[/bold white]")
        
        # Determine the outcome
        if roll_dice == 1 or roll_dice == 2:
            error("You lost your bet.")
            balance -= bet_amount
        
        elif roll_dice == 3 or roll_dice == 4:
            win_amount = int(bet_amount * 1.5)
            success(f"You won: {win_amount}")
            balance += win_amount
        
        elif roll_dice == 5:
            win_amount = int(bet_amount * 2)
            success(f"You won: {win_amount}")
            balance += win_amount
        
        elif roll_dice == 6:
            warning("Bonus round!")
            bonus_roll = random.randint(1, 6)
            console.print(f"[bold white]Bonus roll: {bonus_roll}[/bold white]")
            
            if 1 <= bonus_roll <= 3:
                error("You lost your bet.")
                loss_amount = int(bet_amount // 2)
                error(f"You lost {loss_amount} in the bonus round.")
                balance -= loss_amount
            else:
                win_amount = bet_amount * 3
                success(f"You won {win_amount} in the bonus round!")
                balance += win_amount

        # Update the highest balance
        game_stats.update_highest_balance(balance)

        # Check game end conditions
        round_number += 1
        if balance <= 0:
            error("You ran out of money! Game over!")
            console.print("[bold white]Returning to main menu.[/bold white]\n")
            return "lost"
        
        elif balance >= target_score:
            success(f"Your total balance: {balance}")
            success(f"Congratulations! You've reached your target score of {target_score}!")
            console.print("[bold white]Returning to main menu.[/bold white]\n")
            return "won"

# ==================== MAIN ENTRY POINT

if __name__ == "__main__":
    startmenu()
