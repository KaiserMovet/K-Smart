## K-Smart  

# Opis

System służący do obsługi wszelkiego rodzaju czujników. Do systemu można dodać każdy czujnik, którego działanie polega na odbieraniu oraz wysyłaniu wiadomości/wartości.
Wartości wysyłane na dane czujniki mogą być określane przez użytkownika bądź zmieniane automatycznie na podstawie reguł zdefiniowanych przez użytkownika.

Docelowo cały system był tworzony z myślą o działaniu na NanoPi. NanoPi docelowo powinno mieć dwa interfejsy sieciowe w celu zmaksymalizowania bezpieczeństwa:
- lokalny, służący do kontaktu z czujnikami
- globalny, podłączany do sieci LAN, w której użytkownik może połączyć się z aplikacją webową, a samo NanoPi z internetem, np. w celu zaktualizowania programu

Cała aplikacja została rozbita na dwa moduły:
- engine, czyli część aplikacji obaługująca czujniki oraz przetwarzanie reguł
- app, czyli aplikacja webowa, która wprowadza zmiany do danych w części engine
Powyższe moduły komunikują się za pomocą połączenia klient-serwer. Ponadto możliwe jest napisanie innych modułów, które obsługiwałyby engine, np. aplikację rozpoznającą głosowe komenty użytkownika.

Ważne pliki:
- engine/save.p - plik zawierający dane zapisane przez engine.
- engine/data.txt - plik zawierający wszystkie aktualne dane, które posiada engine, odświeżany regularnie. 
- engine/debug.py - plik z funkcją Log(), edycja jej pozwala na zapis/wyświetlanie logów zgodnie z potrzebą użytkownika
- engine/connector.py - plik z funkcjami służącymi do kontaktu z czujnikami, może być edytowany zgodnie z potrzebą użytkownika

Ponadto moduł engine posiada wbudowaną opcję obsługującą kamery internetowe, za pomocą programu motion. 

# Uruchomienie
Na urządzeniu powinien być zainstalowany python3, motion oraz wymagane moduły do python3

W celu uruchomienia modułu engine, będąc w folderze engine/ należy użyc komend:
- sudo python3 main.py
W przypadku błędu przy uruchamianiu programu dotyczącego zajętych socketów, należy program przerwać za pomocą ctrl+c, zaczekać do zamknięcia, odczekać kilka sekund, oraz uruchomić ponownie.

W celu uruchomienia modułu app, będąc w folderze app/ należy użyć komend:
- export FLASK_APP = hello.py
- flask run --host=0.0.0.0

# Przykład użycia

1. Użytkownik chce podłączyć do systemu dwa czujniki, Czujnik światła oraz żarówkę, oraz wprowadzić regułę, żeby żarówka się zapalała, gdy wartość czujnika jest niższa niż 50, oraz gasła, gdy wartość tego czujnika jest większa lub równa 50
- Użytkownik wchodzi na aplikację webową, dodaje oba urządzenia, określając jego nazwę, opis, adres, interwał odświeżania, ip oraz to, czy jest odbiornikiem (w tym przypadku żarówka jest odbiornikiem, a czujnik nie)
- Użytkownik dodaje nową regułę Cond o wypranej przez siebie nazwie, opisie oraz interwale odświeżania.
- Użytkownik dodaje warunek, który chce sprawdzać, W tym celu tworzy nowy Condition, wybierając nazwę instniejącej reguły, wybraną nazwę warunku, pierwsze urządzenie (czyli Czujnik światła), z którego chce pobierać wartość (jego wartość ustawia na cokolwiek). Jako drugie urządzenie wybiera 'Value' i ustawia jego wartość na 50. Następnie wybiera metodę, którą chce porównywać obie wartości, w naszym przypadku wybieramy less
- Dodajemy effect, wybieramy nazwę reguły, wybraną nazwę efektu, obsługiwane urządzenie (w naszym wypadku żarówka), oraz wartość, jaką żarówka ma przyjmować, gdy warunek jest prawidziwy (w naszym wypadku 1) oraz gdy warunek jest fałszywy(0). Jeśli chcemy, żeby żadna wartość nie była wysyłana, wpisujemy "-1". Oba pola mogą przyjmować jakiekolwiek wartości, w tym stringi

Ponadto wartości urządzeń można zmieniać ręcznie, w zakłądce Devices. Nalezy jednak mieć na uwadzę, że jeżeli dane urządzenie jest zmieniane przez metodę, mogą one zostać nadpisane.

# Znane problemy
- Niedziałające usuwanie czujników oraz warunków
- Brak możliwości zapisu edycji efektów oraz warunków
