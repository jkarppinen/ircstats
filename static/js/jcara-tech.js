$(document).ready(function() {
    new KonamiCode()
        .disable()
        .enable()
        .setListener(document.getElementsByTagName("body")[0])
        .setCallback(function (konamiCode) {
            konamiCode.disable();
            console.log("DONE");
            $('body div').first().addClass("flip-around");

        });
});
