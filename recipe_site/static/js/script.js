// Automatically updates copyright year on base template footer
$("#copyright").text(new Date().getFullYear());


// Automatically updates Post Date to Today's Date on Add Recipe Form
document.getElementById('post_date').valueAsDate = new Date();


// Bootstrap Popovers for the info buttons on the Add Recipe Form
const popoverTriggerList = document.querySelectorAll('[data-bs-toggle="popover"]')
const popoverList = [...popoverTriggerList].map(popoverTriggerEl => new bootstrap.Popover(popoverTriggerEl))
const popover = new bootstrap.Popover('.popover-dismiss', {
  trigger: 'focus'
})