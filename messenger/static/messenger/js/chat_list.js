import {getCookie} from "/static/posts/js/script.js";

const url = 'http://127.0.0.1:8000/api/v1/chats/';

get_chat_list()

async function get_chat_list() {

  const res = await fetch(url, {})
    .then(result => result.json())

  render_chat_list(res)
}

async function render_chat_list(chat_list) {
  const chat_container = document.body.querySelector('[data-wtf-object="chat container"]');
  for (let chat of chat_list) {
    const html_chat = `
      <a href="${chat.absolute_url}" class="col wtf-link px-1">
        <div class="row p-2 mx-1 d-flex wtf-chat--item">
          <div class="col-auto p-0">
            <img src="${chat.client.photo}" alt="" class="wtf-avatar--xs">
          </div>
            
          <div class="col">
            <div class="text-primary">${chat.client.full_name}</div>
            ${chat.last_message}
          </div>
          
          <div class="col-auto">
            <span class="wtf-date">${chat.last_update}</span>
          </div>
        </div>
      </a>
      `
    chat_container.insertAdjacentHTML('beforeend', html_chat)
  }
}