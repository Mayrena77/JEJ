$('.loginImage').hide();
$('.loginImage').fadeIn(2500);

var size = 450;
var s_size = 0.88 * size;
var m_size = 0.99 * size;
var s_resize = ( size - s_size )/2;
var m_resize = ( size - m_size )/2;
var image = $('.loginImage').css('width',size);

var x = image.offset().left;
var y = image.offset().top;

function pulse() {
    image.animate({
        width: s_size, top:x+s_resize,left:y+s_resize
    }, 450, function() {
        image.animate({
            width: size, top:x, left:y
        }, 200, function() {
            image.animate({
                width: m_size, top:x+m_resize, left:y+m_resize
            }, 90 ,function(){
                image.animate({
                    width: size, top:x , left:y
                }, 90, function() {
                   pulse();
                });
            });
        });
    });
};

pulse();
