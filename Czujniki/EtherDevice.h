/*
 * Autor: Cezary Wernik
 * Szczecin 2018 Polska 
 */
#ifndef EtherDevice_h
#define EtherDevice_h

#include <EtherCard.h>
byte Ethernet::buffer[500]; // tcp/ip buffer
BufferFiller bfill;

const char HTTP200[] PROGMEM =
"HTTP/1.1 200 OK\r\n"
"Server: Arduino Ethernet Devices\r\n"
"Cache-Control: no-store\r\n"
"Connection: Keep-Alive\r\n"
"Content-Type: text/html; charset=utf-8\r\n\r\n";

const char HTTP401[] PROGMEM =
"HTTP/1.0 401 Unauthorized\r\n"
"Content-Type: text/html\r\n\r\n"
"<h1>401 Unauthorized</h1>";

const char HTTP404[] PROGMEM =
"HTTP/1.0 404 Not Found\r\n"
"Content-Type: text/html\r\n\r\n"
"<h1>404 Not Found</h1>";

const char HTTP405[] PROGMEM =
"HTTP/1.0 405 Method Not Allowed\r\n"
"Content-Type: text/html\r\n\r\n"
"<h1>405 Method Not Allowed</h1>";

const char HTTP406[] PROGMEM =
"HTTP/1.0 406 Not Acceptable\r\n"
"Content-Type: text/html\r\n\r\n"
"<h1>406 Not Acceptable</h1>";

// Struktura przechowywania argumentów żądania
struct arg
{
  String argName;
  String argValue;
};

class EtherDevice : public EtherCard
{
  public:
    //DHCP IP init
    // mac - MAC adres urządzenia
    // slaveSelect - określa pin dla chip select układu gdy płyta Arduino inna niż UNO 
    int init(byte mac[], int slaveSelect)
    {
      if (begin(sizeof Ethernet::buffer, mac, slaveSelect) == 0)
        return 1;//Failed to access Ethernet controller
    
      if (!dhcpSetup())
        return 2;//DHCP failed
    
      return 0;
    }

    //STATIC IP init
    // mac - MAC adres urządzenia 
    // myip - adres IP, wymaga dodania w sketch-u:
    //        static byte myip[] = { 192,168,1,200 };
    // gateway - adres bramy domyślnej, wymaga dodania w sketch-u:
    //        static byte gwip[] = { 192,168,1,1 };
    // slaveSelect - określa pin dla chip select układu gdy płyta Arduino inna niż UNO
    int init(byte mac[], byte ip[], byte gateway[], int slaveSelect)
    {
      if (begin(sizeof Ethernet::buffer, mac, slaveSelect) == 0)
        return 1;//Failed to access Ethernet controller

      staticSetup(ip, gateway);
      return 0;
    } 

    // Wypisuje poprzez Serial konfigurację IP urządzenia
    void ipconfig()
    {
      printIp("IP:  ", ether.myip);
      printIp("GW:  ", ether.gwip);  
      printIp("DNS: ", ether.dnsip); 
    }
    
    // Wysyła statycznie zdefiniowaną odpowiedź na żądanie HTTP 
    // mem - stały zdefiniowany łańcuch
    void staticHttpServerReply(const char mem[])
    {
      bfill = tcpOffset();
      bfill.emit_p(mem);
      httpServerReply(bfill.position());
    }

    // Wypisuje w Serial wszystkie argumenty przychodzące
    // argc - aktualna liczba argumentów 
    // argv wskaźnik tablicy struktur argumentów
    void printArg(int argc, arg argv[])
    {
      for(int i=0;i<argc;i++)
      {
        Serial.print("[");
        Serial.print(argv[i].argName);
        Serial.print(" = ");
        Serial.print(argv[i].argValue);
        Serial.println("]");
      }
    }

    // Zwraca wartość argumentu o nazwie argName jeżeli istnieje 
    // argc - aktualna liczba argumentów 
    // argv wskaźnik tablicy struktur argumentów
    String getArg(int argc, arg argv[], String argName)
    {
      argName.trim();
      for(int i=0;i<argc;i++)
      {
        argv[i].argName.trim();                      
        if(argv[i].argName.compareTo(argName)==0)
        {
          argv[i].argValue.trim();
          return argv[i].argValue;
        }
      }
      return "";
    }

