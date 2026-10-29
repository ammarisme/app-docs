const playButton = document.querySelector('.promo-play');

if (playButton) {
  playButton.hidden = false;
  playButton.addEventListener('click', () => {
    const player = document.createElement('iframe');
    player.src = 'https://www.youtube-nocookie.com/embed/VTfyFgLmoS8?autoplay=1&rel=0';
    player.title = 'HabitFlip promotional video';
    player.allow = 'accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share';
    player.allowFullscreen = true;
    player.referrerPolicy = 'strict-origin-when-cross-origin';
    document.getElementById('promo-player').replaceChildren(player);
    player.focus();
  }, { once: true });
}
