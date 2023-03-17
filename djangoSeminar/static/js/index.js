const hello = document.querySelector('.hello');

// h1 태그가 클릭될 때 마다 콘솔에 hello 출력
hello.addEventListener('click', () => {
    console.log('hello');
});

const result = document.querySelector('.result');

if (is_authenticate) {
    result.textContent = "login successful";
} else {
    result.textContent = "login failed";
}