
function Student(kg, name) {
  this.kg = kg;
  this.name = name;
  this.toys = []; 
}


Student.prototype.addToy = function(toy) {
  this.toys.push(toy);
  return this;
}

Student.prototype.showOfWithToys = function() {
  this.toys.forEach(function(toy) {
    console.log('He-Hee-Heee! I have a: ' + toy);
  });
  return this;
}

var akos = new Student(56, 'Akos');
akos
  .addToy('Lego set 8880')
  .addToy('Matchbox Ferrari F40')
  .showOfWithToys()
  .addToy('Scrabble')
  .showOfWithToys();





function Student(kg, name) {
  var student;
  var toys = [];

  function addToy(t) {
    toys.push(t);
    return student;
  }

  student = {
    kg: kg,
    name: name,
    addToy: addToy
  }
  return student;
}









