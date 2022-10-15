#include <Wire.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_HMC5883_U.h>


// defining shit we need
const int trigPin = 9;
const int echoPin = 10;
long duration;
int distance;
int sendo =0;

char message[6];

float other;
int start;
int start2;
int start3;
float other2;

int right = 2;
int left = 4;
int ENB = 7;
int ENA = 6;

int finding =0;
int idk = 0;

int done =8;

Adafruit_HMC5883_Unified mag = Adafruit_HMC5883_Unified(12345);

//showing mag sensors if we want to 
void displaySensorDetails(void)
{
  sensor_t sensor;
  mag.getSensor(&sensor);
  delay(500);
}

void setup() {

  //starting communications
  Serial.begin(9600); // opens serial port, sets data rate to 9600 bps
  //Serial.println("HMC5883 Magnetometer Test"); Serial.println("");
  
  /* Initialise the sensor */
  if(!mag.begin())
  {
    /* There was a problem detecting the HMC5883 ... check your connections */
    Serial.println("Ooops, no HMC5883 detected ... Check your wiring!");
    while(1);
  }

  pinMode(trigPin, OUTPUT); // Sets the trigPin as an Output
  pinMode(echoPin, INPUT); // Sets the echoPin as an Input

  
  pinMode(right, OUTPUT);
  pinMode(left, OUTPUT);

  digitalWrite(ENA,  HIGH);
  digitalWrite(ENB, HIGH);
  digitalWrite(left, LOW);
  digitalWrite(right, LOW);

  int finding =0;
  int sendo = 0;
  int done =8;
  
  /* Display some basic information on this sensor */
  //displaySensorDetails();
}


//if hit send variable back to start the voiceline
  void hit(){
    //Serial.println(distance);
    //Serial.print("hit"); 
    done = 8;
    //stop robot
    //digitalWrite(right, LOW);
    //digitalWrite(left, LOW);
    //Serial.print('Q');
    while(done==8){
    Serial.print(done);
    }
   // Serial.print(distance);
    //Serial.print("did it");
  }


//using this as recursion instead of a loop to save the variable "other" from the mag sensor
void redo(){
  while(sendo !=2){
  if(finding == 0){
     digitalWrite(right, HIGH);
     //Serial.print("success");
  }
  
  //Serial.print(other);
  sensors_event_t event; 
  mag.getEvent(&event);
  /* Display the results (magnetic vector values are in micro-Tesla (uT)) */
  //Serial.print("X: "); Serial.print(event.magnetic.x); Serial.print("  ");
  //Serial.print("Y: "); Serial.print(Ser\\event.magnetic.y); Serial.print("  ");
  //Serial.print("Z: "); Serial.print(event.magnetic.z); Serial.print("  ");Serial.println("uT");
  
  float heading = atan2(event.magnetic.y, event.magnetic.x);
  float declinationAngle = 0.22;
  heading += declinationAngle;


  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  // Sets the trigPin on HIGH state for 10 micro seconds
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  // Reads the echoPin, returns the sound wave travel time in microseconds
  duration = pulseIn(echoPin, HIGH);
  // Calculating the distance
  distance = duration * 0.034 / 2;
  // Prints the distance on the Serial Monitor
  //Serial.print(distance);

  
  // Correct for when signs are reversed.
  if(heading < 0)
    heading += 2*PI;
    
  // Check for wrap due to addition of declination.
  if(heading > 2*PI)
    heading -= 2*PI;
   
  // Convert radians to degrees for readability.
  float headingDegrees = heading * 180/M_PI; 
  //Serial.print(headingDegrees);
  if(headingDegrees > other + 15 and other < 345 and other >15){
    //stop turning right
    digitalWrite(right, LOW);
    //start turning left
    digitalWrite(left, HIGH);
    //Serial.print("Too Far right");
  }
  if(headingDegrees < other - 15 and other < 345 and other >15){
    //stop turning right
    digitalWrite(left, LOW);
    //start turning left
    digitalWrite(right, HIGH);
  //  Serial.print("Too Far left");
  }

  if(other > 345 or other < 15){
    digitalWrite(left,HIGH);
    digitalWrite(right,HIGH);
  }

    if(headingDegrees < other + 15 and headingDegrees > other - 15 and other < 345 and other >15){
   // Serial.print("You're in range");
     //start going straight
    digitalWrite(right, HIGH);
    digitalWrite(left, HIGH);
  }

    //Serial.print(distance);
   //if the robot actually runs into something
    if(distance <=3){
    Serial.print(distance);
    digitalWrite(right, LOW);
    digitalWrite(left, LOW);
    sendo = 2;
    idk = 0;
    //exit(0);
    }
    
  //Serial.print("Heading (degrees): "); Serial.println(headingDegrees);
  //delay(100);
  finding++;
  //Serial.print(finding);
  //Serial.print(other);
//  redo();
}
}

void loop() {
  
  if (Serial.available() > 0) { 
    //Serial.print("testing");
    other = Serial.parseFloat();
    other2 = other;
    //Serial.print(other);  
    //Serial.print(other2);
    //digitalWrite(right, HIGH);
  }

if(other != 0){
redo();  
}
}
