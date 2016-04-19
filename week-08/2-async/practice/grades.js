var grades = [3, 4, 5, 2, 3, 5, 2, 5];

function countFives(grades) {
  var count = 0;
  grades.forEach(function(grade) {
    if (grade === 5) {
      count++;
    }
  });
  return count;
}

console.log(countFives(grades)); // 3
