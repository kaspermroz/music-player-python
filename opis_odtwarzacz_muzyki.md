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

Opłata za słuchanie muzyki:
  - Zakładamy, że dla każdego utworu koszt jego odtworzenia będzie wartością losową z zakresu od 10 gr do 4,00zł ( koszt wyznaczany z dokładnością do 1 grosza). 
  - Przy czym im utwór "nowszy" tym koszt odtworzenia większy - można użyć metody random.triangular.
  - Utwory ładowane z dysku mają koszt równy 50% kosztu podstawowego.
  - Ponowne odtworzenie utworu w ramach tej samej playlisty - koszt zmniejszony o 25% kosztu początkowego.
  - Opłata jest naliczana w momencie rozpoczęcia odtwarzania utworu.
  - Jeżeli playlista została przerwana naliczana jest tylko opłata za utwory, które się zakończyły i ostatnio rozpoczęty. Za utwory nieodsłuchane opłata stała wyniesie 10% ich wartości.
  - Płatność za odsłuchanie monetami 10gr, 20gr, 50gr, 1zł, 2zł, 5zł.
  - Odtwarzacz zwraca resztę przy użyciu monet 1gr, 2gr, 5gr, 10gr, 20gr, 50gr, 1zł, 2zł, 5zł
 
Istnieje możliwość odsłuchania muzyki w dwóch wariantach:
  - przedpłata - najpierw wpłacamy pieniądze - tworzymy playlistę do limitu wynikającego z przedpłaty
  - kredyt - tworzymy playlistę - płacimy potem

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
 6. Opłata za słuchanie muzyki
  	 - poprawnie przeliczanie kosztu odtwarzania piosenek
  	 	- przedpłata - odejmowanie wartości piosenek od opłaconej kwoty
  	 	- kredyt - naliczanie kredytu za każdym odtworzeniem
  	 - wydawanie reszty po zakończeniu słuchania 
  	 - przerwanie słuchania muzyki w trakcie odtwarzania - przeliczenie kosztówn według wymagań
