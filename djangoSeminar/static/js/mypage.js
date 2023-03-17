// https://codong.tistory.com/28
// https://nachwon.github.io/how-to-send-csrf-token-ajax/
function get_cookie(name) {
    let cookie_value = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            let cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookie_value = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookie_value;
}

const csrf_token = get_cookie('csrftoken');

function push_heart_button() {
    fetch(heart_url, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",	// json형식의 값을 넘겨줌을 header에 명시
            "X-CSRFToken": csrf_token,
        }
    })
    .then(res => res.json())
    .then(result => {
        document.querySelector('.heart_count').textContent = result.heart_count;
    })
}

document.querySelector('.heart_button').addEventListener('click', push_heart_button);

function date_selected() {
    const date = document.querySelector('.date').value;
    fetch(date_url, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",	// json형식의 값을 넘겨줌을 header에 명시
            "X-CSRFToken": csrf_token,
        },
        body: JSON.stringify({"date": date}),
    })
    .then(res => res.json())
    .then(result => {
        document.querySelector('.date_print').textContent = result.selected;
    })
}

document.querySelector('.date_button').addEventListener('click', date_selected);
