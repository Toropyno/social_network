const url = 'http://127.0.0.1:8000/api/v1/posts/';

export {getCookie}

{
  // Лайки
  document.body.addEventListener('click', function (event) {
    const elem = event.target;
    if (!elem.classList.contains('likes-toggle')) return

    likesToggle(elem)

  })

  let toggles = document.body.querySelectorAll('.likes-toggle');
  toggles.forEach(toggle => isLiked(toggle))

  async function isLiked(toggle) {
    const final_url = url + `${toggle.dataset.id}/`;
    const res = await fetch(final_url)
      .then(result => result.json())
    if (res.is_fan) {
      like(toggle)
    }
  }

  function like(likesToggle) {
    likesToggle.classList.toggle('text-danger')
  }

  async function likesToggle(elem) {
    const likesCounter = elem.nextElementSibling;

    elem.classList.toggle('text-danger')

    let final_url;
    if (elem.classList.contains('text-danger')) {
      final_url = url + `${elem.dataset.id}/like/`;
    } else {
      final_url = url + `${elem.dataset.id}/unlike/`;
    }
    const res = await fetch(final_url, {
      method: 'POST',
      headers: {
        'X-CSRFToken': getCookie('csrftoken'),
        'X-Requested-With': 'XMLHttpRequest',
      },
    })
      .then(result => result.json())
    likesCounter.textContent = res.total_likes;
  }
  // Лайки
}

{
  // Записи
  document.body.addEventListener('click', async function (event) {
    const elem = event.target;
    if (elem.dataset.wtfAction !== 'remove post') return

    const post = elem.closest('[data-wtf-object="post"]');

    removePost(post)

  })

  async function removePost(post) {
    const final_url = url + `${post.dataset.id}/remove/`;

    const res = await fetch(final_url, {
      method: 'POST',
      headers: {
        'X-CSRFToken': getCookie('csrftoken'),
        'X-Requested-With': 'XMLHttpRequest',
      },
    })
    post.remove()
  }
  // Записи
}

function getCookie(name) {
  let matches = document.cookie.match(new RegExp(
    "(?:^|; )" + name.replace(/([\.$?*|{}\(\)\[\]\\\/\+^])/g, '\\$1') + "=([^;]*)"
  ));
  return matches ? decodeURIComponent(matches[1]) : undefined;
}