# Python Projekty

Zbiór małych projektów Python, które tworzę ucząc się programowania, ze szczególnym naciskiem na podstawy i cyberbezpieczeństwo.

## Projekty

### 🔐 Sprawdzacz siły hasła

Program sprawdzający, czy podane hasło spełnia podstawowe wymagania bezpieczeństwa (długość, wielkie/małe litery, cyfry, znaki specjalne).

**Użyte technologie:** pętle, warunki, stringi

📁 [`Sprawdzacz sily hasla/Sprawdzacz sily hasla.py`](./Sprawdzacz%20sily%20hasla/Sprawdzacz%20sily%20hasla.py)

---

### 🎲 Generator haseł

Program generujący losowe, silne hasło o długości podanej przez użytkownika (8-30 znaków), złożone z małych/wielkich liter, cyfr i znaków specjalnych.

**Użyte technologie:** pętle, moduł `random`, moduł `string`, sprawdzanie poprawności danych od użytkownika

📁 [`Generator hasel/Generator hasel.py`](./Generator%20hasel/Generator%20hasel.py)

---

### 🔑 Szyfr Cezara

Program szyfrujący tekst metodą przesunięcia liter w alfabecie o wartość podaną przez użytkownika (klasyczny szyfr Cezara). Cyfry, spacje i znaki specjalne pozostają bez zmian, szyfrowane są tylko litery.

**Użyte technologie:** pętle, moduł `string`, kody znaków (`ord`, `chr`), sprawdzanie poprawności danych od użytkownika

📁 [`Szyfr cezara/Szyfr Cezara.py`](./Szyfr%20cezara/Szyfr%20Cezara.py)

---

### 📊 Analizator logów

Program czytający plik z logami (adres IP i godzina w każdej linii), który liczy, ile razy pojawił się każdy adres IP. Użytkownik podaje bezpieczny limit, a program wypisuje adresy, które go przekraczają, razem z godziną pierwszej i ostatniej próby. Tak można wykryć podejrzaną aktywność, np. próby włamania metodą brute force. Limit można zmieniać bez ponownego uruchamiania programu.

**Użyte technologie:** odczyt plików, słowniki i listy, `split`, pętle, sprawdzanie poprawności danych od użytkownika

📁 [`Analizator logow/Analizator logow.py`](./Analizator%20logow/Analizator%20logow.py)

---

### 🕵️ Sprawdzacz wycieków haseł

Program sprawdzający, czy podane hasło wyciekło w publicznych wyciekach danych, z wykorzystaniem API serwisu Have I Been Pwned. Hasło jest zamieniane na skrót (hash SHA-1), a do serwera wysyłane jest tylko pierwsze 5 znaków tego skrótu. Serwer odsyła listę pasujących końcówek, a porównanie robi program lokalnie. Dzięki temu serwis nigdy nie poznaje hasła ani pełnego skrótu (metoda k-anonimowości). Program wypisuje, ile razy hasło wyciekło.

**Użyte technologie:** API (moduł `requests`), haszowanie (moduł `hashlib`), kodowanie tekstu na bajty, przetwarzanie odpowiedzi z serwera, pętle

📁 [`Sprawdzacz wyciekow hasel/Sprawdzacz wyciekow hasel.py`](./Sprawdzacz%20wyciekow%20hasel/Sprawdzacz%20wyciekow%20hasel.py)

---

## O mnie

Uczę się Pythona z naciskiem na cyberbezpieczeństwo. Każdy projekt w tym repozytorium został napisany samodzielnie jako część nauki.
