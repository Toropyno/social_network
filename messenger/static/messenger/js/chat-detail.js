import {getCookie} from "/static/posts/js/script.js";

const message_container = document.body.querySelector('[data-wtf-object="message container"]');
const textArea = document.querySelector('textarea[name="text"]');
const submitButton = document.querySelector('form button[type=submit]')

submitButton.addEventListener('click', function (event) {
  event.preventDefault()
  send_message()
});

get_messages()

const chatSocket = new WebSocket(
  'ws://'
  + window.location.host
  + window.location.pathname
);

chatSocket.addEventListener('message', function (event) {
  const data = JSON.parse(event.data);

  render_message(data.message)
});

chatSocket.addEventListener('close', function (evbent) {
  console.error('Chat socket closed unexpectedly');
})


async function get_messages() {

  const messages = await fetch(chat_url)
    .then(result => result.json())
  // console.log(res)
  for (const message of messages) {
    render_message(message)
  }
}

async function render_message(message) {

  const html_msg = `
<div class="row align-items-start mb-2">
  <div class="col-auto p-1 me-1">
    <img src="${message.author.photo}" alt="" class="wtf-avatar--xxs">
  </div>
  <div class="col px-0">
    <span>
      <a href="${message.author.absolute_url}" class="wtf-link text-primary">${message.author.first_name}</a>
    </span>
    <span class="wtf-date">${message.pub_date}</span>
    <div>
      <small style="white-space: pre-line">${message.text}</small>
    </div>
  </div>
</div>
      `
  message_container.insertAdjacentHTML('beforeend', html_msg)
  message_container.scrollTop = message_container.scrollHeight;
}



function send_message() {
  if (!textArea.value) return false;
  const msgForm = textArea.closest('form');
  const msgFormData = new FormData(msgForm);

  chatSocket.send(JSON.stringify(Object.fromEntries(msgFormData)))
  textArea.value = null;
}