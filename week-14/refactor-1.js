function alma(in) {
  if (in.majom === 1) {
    if (in.kecske === 1) {
      return 'good';
    }
  } else {
    return 'bad';
  }
}
 
// step 1
function alma(in) {
  if (in.majom === 1 && in.kecske === 1) {
    return 'good';
  }
  return 'bad';
}

// step 2
function alma(in) {
  if (isValidMajomAndKecske(in)) {
    return 'good';
  }
  return 'bad';
}

function isValidMajomAndKecske(in) {
  return in.majom === 1 && in.kecske === 1;
}

// Tape
test(function(t) {
  t.equal(alma({majom: 1, kecske: 1}), 'good');
  t.end();
});

test(function(t) {
  t.equal(alma({majom: 2, kecske: 4}), 'bad');
  t.end();
});

// jasmine
describe('alma', function() {
  it('should return good', function() {
    expect(alma({majom: 1, kecske: 1})).toBe('good');
  });
});
