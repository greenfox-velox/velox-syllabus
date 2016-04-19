function alma(in) {
  if (in.majom === 1) {
    if (in.kecske === 1) {
      return 'good';
    } else {
      return 'goodish';
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
  if (in.majom === 1) {
    return 'goodish';
  }
  return 'bad';
}


 
