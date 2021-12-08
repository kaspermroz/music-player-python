# Odtwarzacz muzyki

## Opis projektu

### Wymagania
Celem projektu będzie stworzenie klienta odtwarzacza muzyki w Pythonie. Klient posiada interfejs wiersza poleceń (CLI) oraz oparty na nim interfejs graficzny (GUI).  Odtwarzacz będzie posiadać dwa tryby (adaptery):
 - tryb odtwarzania muzyki z dysku, możliwość przeszukania systemu celem zlokalizowania plików .mp3
 - tryb streamowania - w tym celu wykorzystany jeden z najpopularniejszych streamingów muzyki - Spotify

Niezależnie od wybranego trybu, użytkownik może:
 - dodawać i usuwać utwory do swojej biblioteki
 - tworzyć playlisty w obrębie biblioteki
 - przy odtwarzaniu playlisty użytkownik może zapętlić konkretny otwór oraz całą playlistę
 
 W trybie streamingu użytkownik dodatkowo może:
  - zalogować się do streamingu za pomocą istniejącego konta
  - przeszukiwać bibliotekę streamingu i odtwarzać pojedyncze utwory
  

### Metodologia
Całość projektu jest zaimplementowania w duchu Clean Architecture, z wykorzystaniem DDD (Domain Driven Design). Reguły biznesowe aplikacji znajdują się w centrum grafu zależności, definiują pozostałe warstwy (porty, adaptery).

## Testy
 1.  Wyszukiwanie plików w systemie po danej ścieżce
	  - znalezione testowe pliki .mp3
	  - pusta lista plików
 2.  Dodawanie i usuwanie plików z biblioteki
	 - dodanie istniejącego pliku - sukces
	 - dodanie nieistniejącego pliku - błąd
	 - dodanie uszkodzonego pliku - błąd
	 - usunięcie istniejącego pliku z biblioteki - sukces
	 - usunięcie pliku, który nie znajduje się w bibliotece - błąd
 3. Tworzenie playlist z biblioteki
	 - stworzenie playlisty z utworów znajdujących się w bibliotece - sukces
	 - stworzenie playlisty z utworami spoza biblioteki - błąd
	 - usunięcie istniejącej playlisty - sukces
	 - usunięcie nieistniejącej playlisty - błąd
 4. Odtwarzanie muzyki:
	 - odtwarzanie utworów lokalnie
	 - odtwarzanie utworów ze streamingu
 5. Interfejs graficzny, poprawne wyświetlanie informacji
	 - odtwarzany utwór - autor, tytuł długość, głośność, długość
	 - playlista
	 - przyciski do sterowania odtwarzaczem

