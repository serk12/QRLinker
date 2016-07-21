(function () {
    'use strict';

    var jq = window.jQuery;
    var guiValuePairs = [
        ['size', 'px'],
        ['minversion', ''],
        ['quiet', ' modules'],
        ['radius', '%'],
        ['msize', '%'],
        ['mposx', '%'],
        ['mposy', '%']
    ];

    function updateGui() {
        jq.each(guiValuePairs, function (idx, pair) {
            var $label = jq('label[for="' + pair[0] + '"]');
            $label.text($label.text().replace(/:.*/, ': ' + jq('#' + pair[0]).val() + pair[1]));
        });
    }

    function updateQrCode() {
        var options = {
            render: jq('#render').val(),
            ecLevel: jq('#eclevel').val(),
            minVersion: parseInt(jq('#minversion').val(), 10),

            fill: jq('#fill').val(),
            background: jq('#background').val(),
            // fill: jq('#img-buffer')[0],

            text: document.cookie,
            size: parseInt(400, 10),
            radius: parseInt(jq('#radius').val(), 10) * 0.01,
            quiet: parseInt(jq('#quiet').val(), 10),

            mode: parseInt(jq('#mode').val(), 10),

            mSize: parseInt(jq('#msize').val(), 10) * 0.01,
            mPosX: parseInt(jq('#mposx').val(), 10) * 0.01,
            mPosY: parseInt(jq('#mposy').val(), 10) * 0.01,

            label: jq('#label').val(),
            fontname: jq('#font').val(),
            fontcolor: jq('#fontcolor').val(),

            image: jq('#img-buffer')[0]
        };

        jq('#container').empty().qrcode(options);
    }

    function update() {
        updateGui();
        updateQrCode();
    }

    function onImageInput() {
        var input = jq('#image')[0];
        if (input.files && input.files[0]) {
            var reader = new FileReader();
            reader.onload = function (event) {
                jq('#img-buffer').attr('src', event.target.result);
                jq('#mode').val('4');
                setTimeout(update, 250);
            };
            reader.readAsDataURL(input.files[0]);
        }
    }

    function download() {
        jq('#download').attr('href', jq('#container canvas')[0].toDataURL('image/png'));
    }

    function init() {
        jq('#download').on('click', download);
        jq('#image').on('change', onImageInput);
        jq('input, textarea, select').on('input change', update);
        jq(window).load(update);
        update();
    }
    
    //funcion to server get getPass
    function updateID() { 
        var posting = $.post('new_token');
        posting.done(function(data) {
            document.cookie = 'cookie=' + data;
            update();
        });
        
    }
    
    setInterval(function() {updateID();}, 10*1000);

    setInterval(function() {
        
        var posting = $.post('is_registred', {cookie: document.cookie });
        posting.done(function(data) {
            if (data === '1') location.replace('./linked');
        });
    }, 1*1000);

    
    jq(init);
}());
