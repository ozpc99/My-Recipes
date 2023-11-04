// Automatically updates copyright year on base template footer.
$("#copyright").text(new Date().getFullYear());


// Bootstrap Popovers for the info buttons on 'Add Recipe' Form.
const popoverTriggerList = document.querySelectorAll('[data-bs-toggle="popover"]')
const popoverList = [...popoverTriggerList].map(popoverTriggerEl => new bootstrap.Popover(popoverTriggerEl))
const popover = new bootstrap.Popover('.popover-dismiss', {
  trigger: 'focus'
})