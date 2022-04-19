$(()=>{
    $('form').submit(function(event){
      event.preventDefault()
      form = $("form")
      alert("success")
  
      $.ajax({
        'path':'/ajax/rate_project/',
        'type':'POST',
        'data':form.serialize(),
        'dataType':'json',
        'success': function(data){
          alert(data['success'])

        },
      })// END of Ajax method
      $('#id_usability').val('')
      $("#id_design").val('')
      $("#id_content").val('')
    }) // End of submit event
    
  
  }) // End of document ready function

