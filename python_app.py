import random

def get_user_choice():
    while True:
        user_choice = input("Taş, kağıt yada Makas seç: ").lower()
        if user_choice in ["taş","kağıt","makas"]:
            return user_choice
        else:
            print("Geçersiz bir seçim yaptınız. Lütfen Taş, Kağıt yada Makas olarak giriniz")

def get_computer_choice():
    if random.randint(1, 3) == 1:
        return "taş"
    elif random.randint(1, 3) == 2:
        return "kağıt"
    else:
        return "makas"

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "Berabere"
    elif (user_choice == "taş" and computer_choice == "makas") or \
         (user_choice == "kağıt" and computer_choice == "taş") or \
         (user_choice == "makas" and computer_choice == "kağıt"):
        return "Kullanıcı"
    else:
        return "Bilgisayar"

def main():

    user_score = 0
    computer_score = 0

    while user_score < 3 and computer_score < 3:
        print(f"\nKullanıcı Puanı: {user_score} - Bilgisayar Puanı: {computer_score}")
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print(f"\nSiz: {user_choice} - Bilgisayar: {computer_choice}")

        winner = determine_winner(user_choice, computer_choice)
        if winner == "berabere":
            print("Berabere")
        else:
            print(f"{winner.capitalize()} kazandı")
            
            if winner == "Kullanıcı":
                user_score += 1
            elif winner == "Bilgisayar":
                computer_score += 1

        print("\nOyun Bitti")
        if user_score > computer_score:
            print("Tebrikler, kullanıcı kazandı")
        else:
            print("Üzgünüz, Bilgisayar kazandı")

if __name__ == "__main__":
    main()
