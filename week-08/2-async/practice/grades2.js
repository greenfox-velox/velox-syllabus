var grades = [
  {num: 3, subject: 'math'},
  {num: 4, subject: 'math'},
  {num: 5, subject: 'arts'},
  {num: 2, subject: 'sport'},
  {num: 5, subject: 'physics'},
  {num: 4, subject: 'physics'}
];


function countFives(grades) {
  var count = 0;
  grades.forEach(function(grade) {
    if (grade.num === 5) {
      count++;
    }
  });
  return count;
}


console.log(countFives(grades)); // 2

