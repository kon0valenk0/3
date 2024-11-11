# gtrans.py
from my_package.gtrans_module import TransLate, LangDetect, CodeLang, LanguageList

if __name__ == "__main__":
    print(TransLate("Hello", "en", "uk"))
    print(LangDetect("Привіт, how are you?", "all"))
    print(CodeLang("uk"))
    print(LanguageList("screen", "Добрий день"))
