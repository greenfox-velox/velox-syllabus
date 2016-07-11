function getTodos() {
  var xhr = new XMLHttpRequest();
  xhr.open('GET', url);
  xhr.onload = function() {
    if (xhr.readyState === 4) {
      var data = JSON.parse(xhr.responseText);
      data.forEach(function (e, i) {
        createAnElement(data[i].id, data[i].text);
        if (e.completed) {
          document.getElementById('chk'+data[i].id).classList.add('checked');
        }
      })
    }
  };
  xhr.send();
}
