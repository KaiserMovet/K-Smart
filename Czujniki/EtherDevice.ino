/*
 * Autor: Cezary Wernik
 * Szczecin 2018 Polska 
 */
#include "EtherDevice.h"
static byte mac[] = {0x74, 0x69, 0x69, 0x2D, 0x30, 0x31 }; 
String secretKey = "7rHvCGd59C"; 
static const int argc=3;
arg argv[argc];

int pwm_wentylatora = 0;

void setup()
{
  Serial.begin( 57600 );
  Serial.println( "Arduino ethernet device" );
  while( eth.init( mac, SS ) != 0 );
  eth.ipconfig();
}

void loop()
{
  analogWrite(9,pwm_wentylatora); 
  int c = eth.getTask(argc, argv);  
  if(c>=0)
  {
    if(eth.checkArg(c, argv, "secretKey", secretKey)==0)
    {
      if(eth.checkArg(c, argv, "cmd", "changepwm")==0)
      {
        String pwm = eth.getArg(c, argv, "pwm");
        if(pwm.length()>0)
        {
          if(pwm.toInt()>=0 && pwm.toInt()<=255)
            pwm_wentylatora = pwm.toInt(); 
        }
      }

      if(eth.checkArg(c, argv, "cmd", "resetpwm")==0)
        pwm_wentylatora = 0;

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
    ),
    HTTP200,
    (pwm_wentylatora!=0)
  );
  return bfill.position();
}
