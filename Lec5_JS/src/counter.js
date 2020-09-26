if (!localStorage.getItem('cnt')) {
  localStorage.setItem('cnt', 0);
}


function counterFun() {
  let cnt = localStorage.getItem('cnt');
  const counterMsg = document.querySelector('h1');
  cnt++;
  counterMsg.innerHTML = cnt;
  localStorage.setItem('cnt', cnt);

  if (cnt % 10 === 0) {
    alert(`counter is now ${cnt}`);
  }
}
document.addEventListener('DOMContentLoaded', function () {
  document.querySelector('h1').innerHTML = localStorage.getItem('cnt');
  document.querySelector('button').onclick = counterFun;

  //setInterval(counterFun, 3000);
});

