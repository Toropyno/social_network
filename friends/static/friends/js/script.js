import {getCookie} from '/static/posts/js/script.js'

const url = 'http://127.0.0.1:8000/api/v1/users/';

let friends = document.body.querySelectorAll('[data-wtf-object="friend"]');


document.body.addEventListener('click', function (event) {
  const elem = event.target;
  if (elem.dataset.wtfAction !== 'unfriend') return

  unfriend(elem.closest('[data-wtf-object="friend"]'))

})

async function unfriend(friend) {

  const final_url = url + `${friend.dataset.id}/unfriend/`
  const res = await fetch(final_url, {
    method: 'POST',
    headers: {
      'X-CSRFToken': getCookie('csrftoken'),
      'X-Requested-With': 'XMLHttpRequest',
    },
  })
  friend.remove()
}


document.body.addEventListener('click', function (event) {
  const elem = event.target;
  if (elem.dataset.wtfAction !== 'accept request') return

  accept_request(elem.closest('[data-wtf-object="follower"]'))

})

async function accept_request(request) {
  const final_url = url + `${request.dataset.id}/accept_request/`;
  const res = await fetch(final_url, {
    method: 'POST',
    headers: {
      'X-CSRFToken': getCookie('csrftoken'),
      'X-Requested-With': 'XMLHttpRequest',
    },
  })
  request.remove()
}