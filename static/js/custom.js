document.addEventListener("DOMContentLoaded", function() {
    const audioPlayer = document.getElementById("audio-player");
    const playPauseButton = document.getElementById("play-pause-button");
    const playIcon = document.getElementById("play-icon");
    const pauseIcon = document.getElementById("pause-icon");
    const audioSlider = document.getElementById("audio-slider");
    const timeDisplay = document.getElementById("time-display");
  
    playPauseButton.addEventListener("click", () => {
      if (audioPlayer.paused) {
        audioPlayer.play();
        playIcon.classList.add("hidden");
        pauseIcon.classList.remove("hidden");
      } else {
        audioPlayer.pause();
        pauseIcon.classList.add("hidden");
        playIcon.classList.remove("hidden");
      }
    });
  
    audioPlayer.addEventListener("timeupdate", () => {
      audioSlider.value = (audioPlayer.currentTime / audioPlayer.duration) * 100;
      const minutes = Math.floor(audioPlayer.currentTime / 60);
      const seconds = Math.floor(audioPlayer.currentTime - minutes * 60);
      const durationMinutes = Math.floor(audioPlayer.duration / 60);
      const durationSeconds = Math.floor(audioPlayer.duration - durationMinutes * 60);
      timeDisplay.textContent = `${minutes}:${seconds < 10 ? '0' + seconds : seconds} / ${durationMinutes}:${durationSeconds < 10 ? '0' + durationSeconds : durationSeconds}`;
    });
  
    audioSlider.addEventListener("input", () => {
      audioPlayer.currentTime = (audioSlider.value / 100) * audioPlayer.duration;
    });
  
    window.playTrack = function(url, trackName, artistName) {
      audioPlayer.src = url;
      audioPlayer.play();
      document.getElementById('track-title').innerText = trackName;
      document.getElementById('artist-name').innerText = artistName;

      playIcon.classList.add("hidden");
      pauseIcon.classList.remove("hidden");
    }
  });