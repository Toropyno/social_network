{
  // Делегирование для прикрепленных к сообщению фото
  document.body.addEventListener('change', function (event) {
    let target = event.target;
    if (!(target.tagName === 'INPUT' && target.classList.contains('attachment'))) return;

    let closeButton = document.createElement('i');
    closeButton.classList.add('bi');
    closeButton.classList.add('bi-x');
    closeButton.classList.add('wtf-upload--img-x');

    let formPost = target.closest('form');
    let uploadContainer = formPost.querySelector('div.upload-container');

    let image = document.createElement('img');
    image.classList.add('wtf-upload--img');
    image.classList.add('py-2');
    if (target.files[0]) {
      let img = uploadContainer.querySelector('img');
      if (img) {
        img.remove();
      }
      image.src = URL.createObjectURL(target.files[0]);
      uploadContainer.append(image);
      uploadContainer.append(closeButton);
    } else {
      uploadContainer.innerHTML = null;
    }
  })
}

{
  //  Делегирование для кнопок закрывающих иконки фото
  document.body.addEventListener('click', function (event) {
    let target = event.target;
    if (!(target.tagName === 'I' && target.classList.contains('bi-x'))) return;

    let formPost = target.closest('form');
    formPost.querySelector('div.upload-container').innerHTML = null;
    formPost.querySelector('input.attachment').value = null;

  })
}
