'use strict';

function ImageStorage(images) {
  this.images = images;
  this.currentImageIndex = 0;

  this.jumpRelative = function(amount) {
    this.currentImageIndex =
      (this.images.length +
      this.currentImageIndex +
      amount) %
      this.images.length;
  }

  this.next = function() {
    this.jumpRelative(1);
  }

  this.prev = function() {
    this.jumpRelative(-1);
  }

  this.getCurrentSrc = function() {
    return this.images[this.currentImageIndex];
  }
}
