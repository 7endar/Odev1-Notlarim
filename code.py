# Fortune Teller Application

def fortune_teller(number):
    match number:
        case 1:
            return "Bu hafta son derece şanslısın, hemen bir piyango bileti almalısın!"
        case 2:
            return "Başarılı bir hafta olacak, işinde/eğitiminde önün oldukça açık!"
        case 3:
            return "Kalbin kırılacak gibi duruyor, hayır maalesef senden hoşlanmıyor :("
        case 4:
            return "Bu hafta oldukça eğlenceli geçecek gibi duruyor, ama sen yine de dozunu kaçırmamaya dikkat et."
        case 5:
            return "Tüm hafta reels kaydıracak gibisin, ne iyi ne kötü -_-"
        case _:
            return "Uzaylı istilası?"


def get_int(message):
    user_input = input(message)
    try:
        number = int(user_input)
        if 1 <= number <= 5:
            print(fortune_teller(number))
        else:
            get_int("Girdiğiniz sayı 1,2,3,4 veya 5 olmalıdır!\n")
    except ValueError:
        get_int("Hatalı değer girdiniz, tekrar deneyin!\n")


print("Fal Uygulamasına Hoşgeldiniz!")
get_int("1 ile 5 arasında bir değer girin: ")