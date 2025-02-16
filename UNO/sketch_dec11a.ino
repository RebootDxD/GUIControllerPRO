//Реле на ПРЭМ
#define PREM_4 13
#define PREM_3 12
#define PREM_2 11
#define PREM_1 10
//Реле на Питерфлоу РС
#define PC_4 6
#define PC_3 7
#define PC_2 8
#define PC_1 9

void setup() {
  //Реле на ПРЭМ
  pinMode(PREM_4, 1);
  pinMode(PREM_3, 1);
  pinMode(PREM_2, 1);
  pinMode(PREM_1, 1);
  //Реле на Питерфлоу РС
  pinMode(PC_4, 1);
  pinMode(PC_3, 1);
  pinMode(PC_2, 1);
  pinMode(PC_1, 1);

  Serial.begin(115200);

}

void loop() {
    if (Serial.available() > 0){
      int dataIn = Serial.parseInt();
      if (dataIn <= 5){
        switch (dataIn){
        case 0: //sf
          Serial.println("#1.29");          
          break;
        case 1: //10
          digitalWrite(PREM_1, 0);
          digitalWrite(PREM_2, 0);
          digitalWrite(PREM_3, 0);
          digitalWrite(PREM_4, 0);
          Serial.println(dataIn);
          break;
        case 2: //8
          digitalWrite(PREM_1, 1);
          digitalWrite(PREM_2, 1);
          digitalWrite(PREM_3, 1);
          digitalWrite(PREM_4, 0);
          Serial.println(dataIn);
          break;
        case 3:
          digitalWrite(PREM_1, 1);
          digitalWrite(PREM_2, 1);
          digitalWrite(PREM_3, 0);
          digitalWrite(PREM_4, 0);
          Serial.println(dataIn);
          break;
        case 4:
          digitalWrite(PREM_1, 1);
          digitalWrite(PREM_2, 0);
          digitalWrite(PREM_3, 0);
          digitalWrite(PREM_4, 1);
          Serial.println(dataIn);
          break;
        case 5:
          digitalWrite(PREM_1, 1);
          digitalWrite(PREM_2, 0);
          digitalWrite(PREM_3, 0);
          digitalWrite(PREM_4, 0);
          Serial.println(dataIn);
          break;
        }
      }else if (dataIn >= 6){
        switch (dataIn){
        case 6:
          digitalWrite(PC_1, 0);
          digitalWrite(PC_2, 0);
          digitalWrite(PC_3, 0);
          digitalWrite(PC_4, 0);
          Serial.println(dataIn);
          break;
        case 7:
          digitalWrite(PC_1, 1);
          digitalWrite(PC_2, 1);
          digitalWrite(PC_3, 1);
          digitalWrite(PC_4, 0);
          Serial.println(dataIn);
          break;
        case 8:
          digitalWrite(PC_1, 1);
          digitalWrite(PC_2, 1);
          digitalWrite(PC_3, 0);
          digitalWrite(PC_4, 0);
          Serial.println(dataIn);
          break;
        case 9:
          digitalWrite(PC_1, 1);
          digitalWrite(PC_2, 0);
          digitalWrite(PC_3, 0);
          digitalWrite(PC_4, 1);
          Serial.println(dataIn);
          break;
        case 10:
          digitalWrite(PC_1, 1);
          digitalWrite(PC_2, 0);
          digitalWrite(PC_3, 0);
          digitalWrite(PC_4, 0);
          Serial.println(dataIn);
          break;
      
        }
      }
    }
      
}
 
// 2 4   прэм
// 1 3 5

// 1 5 
// 2 3 4 плата