    // Sprawdza czy argument o podanej nazwie argName zawiera argValue
    // argc - aktualna liczba argumentów 
    // argv wskaźnik tablicy struktur argumentów
    int checkArg(int argc, arg argv[], String argName, String argValue)
    {
      argName.trim();
      argValue.trim();
      if(getArg(argc, argv, argName).compareTo(argValue)==0)
      {
        return 0;
      }
      return 1;
    }

    // Zwraca liczbę argumentów przychodzących w żądaniu HTTP
    // i zapisuje argumenty pod wskaźnikiem argv
    // argc - dopuszczalna liczba argumentów
    // argv wskaźnik tablicy struktur argumentów
    int getTask(int argc, arg argv[])
    {
      word offset = packetLoop(packetReceive());
      if ( offset ) 
      {
        char *request = (char *) Ethernet::buffer + offset;
        if (strncmp("GET /", request, 5) != 0) 
        {   
          // 405 Unsupported HTTP request
          staticHttpServerReply(HTTP405);
          return -1;
        } else {
          request += 5;
          if (request[0] == ' ') 
          { 
            //Jeżeli nie ma żadnych argumentów
            for(int idx=0; idx<argc; idx++)
            {
              argv[idx].argName = "";
              argv[idx].argValue = "";
            }
            return 0;
          } else {
            if (!strncmp("?",request,1))
            { 
              //Wycinanie rządania od znaku "?" + 1, żeby tego znaku "?" nie było w ciągu,
              //do znaku " " o indeksie endIdx.
              int endIdx = strcspn (request," ");
              request += strcspn (request,"?") + 1;

              int idx = 0;
              int args_valid = 0;
              int args_cnt = 0;
          
              for( idx=0; idx<endIdx; idx++ )
              {
                if(request[idx]=='&')
                  args_cnt++;
                if(request[idx]=='=')
                  args_valid++;
              }

              if( (args_valid == (args_cnt+1)) && (args_valid<=argc) )
              { 
                for( idx=0; idx<argc; idx++)
                {
                  argv[idx].argName = "";
                  argv[idx].argValue = "";
                }

                idx=0;
                bool tictac=0;
                for( int c=0; c<endIdx; c++ )
                {
                  if( tictac == 0)
                  {
                    if( request[c] == '=')
                    {
                      tictac=!tictac;
                    }else{
                      argv[idx].argName += request[c];  
                    }
                  }else{
                    if( request[c] == '&')
                    {
                      tictac=!tictac;
                      idx++;
                    }else{
                      argv[idx].argValue += request[c];
                    }
                  }
                }
                return args_cnt+1;
              }else{
                // 406 Not Acceptable
                staticHttpServerReply(HTTP406);
                return -3;
              }
            } else {
              // 404 Page not found
              staticHttpServerReply(HTTP404);
              return -2;
            }
          }
        }
      } else {
        return -1;
      }
    }

    // Służy wygenerowaniu odpowiedzi na żądanie HTTP  
    // Definicja musi być w pliku .ino (w sketch-u) jako:
    // word EtherDevice::webPage()
    // {
    //   // Ustawia offset w BufferFiller
    //   bfill = tcpOffset();
    //
    //   // Wewnątrz PSTR(...) możesz używać następujących typów:
    //   //  $D = word data type
    //   //  $L = long data type
    //   //  $S = c string
    //   //  $F = progmem string
    //   //  $E = byte from the eeprom
    //   bfill.emit_p(
    //     PSTR(
    //       "$F"// Tego $F nie zmieniaj i nie usuwaj - to nagłówek odpowiedzi HTTP OK
    //       " jakiś tekst html $D jakiś tekst html " 
    //       " jakiś tekst html $D jakiś tekst html" 
    //       "..."
    //       ...
    //     ),
    //     HTTP200,// Tego HTTP200 nie zmieniaj i nie usuwaj - to nagłówek odpowiedzi HTTP OK
    //     ..., // potrzebne zmienne
    //     ...
    //   );
    //
    //  // Zwraca aktualny offset BufferFiller
    //  return bfill.position();
    // }
    word webPage();
};

extern EtherDevice eth;

#endif
