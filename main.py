import pyfiglet
from colorama import Fore, Style

class FigletASCIIArtGenerator:
    def __init__(self, font='standard'):
        self.figlet = pyfiglet.Figlet(font=font)

    def generate_ascii_art(self, text):
        ascii_art = self.figlet.renderText(text)
        print(ascii_art)

    def change_font(self, font):
        available_fonts = self.figlet.getFonts()
        if font in available_fonts:
            self.figlet = pyfiglet.Figlet(font=font)
            print(f"Font changed to '{font}'")
        else:
            print(f"Font '{font}' not found. Keeping the current font.")

def main():
    default_font = 'standard'
    figlet_ascii_art_generator = FigletASCIIArtGenerator(default_font)

    while True:
        print(Style.RESET_ALL)
        user_input = input("Enter your text or 'change_font' to set a new font (type 'exit' to quit): ")
        if user_input.lower() == 'exit':
            break
        elif user_input.lower() == 'change_font':
            new_font = input("Enter the font name: ")
            figlet_ascii_art_generator.change_font(new_font)
        else:
            color = input("Choose the color of your ascii text :\n BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE")
            color = color.upper()
            if(color == 'BLACK'):
                print(Fore.BLACK)
            elif(color=='RED'):
                print(Fore.RED)
            elif(color == "GREEN"):
                print(Fore.GREEN)
            elif(color == "YELLOW"):
                print(Fore.YELLOW)
            elif(color == "BLUE"):
                print(Fore.BLUE)
            elif(color == "MAGENTA"):
                print(Fore.MAGENTA)
            elif(color== "CYAN"):
                print(Fore.CYAN)
            elif(color == "WHITE"):
                print(Fore.WHITE)
            else:
                continue
            figlet_ascii_art_generator.generate_ascii_art(user_input)

if __name__ == "__main__":
    main()

