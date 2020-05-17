
#include <WiFi.h>
#include <DHT.h>
#include <Adafruit_GFX.h>
#include <Adafruit_PCD8544.h>
#define DHTPIN 18
#define DHTTYPE DHT11

DHT dht(DHTPIN, DHTTYPE);

//inicio display nokia
const int reset = 2;
const int sce = 4;
const int dc = 5;
const int sdin = 19;
const int lk = 21;
Adafruit_PCD8544 display = Adafruit_PCD8544 (lk,sdin,dc ,sce,reset);


//-------------------VARIABLES GLOBALES--------------------------
int contconexion = 0;

const char *ssid = "DIEGO_GOMEZ";
const char *password = "Diego2020";

unsigned long previousMillis = 0;

const char* server = "api.thingspeak.com";
String apiKey ="QCRF5N9SBDU1ZKMN";

//----Función para Enviar Datos a Thingspeak----

void enviarTempTS(float temp)
{  
   WiFiClient client;
  
   if (client.connect(server, 80)) { // usar 184.106.153.149 ó api.thingspeak.com
   Serial.println("WiFi Client connected ");
   
   String postStr = apiKey;
   postStr += "&field1=";
   postStr += String(temp);
   postStr += "\r\n\r\n";
   
   client.print("POST /update HTTP/1.1\n");
   client.print("Host: api.thingspeak.com\n");
   client.print("Connection: close\n");
   client.print("X-THINGSPEAKAPIKEY: " + apiKey + "\n");
   client.print("Content-Type: application/x-www-form-urlencoded\n");
   client.print("Content-Length: ");
   client.print(postStr.length());
   client.print("\n\n");
   client.print(postStr);
   delay(1000);
   
   }
 client.stop();
}

//-------------------------------------------------------------------------

void setup() {

  
  // Inicia Serial
  Serial.begin(115200);
  dht.begin();
  Serial.println("");
  //pinMode(2, OUTPUT);
  //-----DISPLAY------
  display.begin();
  display.setContrast(50);
  display.clearDisplay();
  display.display();  


  // Conexión WIFI
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED and contconexion <50) { //Cuenta hasta 50 si no se puede conectar lo cancela
    ++contconexion;
    delay(500);
    Serial.print(".");
  }
  if (contconexion <200) {
      Serial.println("");
      //digitalWrite(2, HIGH);
      Serial.println("WiFi CONECTADO");
      display.setTextSize(1);//-------DISPLAY------
      display.setCursor(0,0);
      display.print("WiFi conectado");
      display.setTextSize(1);//-------DIRECCION IP------
      display.setCursor(11,10);
      display.print(WiFi.localIP());
      display.setCursor(0,25);
      display.display();
      
     
      
  }
  else { 
      Serial.println("");
      Serial.println("Error de conexion");
  }
}

//--------------------------LOOP--------------------------------
void loop() {


  unsigned long currentMillis = millis();

    if (currentMillis - previousMillis >= 600000) { //envia la temperatura cada 5 segundos
    previousMillis = currentMillis;
    float t = dht.readTemperature();
    float cal = t-3;
    enviarTempTS(cal);
    Serial.print(t);
    Serial.println(cal);
    display.setCursor(0,0);
    display.print("WiFi conectado");
    display.setTextSize(1);//-------DIRECCION IP------
    display.setCursor(11,10);
    display.print(WiFi.localIP());
    display.setCursor(10,20);
    display.print("Temperatura");
    display.setTextSize(1);
    display.setCursor(30,35);
    display.print(cal);
    display.display();
    display.clearDisplay();
     
    
  }
}
