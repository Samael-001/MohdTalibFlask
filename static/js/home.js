$(function() {
  /* NOTE: hard-refresh the browser once you've updated this */
  $(".typed").typed({
    strings: [
      "./talib.human<br/>" + 
      "><span class='caret'>$</span> skills: python, core-linux, flask, penetesting<br/> ^100" +
      "><span class='caret'>$</span> job: intern at  <a href='https://www.tattvafoundation.org/'>Tattva Foundation</a><br/> ^100" +
      "><span class='caret'>$</span> hobbies: <a href='https://open.spotify.com/artist/1oyUjl52ohRrCv3EL1UdpM'>music,</a> ctf, <a href='https://clinerds.com'>writing</a><br/> ^300" +
      "><span class='caret'>$</span> alias: lunatic_samael <br/>" +
      "><span class='caret'>$</span> social: <a href='http://www.github.com/lunatic-samael/'>github</a> <a href='https://in.linkedin.com/in/cli-nerds-620064214'>linkedin</a> <a href='https://clinerds.com'>blog</a> <a href='http://www.instagram.com/lunatic_samael/'>instagram</a><br/>"
    ],
    showCursor: true,
    cursorChar: '_',
    autoInsertCss: true,
    typeSpeed: 0.001,
    startDelay: 50,
    loop: false,
    showCursor: false,
    onStart: $('.message form').hide(),
    onStop: $('.message form').show(),
    onTypingResumed: $('.message form').hide(),
    onTypingPaused: $('.message form').show(),
    onComplete: $('.message form').show(),
    onStringTyped: function(pos, self) {$('.message form').show();},
  });
  $('.message form').hide()
});
