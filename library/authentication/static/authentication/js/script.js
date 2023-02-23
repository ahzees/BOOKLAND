
const elemLogin = document.querySelector('#description');
const elemCounter = elemLogin.nextElementSibling;
const maxLength = elemLogin.maxLength;
const updateCounter = (e) => {
    const len = e ? e.target.value.length : 0;
    elemCounter.textContent = `${len} / ${maxLength}`;
}
updateCounter();
elemLogin.addEventListener('keyup', updateCounter);
elemLogin.addEventListener('keydown', updateCounter);
