
alert('hello worl ')
 const alertbox = document.getElementById('alert-box')
 const imagbox  = document.getElementById('image-box')
 const form = document.getElementById('form-id')

 const formFile =  document.getElementById('formFile')
 const email = document.getElementById('emailinput')
 const username = document.getElementById('usernameinput')
 const fullname = document.getElementById('fullnameinput')
 const crsf = document.getElementsByName('csrfmiddlewaretoken')

 const url = ""
 const aletbox = (type,text)=>{
     alertbox.innerHTML = `<div class="alert alert-${type}" role="alert">
    ${text}
   </div>`
 }
 formFile.addEventListener('change',()=>{
     const imagefile = formFile.files[0]
     const myurl = URL.createObjectURL(imagefile)
    
     imagbox.innerHTML = `<img src="${myurl}" width="100%">`})

form.addEventListener('submit', e=>{
    e.preventDefault()
    const formdata = new FormData()
    formdata.append('csrfmiddlewaretoken', crsf[0].value)
    formdata.append('formFile', formFile.files[0])
    formdata.append('email', email.value)
    formdata.append('username', username.value)
    formdata.append('fullname',fullname.value )
  

$.ajax({
    type: "POST",
    url: url,
    data: formdata,
    enctype: 'multipart/form-data',
   
    success: function(response){
        console.log(response)
        const sText = `sucessfully saved ${response.username}`
        aletbox('success', sText)

         
    },
    error:  function(error){
        console.log(error)
        aletbox('danger', 'ooop something want bad fix and try again')
    },
    cache: false,
    contentType: false,
    processData: false,
    
    
})

})