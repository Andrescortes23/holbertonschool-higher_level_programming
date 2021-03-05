$.get('https://swapi-api.hbtn.io/api/people/5/?format=json', (responseText, textStatus) => {
  if (textStatus) {
    $('DIV#character').text(responseText.name);
  }
});
