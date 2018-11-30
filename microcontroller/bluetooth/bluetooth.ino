/*
  Example Bluetooth Serial Passthrough Sketch
 by: Jim Lindblom
 SparkFun Electronics
 date: February 26, 2013
 license: Public domain

 This example sketch converts an RN-42 bluetooth module to
 communicate at 9600 bps (from 115200), and passes any serial
 data between Serial Monitor and bluetooth module.
 */
#include <SoftwareSerial.h>  

#define I 0
#define R 1
#define RS 2
#define RSS 3

int bluetoothTx = 2;  // TX-O pin of bluetooth mate, Arduino D2
int bluetoothRx = 3;  // RX-I pin of bluetooth mate, Arduino D3

const char* states[4] = {"I", "R", "RS", "RSS"};


SoftwareSerial bluetooth(bluetoothTx, bluetoothRx);

void setup()
{
  Serial.begin(9600);
  delay(1000);
  bluetooth.begin(115200);  // The Bluetooth Mate defaults to 115200bps
  bluetooth.print("$");  // Print three times individually
  bluetooth.print("$");
  bluetooth.print("$");  // Enter command mode
  delay(100);  // Short delay, wait for the Mate to send back CMD
  bluetooth.println("U,9600,N");  // Temporarily Change the baudrate to 9600, no parity
  // 115200 can be too fast at times for NewSoftSerial to relay the data reliably
  bluetooth.begin(9600);  // Start bluetooth serial at 9600
}

int getrssi(int index)
{
  if (index > 4) return -1;
  return analogRead(index);
}

int state = I;
int prev = 0;
void loop()
{
  char c = 0;
  if(!bluetooth.available()) return;
  c = (char)bluetooth.read();
  
  Serial.print("Received: "); Serial.println(c);
  Serial.print("Current state: "); Serial.println(states[state]);
  
// fsm

  switch(state)
  {
    case I:
      if (c == 'R') state = R;
      break;

     case R:
      if (c == 'S') state = RS;
      else state = I;
      break;

     case RS:
      if (c == 'S')
      {
        state = RSS;
        bluetooth.print("[");
      }
      else state = I;
      break;

      case RSS:
        if (c < '0' || c > '4')
        {
          bluetooth.print("]\r\n");
          prev = 0;
          if (c == 'R') state = R;
          else state = I;
        }
        else
        {
          if (prev) bluetooth.print(",");
          bluetooth.print(getrssi(c - '0'), DEC);
          Serial.print(getrssi(c - '0'), DEC);
          prev = 1;
        }
        break;

      default:
        break;
      
  }
}
