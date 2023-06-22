$(function(){
    //executed when js-menu-icon is clicked
    $('.js-menu-icon').click(function(){
        //$(this) : self elements, js-menu-icon
        //next() : Next to div/js-menu-icon
        //toggle() : switch show and Hide
        $(this).next().toggle();
    })
})