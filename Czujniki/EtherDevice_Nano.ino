/*
 * Autor: Cezary Wernik
 * Szczecin 2018 Polska 
 */
#include "EtherDevice.h"
static byte mac[] = {0x74, 0x69, 0x69, 0x2D, 0x30, 0x31 }; 
String secretKey = "7rHvCGd59C"; 
static const int argc=3;
arg argv[argc];
 

 
void setup()
{
  Serial.begin( 57600 );
  Serial.println( "Arduino ethernet device" );
  while( eth.init( mac, SS ) != 0 );
  eth.ipconfig();
  pinMode(2, OUTPUT);
  pinMode(3, OUTPUT);
  pinMode(4, OUTPUT);
  pinMode(5, OUTPUT);
  pinMode(6, OUTPUT);
  pinMode(7, OUTPUT);
  pinMode(8, OUTPUT);
  pinMode(9, OUTPUT);
}
 
void loop()
{

 
  int c = eth.getTask(argc, argv);  
  if(c>=0)
  {
    if(eth.checkArg(c, argv, "secretKey", secretKey)==0)
    {
      if(eth.checkArg(c, argv, "cmd", "turnlighton")==0)
      {
        String seq = eth.getArg(c, argv, "seq");
        digitalWrite(9, seq[0]&1);
        digitalWrite(8, seq[1]&1);
        digitalWrite(7, seq[2]&1);
        digitalWrite(6, seq[3]&1);
        digitalWrite(5, seq[4]&1);
        digitalWrite(4, seq[5]&1);
        digitalWrite(3, seq[6]&1);
        digitalWrite(2, seq[7]&1);
      }
 
      if(eth.checkArg(c, argv, "cmd", "turnlightoff")==0){
        digitalWrite(9, 0);
        digitalWrite(8, 0);
        digitalWrite(7, 0);
        digitalWrite(6, 0);
        digitalWrite(5, 0);
        digitalWrite(4, 0);
        digitalWrite(3, 0);
        digitalWrite(2, 0);
      }
      
 
      eth.httpServerReply(eth.webPage());
    }else{
      eth.staticHttpServerReply(HTTP401);
    }
  }
}
 
word EtherDevice::webPage()
{
  bfill = tcpOffset();
  bfill.emit_p(
    PSTR(
      "$F"
      "$D" 
      "$D" 
      "$D" 
      "$D"
      "$D" 
      "$D"
      "$D" 
      "$D"
    ),
    HTTP200,
    digitalRead(9),
    digitalRead(8),
    digitalRead(7),
    digitalRead(6),
    digitalRead(5),
    digitalRead(4),
    digitalRead(3),
    digitalRead(2)
  );
  return bfill.position();
}
