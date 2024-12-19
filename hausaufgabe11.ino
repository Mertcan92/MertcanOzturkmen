#include <Servo.h>

// C++ code
//
#include <Servo.h>

int distanz = 0;

long readUltrasonicDistance(int triggerPin, int echoPin)
{
  pinMode(triggerPin, OUTPUT);  // Clear the trigger
  digitalWrite(triggerPin, LOW);
  delayMicroseconds(2);
  // Sets the trigger pin to HIGH state for 10 microseconds
  digitalWrite(triggerPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(triggerPin, LOW);
  pinMode(echoPin, INPUT);
  // Reads the echo pin, and returns the sound wave travel time in microseconds
  return pulseIn(echoPin, HIGH);
}

Servo servo_2;

void setup()
{
  servo_2.attach(2, 500, 2500);
}

void loop()
{
  distanz = 0.01723 * readUltrasonicDistance(A0, A1);
  if (distanz <= 10) {
    servo_2.write(45);
  }
  delay(3000); // Wait for 3000 millisecond(s)
  if (distanz > 10) {
    servo_2.write(9);
  }
}