'use strict';

function Student() {
  this.grades = {};

  this.addGrade = function(subject, grade) {
  //  if (this.grades[subject] === undefined) {
  if (!(subject in this.grades)) {
      this.grades[subject] = [];
    }
    this.grades[subject].push(grade);
  };

  this.getCount = function() {
    var output = {};
    for (var subject in this.grades) {
      output[subject] = this.grades[subject].length;
    }
    return output;
  };

  this.getAverage = function() {
    var sum = 0;
    var count = 0;
    for (var subject in this.grades) {
      this.grades[subject].forEach(function(grade) {
        sum += grade;
        count += 1;
      });
    }
    return sum / count;
  };
}

var dezso = new Student();
dezso.addGrade('matek', 5);
dezso.addGrade('matek', 4);
dezso.addGrade('matek', 4);
dezso.addGrade('rajz', 1);
dezso.addGrade('rajz', 3);
dezso.addGrade('magyar', 4);
console.log(dezso.getCount()) // {'rajz': 2, matek: 3}
console.log(dezso.getAverage()) // 3.4
// szorgalmi
//dezso.getAverageBySubject() // {'matek': 4.3, 'rajz': 2}
