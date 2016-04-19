'use strict';

function ImageStore(images) {
  this.currentIndex = 0;
  this.images = images;

  this.getCurrentSrc = function() {
    return this.images[this.currentIndex];
  }

  this.next = function() {
    this.jumpRelative(1);
  }

  this.prev = function() {
    this.jumpRelative(-1);
  }

  this.jumpRelative = function(step) {
    var length = this.images.length;
    this.currentIndex =
      (length + this.currentIndex + step) % length;
  }


}

module.exports = ImageStore;
