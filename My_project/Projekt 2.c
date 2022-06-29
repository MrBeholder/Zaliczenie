// tablica ze zmienną pin do której podłączone są diody LED (użyte w pętli)
int pin[] = {5,6,7,8,9};

const int analogInPin = A0;  // pin wejścia analogowego do którego podłączony jest potencjometr

// stałe przechowujące zmienne odnoszące się do pinów diod LED
const int analogOutPin1 = 9; 
const int analogOutPin2 = 8;
const int analogOutPin3 = 7;
const int analogOutPin4 = 6;
const int analogOutPin5 = 5; 

// zmienne dla wartości wyjściowych i wejściowych (wartość początkowa 0)
// wartości wyjściowe - potencjometr (konsola)
int sensorValue = 0;  

// wartości wyjściowe - diody LED
int outputValue1 = 0;       
int outputValue2 = 0;
int outputValue3 = 0; 
int outputValue4 = 0; 
int outputValue5 = 0;

// wartości wejściowe (konsola)
int outputValue = 0;        

void setup() {
  // Serial.begin(9600) - pozwala na wyświetlanie danych w konsoli (sensor i output)
  Serial.begin(9600);
  // pętla - wartości przyjmujemy od 0-4 (tyle ile diod)
  // zastosowanie inkrementacji, ponieważ chcemy by diody się zapalały
  for(int i=0; i<=4; i++){
   analogWrite(pin[i], 255);
    delay(500);
  }
  // sytuacja analogiczna, ale by diody zaczęły się wyłączać stosujemy inkrementację
  for(int i=4; i>=0; i--){
   analogWrite(pin[i], 0); 
    delay(500);
  }
}

void loop() {
  // przyjmuje wartości przypisane z potencjometra
  sensorValue = analogRead(analogInPin);
  // tutaj przypisujemy to co wyślemy do dody LED (dioda zakres 0-255)
  // potencjometr (0-1023)
  // funkcja map() mapuje zakresy, a więc przyjmuje zakresy z 0-1023 na 0-255
  outputValue = map(sensorValue, 0, 1023, 0, 255);

  analogWrite(analogOutPin1, outputValue);
  analogWrite(analogOutPin2, outputValue);
  analogWrite(analogOutPin3, outputValue);
  analogWrite(analogOutPin4, outputValue);
  analogWrite(analogOutPin5, outputValue);

  // opis generowany w konsoli sensor/output sensorValue/outputValue
  Serial.print("sensor = ");

  Serial.print(sensorValue);

  Serial.print("\t output = ");

  Serial.println(outputValue);

  // opóźnienie
  delay(2);
}