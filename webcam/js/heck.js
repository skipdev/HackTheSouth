function onLoad() {
   startTimers();
}

function startTimers() {
   var screen1 = setTimeout(function(){
      console.log('screen1 change works');
      document.getElementById('section1').style.display = 'none';
      document.getElementById('section2').style.display = 'block';}, 5000);

   var screen2 = setTimeout(function () {
      console.log('screen2 change works');
      document.getElementById('section2').style.display = 'none';
      document.getElementById('section3').style.display = 'block';}, 10000);

   var screen3 = setTimeout(function section_change3(screen3) {
      console.log('screen3 change works');
      document.getElementById('section3').style.display = 'none';
      document.getElementById('section4').style.display = 'block';}, 15000);

   var screen4 = setTimeout(function section_change3(screen4) {
      console.log('screen4 change works');
      document.getElementById('section4').style.display = 'none';
      document.getElementById('section5').style.display = 'block';}, 20000);

}

function change_text() {
   document.getElementById('text2speech').innerHTML = "yeeeeeet";
}