$(function () {
    var sliderNav = $(".header__slider__nav__i"),
        slide = $(".header__slider img"),
        slideText = $(".header__slider__text");
    slide.eq(0).show().addClass("_active");
    slideText.eq(0).show().addClass("_active");
    sliderNav.eq(0).addClass("_active");
    function rotate() {
        var indexAct = $(".header__slider img._active").index();
        if (!slide.eq(indexAct).next().length == 0) {
            slide.eq(indexAct).next().fadeIn(1000).addClass("_active").end().fadeOut(1000).removeClass("_active");
            slideText.eq(indexAct).next().fadeIn(1000).addClass("_active").end().fadeOut(1000).removeClass("_active");
            sliderNav.eq(indexAct).next().addClass("_active").end().removeClass("_active");
        }
        else {
            slide.eq(indexAct).fadeOut(1000).removeClass("_active");
            slideText.eq(indexAct).fadeOut(1000).removeClass("_active");
            sliderNav.eq(indexAct).removeClass("_active");
            slide.eq(0).fadeIn(1000).addClass("_active");
            slideText.eq(0).fadeIn(1000).addClass("_active");
            sliderNav.eq(0).addClass("_active");
        }

    }
    var auto = setInterval(rotate, 4000);

    sliderNav.click(function(){
        clearInterval(auto);
        slide.stop();
        if(!slide.is(":animated")){
            var index = $(this).index();
            slide.fadeOut(1000).removeClass("_active");
            slide.eq(index).fadeIn(1000).addClass("_active");
            slideText.fadeOut(1000).removeClass("_active");
            slideText.eq(index).fadeIn(1000).addClass("_active");
            sliderNav.removeClass("_active");
            sliderNav.eq(index).addClass("_active");
            auto = setInterval(rotate, 4000);

        }
    });


    $(".header__btn-call").click(function(){
        $(".popup-wrp").fadeIn(500);

    });

    $(".popup-close").click(function(){
        $(".popup-wrp").fadeOut(500);
    });
    
    $(".header__btn-application").click(function(){
        console.log('***');
        $(".popup-wrp-r").fadeIn(500);

    });

    $(".popup-close-r").click(function(){
        $(".popup-wrp-r").fadeOut(500);
    });
    
//     $('body').on('click', '.popup-wrp', function (e) {
//         if (!$(e.target).closest('.popup').length==0) {
//             return false;
//         }
//         popupWrp.fadeOut();
//         e.stopPropagation();
//     });
});