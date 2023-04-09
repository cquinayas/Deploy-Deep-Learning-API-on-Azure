$("#chooseimg").on('click',function(){
    $("#predtext").hide();
    $("#tumorimg").hide();
});
$("#detecttum").on('click',function(){
    $( window ).load(function() {
      $("#predtext").show();
      $("#tumorimg").show();
    });
    
});