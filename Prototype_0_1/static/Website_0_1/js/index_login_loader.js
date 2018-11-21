$(function() {
  $(".form-btn").on("click",function(e) {
    e.preventDefault();
    $(".hidden_content").hide();
    $("#"+this.id+"_form").show();
  });
});