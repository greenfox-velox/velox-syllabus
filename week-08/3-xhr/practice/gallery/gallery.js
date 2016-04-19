'use strict';

function Gallery(images) {
  this.imageStorage = new ImageStorage(images);
  this.mainImage;
  this.nextButton;
  this.prevButton;

  this.initDom = function () {
    var _this = this;
    this.mainImage = document.querySelector('.main-image');
    this.nextButton = document.querySelector('.next');
    this.prevButton = document.querySelector('.prev');
    this.nextButton.addEventListener('click', function() {
      _this.handleMove('next');
    });
    this.prevButton.addEventListener('click', function() {
      _this.handleMove('prev');
    });
  }

  this.updateMainImage = function (src) {
    this.mainImage.setAttribute('src', src);
  }

  this.handleMove = function (direction) {
    this.imageStorage[direction]();
    this.updateMainImage(this.imageStorage.getCurrentSrc());
  }
}
