let toggle = document.querySelector('.toggle');
let hidden = document.querySelector('.hidden');
let button = document.querySelector('#counter');
let count = document.querySelector('#count');

let isHidden = true;

toggle.addEventListener('click', e => {
  if (isHidden) {
    hidden.style.display = 'block';
    isHidden = false;
  } else {
    hidden.style.display = 'none';
    isHidden = true;
  }

});

button.addEventListener('click', e => {
    window.fetch('/count', {'method': 'post'}).then(
      response => response.json()).then(json => {
        console.log(json);
        count.innerText = json.count;
      });
});
