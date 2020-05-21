
$(document).ready(function() {


    if ($(".success")[0]){
          $(function() {
            $( ".success" ).dialog({
                open: function(event, ui){
                 setTimeout("$('.success').dialog('close')",5000);
                },
                modal: false,
                // position: [100, 100],
                resizeable: false,
                draggable: false,
                autoOpen: true,
                show: {
                  effect: "fade",
                  duration: 1000,
                  },

                hide: {
                  effect: "fade",
                  duration: 500
                }
            });
          });
    }


    if ($(".error")[0]){
          $(function() {
            $( ".error" ).dialog({
              open: function(event, ui){
                 setTimeout("$('.error').dialog('close')",100000);
                },
                autoOpen: true,
                show: {
                  effect: "bounce",
                  duration: 1000,
                },

                hide: {
                  effect: "bounce",
                  duration: 500
                }
            });
          });
    }



   // Scroll Top Script
   //Check to see if the window is top if not then display button
    $(window).scroll(function(){
      if ($(this).scrollTop() > 300) {
        $('.scrollToTop').fadeIn();
      } else {
        $('.scrollToTop').fadeOut();
      }
    });

    //Click event to scroll to top
    $('.scrollToTop').click(function(){
      $('html, body').animate({scrollTop : 0},800);
      return false;
    });
   //END Scroll Top Script



    $(".jumbotron, .navbar").hide().fadeIn(1000);
    $('.jumbotron').ready(function () {
      $(".display-icons").hide().fadeIn(1000);
    })
    



    $('ul.nav li.dropdown').hover(function() {
        $(this).find('.dropdown-menu').stop(true, true).delay(300).slideDown(300);
      }, function() {
        $(this).find('.dropdown-menu').stop(true, true).delay(300).slideUp(300);
      });

    $("#id_start_date, #id_end_date").datetimepicker({format:'Y-m-d H:i',}); //Pick date and time manually

    // Pagination Script
    $('.table').paging({limit:15});
    // END Pagination Script
     
    $(".dateinput").datepicker({yearRange: '1930:2100', showButtonPanel: true, changeMonth: true, changeYear: true, dateFormat: 'yy-mm-dd'});

    NProgress.start();
    NProgress.done();


  setInterval(function(){
    document.getElementById("updatetime").innerHTML = (new Date()).toLocaleTimeString();
  }, 1000);


  $('.pannel').accordion({active: 0},{collapsible: true},{heightStyle: 'content'},{icons: {
                                                                                header: "ui-icon-plus",
                                                                                activeHeader: "ui-icon-minus"
                                                                              }
                                                                      }
                        );

  $('.tabs').tabs();


  // var forex = "forex";

  //   forexResults = url.search('forex');

  //   if (forexResults != -1){
  //       // $.each(results['hide'], function() {                     
  //       $("#id_transfer_type option[value='Local Transfer']").hide();
  //       // $("#edit-field-service-sub-cat-value option[@value=title]").hide();
  //     // }); 
  //   }
// $("#id_transfer_type option[value='Local Transfer']").hide();

  
});//Document.ready closing brace
