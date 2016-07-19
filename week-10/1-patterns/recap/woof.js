// var dog = function () {
//   var sound = "woof";
//   return {
//     talk: function () {
//       console.log(sound);
//     }
//   };
// };
//
// var zsele = dog();
// zsele.talk();

// var dog = (function () {
//   var sound = "woof";
//   return {
//     talk: function () {
//       console.log(sound);
//     }
//   };
// })();
//
// dog.talk();
//

var dog = (function () {
  var sound = "woof";

  function publicTalk () {
    console.log(sound);
  }

  return {
    talk: publicTalk
  };
})();

dog.talk();


//
// var Dog = function () {
//   this.sound = "woof";
// };
//
// Dog.prototype.talk = function () {
//   console.log(this.sound);
// };
//
// var zsele = new Dog();
// zsele.talk();
