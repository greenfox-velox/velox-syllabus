var GreeterConstructor = function () {
  this.name = "Ben Cherry";
  this.greet = "Hey there!";
};

ConstructorFunction.prototype._getName = function () {
  console.log( "Name:" + this.name );
};

ConstructorFunction.prototype.setName = function ( strName ) {
  this.name = strName;
}

ConstructorFunction.prototype.getName = function () {
  this._getName();
}

myGreeter = new GreeterConstructor();
myGreeter.setName( "Paul Kinlan" );
