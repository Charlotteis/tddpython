/*global $, jQuery*/
jQuery(document).ready(function() {
    $("input[name='text']").on("keypress", function() {
        $(".has-error").hide();
    });

    // NOTE: THERE IS NOT TEST FOR THIS AS I CAN'T DO IT
    $("input[name='text']").on("click", function() {
        $(".has-error").hide();
    });
});
