import {getCookie} from "/static/posts/js/script.js";

const url = 'http://127.0.0.1:8000/api/v1/users/';

let chat_links = document.body.querySelectorAll('[data-wtf-object="chat"]')
chat_links.forEach(link => {
  if (!link.href) {
    return get_chat_url(link)
  }
})

async function get_chat_url(chat_link) {
  const final_url = url + `${chat_link.dataset.clientId}/get_chat/`
  const res = await fetch(final_url, {
    method: 'POST',
    headers: {
      'X-CSRFToken': getCookie('csrftoken'),
      'X-Requested-With': 'XMLHttpRequest',
    },
  })
    .then(result => result.json())
  chat_link.href = res.absolute_url;
}

async function get_chat_list(user) {
  const final_url = url + `${chat_link.dataset.clientId}/get_chat/`
  const res = await fetch(final_url)

}