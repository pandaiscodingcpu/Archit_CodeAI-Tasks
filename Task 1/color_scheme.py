GREEN = "\033[92m"   # bright green
YELLOW = "\033[93m"  # bright yellow
GRAY = "\033[90m"    # gray
RESET = "\033[0m"    # reset color

def color_letter(letter, color):
    return f"{color}{letter}{RESET}"

def display_word(user_word, target_word):
    colored = []
    for i, ch in enumerate(user_word):
        if i < len(target_word) and ch == target_word[i]:
            colored.append(color_letter(ch, GREEN))
        elif ch in target_word:
            colored.append(color_letter(ch, YELLOW))
        else:
            colored.append(color_letter(ch, GRAY))
    return "".join(colored)
