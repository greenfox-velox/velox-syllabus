'use strict';


var student = {
  age: 10,
  sayYourAge: sayYourAge
};

function sayYourAge() {
  console.log('I am ' + this.age);
}

student.sayYourAge();
